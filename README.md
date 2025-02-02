# Remote Access & System Management Tool

## ⚠ Disclaimer
**This project is strictly for educational and research purposes only.** It should only be used in controlled environments with explicit permission. Unauthorized use on systems without consent may violate ethical and legal guidelines. The developers assume no responsibility for misuse.

---

## 📖 Overview
This tool enables remote access and system management capabilities by integrating with Discord, allowing users to execute commands on a Windows machine remotely. 
It provides features such as:
- **Screen recording & monitoring**
- **Process control & termination**
- **File operations (upload/download/delete)**
- **System diagnostics and network monitoring**
- **Persistence mechanisms (startup entry, hidden execution)**
- **Windows security research (bypassing UAC & Defender for educational analysis)**

This software should only be used with **full authorization and consent** for research and learning purposes.

---

## 🚀 Features (Detailed Breakdown)

### 🎥 Screen Capture & Recording
- Captures screenshots or video recordings remotely.
- Supports adjustable resolution, frame rate, and optional audio recording.
- Automatically deletes temporary recording files after transmission.

### 🔌 System Control
- Remotely **shutdown**, **restart**, or **lock** the system.
- Only supported on Windows platforms.

### 📝 Process Management
- Lists running processes.
- Allows killing specified processes by name.

### 📂 File Operations
- Upload and download files remotely.
- Delete or move files on the system.
- Supports file handling via Discord commands.

### 🔍 Network Diagnostics
- Perform **ping** and **traceroute** commands remotely.
- Collect network performance insights.

### 🛡 Security Research (Educational Bypass Techniques)
- Demonstrates methods to **bypass User Account Control (UAC)** for privilege escalation.
- Temporarily **disables Windows Defender** using registry and PowerShell methods.
- Provides insight into security vulnerabilities (for research purposes only).

### 🖥 Persistence Methods
- Automatically adds itself to Windows startup.
- Ensures continuous execution after system reboot.
- Can be manually removed via registry.

### 🤖 Discord Bot Integration
- Executes commands via Discord messages.
- Provides an interactive control interface.

---

## 📷 Screenshots (Placeholders)

![Placeholder for Screenshot 1](https://imgur.com/undefined)

![Placeholder for Screenshot 1](images/screenshot1.png)

![Placeholder for Screenshot 1](images/screenshot1.png)

![Placeholder for Screenshot 2](images/screenshot2.png)

---

## 🛠 Installation & Setup Guide

### 🔧 Prerequisites
Before running this tool, ensure the following:
- **Python 3.x installed** on the system.
- Install the required dependencies:
  ```bash
  pip install discord mss numpy opencv-python sounddevice soundfile psutil requests
  ```
- Set up a **Discord bot token** and replace `YOUR_BOT_TOKEN` in `client.py`.

### 🏗️ Running the Program
To launch the bot, execute:
```bash
python client.py
```
This will initialize the first-time setup, including startup persistence and security bypass demonstrations.

---

## 🔨 Compiling to .EXE
To convert this Python script into a standalone Windows executable:

1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Compile the script with the following command:
   ```bash
   pyinstaller --onefile --noconsole --icon=icon.ico client.py
   ```
3. The compiled `.exe` file will be available in the `dist/` directory.

---

## 🛑 Ethical & Legal Notice
- This tool **must only** be used on systems **you own or have explicit permission to access**.
- Misuse of this software can have **severe legal consequences**.
- **The developers are not liable for unethical or illegal use.**
- Conducting security research without consent is strictly prohibited.

---

## 🏆 Credits
- Developed for **educational cybersecurity research**.
- Inspired by ethical hacking, malware analysis, and penetration testing.
- Contributions & improvements are welcome.

---

## 📥 Download
This documentation is available for download as a `.txt` file. Click the button below to save it:
