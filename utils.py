import os
import shutil
import sys
import winreg
import platform
import subprocess
import psutil
import logging

def add_to_startup():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        
        executable_path = os.path.abspath(sys.executable)
        
        winreg.SetValueEx(key, "MyStartupKey", 0, winreg.REG_SZ, executable_path)
        
        winreg.CloseKey(key)
        print("[INFO] Added to startup.")
    except Exception as e:
        print(f"[ERROR] Failed to add to startup: {e}")

def remove_from_startup():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        
        winreg.DeleteValue(key, "MyStartupKey")
        
        winreg.CloseKey(key)
        print("[INFO] Removed from startup.")
    except Exception as e:
        print(f"[ERROR] Failed to remove from startup: {e}")

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"[INFO] Copied {src} to {dst}.")
    except Exception as e:
        print(f"[ERROR] Failed to copy file: {e}")

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        print(f"[INFO] Moved {src} to {dst}.")
    except Exception as e:
        print(f"[ERROR] Failed to move file: {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"[INFO] Deleted {file_path}.")
    except Exception as e:
        print(f"[ERROR] Failed to delete file: {e}")

def get_system_info():
    try:
        system_info = {
            "system": platform.system(),
            "node_name": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cpu_count": psutil.cpu_count(logical=True),
            "total_ram": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        }
        return system_info
    except Exception as e:
        print(f"[ERROR] Failed to get system info: {e}")
        return {}

def ping(host):
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        return result.stdout
    except Exception as e:
        logging.error(f"[ERROR] Failed to ping {host}: {e}")
        return None

def traceroute(host):
    try:
        result = subprocess.run(["tracert", host], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        return result.stdout
    except Exception as e:
        logging.error(f"[ERROR] Failed to traceroute {host}: {e}")
        return None