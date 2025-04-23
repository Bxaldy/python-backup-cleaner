# python-backup-cleaner
# 🧹 Backup Cleaner

This is a simple Python tool that helps clean up old backup files while preserving those created in key months like **December** and **January** (or whatever you want). I originally built it back in 2019 while working as a junior sysadmin and learning Python by solving real problems in our infrastructure.

> ⚠️ This project was created strictly for educational purposes, but it ended up being quite practical too!

---

## 📂 Versions

### 🟢 v1 - Config File Based ([`v1-config-file/`](./v1)) - December 2019
- Reads configuration from a `config.ini` file.
- Suitable for converting to a `.exe` file (e.g., using PyInstaller).
- Simple for non-technical users or for static configurations — just double-click to run.


### ⚙️ v2 - Command-Line Version ([`v2-cli-version/`](./v2)) - January 2020
- Accepts arguments directly from the terminal (using `argparse`).
- More flexible and better suited for automation, cron jobs, or CI/CD tasks.
- No config file needed — you provide everything at runtime.

---

🧯 Safety Notes
Whether you use the config.ini version or the CLI version:

Always double-check paths, days, and exception months before execution.

Be aware that:

If exceptionMonth1/2 are missing (in config file), the script will crash.

If exceptionMonth1/2 = 0, or invalid months are used (like 0 or >12), the script will not exclude any files, potentially deleting everything older than the given threshold.

If --days is set to 0, the script will treat all files (except excluded months) as ready to delete.


## 🔧 What It Does

Both versions:
- Recursively scan a target directory.
- Identify files older than a defined number of days.
- **Exclude** files modified in specific months (e.g. December and January).
- Log actions to a `.log` file for auditing.

---

## 🧪 Why This Exists

I created this script when I had to manage a large backup storage system and make sure it stayed clean without accidentally deleting important year-end data. It also became a way for me to:
- Learn the Python basics (file handling, `os`, `datetime`, `configparser`)
- Write code that interacts with the real world
- Understand how automation improves sysadmin workflows

---

## 👤 Author

**Ionuț Gabriel Buicu**  
Script originally written in **2019**  
Feel free to use or improve it as you like!

---

---

⚠️ **Disclaimer**

This script was created for educational purposes only. Use it at your own risk.
The author is not responsible for any data loss or damage caused by improper use of this tool.

---

## 🪪 License

No formal license — feel free to use or modify this code however you like!  
I accept donations in beers and 35mm film rolls. 🍻📸

![MemesFelizNocheGIF](https://github.com/user-attachments/assets/3dfa2abe-f5d5-49a8-9a1f-3d3427432849)


