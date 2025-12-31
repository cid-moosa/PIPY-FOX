
**PIPY FOX** is a single-file Python 3 CLI automation script for **TP-Link USB Wi-Fi adapters (V2 / V3)**.  
Its primary aim is to install drivers that enable **monitor mode** and **packet injection** where the driver/chipset supports those features — for legitimate research, testing, and educational use.

> **Important:** PIPY FOX automates installation only. It does **not** create or claim ownership of the drivers. Drivers remain the intellectual property of their original authors.

---

## Quick facts

- Project file: `pipy_fox.py` (single file)  
- Target: **Kali Linux / Parrot OS** (Linux)  
- Requires: Python **3.8+**, `sudo`/root, internet access  
- Behavior: Downloads needed files, installs drivers, then removes downloaded files and (by default) prompts to delete the installer script itself (self-destruct).

---

## Supported Models — V2 / V3

Targets **TP-Link USB Wi-Fi adapters V2 / V3**.  
Later revisions that use the **same Realtek chipset** are likely compatible.

**Primary aim:** Enable **monitor mode** and **packet injection** (where supported) for lawful research and testing.

> **Note:** V1 adapters are plug-and-play and are not targeted by this project.

---

## Quick Start — Copy/paste steps

> Replace `USERNAME/REPOSITORY` with your GitHub path and ensure `pipy_fox.py` is the script filename.

```bash
# ---------------------------
# 1) Verify the adapter is visible
# ---------------------------
lsusb
# optional filtered search:
lsusb | grep -i tp-link || lsusb | grep -i realtek

# ---------------------------
# 2) Clone the repository
# ---------------------------
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY

# ---------------------------
# 3) (Optional) Create & activate a Python virtual environment
# ---------------------------
python3 -m venv .venv
source .venv/bin/activate

# ---------------------------
# 4) (Optional) Install Python dependencies if a requirements.txt exists
# ---------------------------
if [ -f requirements.txt ]; then
  pip install --upgrade pip
  pip install -r requirements.txt
fi

# ---------------------------
# 5) Run the installer (normal mode)
# ---------------------------
sudo python3 pipy_fox.py

# or: switch to root first, then run:
# sudo su
# python3 pipy_fox.py

# When prompted at the end:
#  - press 'y' to confirm removing downloaded files and delete the installer (self-destruct)
#  - press 'n' to keep files for inspection

# ---------------------------
# 6) Run the installer (debug / inspect mode — if supported by the script)
# ---------------------------
sudo python3 pipy_fox.py --no-cleanup --verbose

# ---------------------------
# 7) If a reboot is recommended by the script
# ---------------------------
sudo reboot

# ---------------------------
# 8) Quick troubleshooting commands
# ---------------------------
# Check kernel messages after plugging the adapter in
dmesg | tail -n 50

# Re-check USB devices
lsusb

# Inspect detailed USB info for a specific VID:PID (example)
# lsusb -v -d 0bda:8179
