
**PIPY FOX** is a single-file Python 3 CLI automation script built for **Kali Linux and Parrot OS**.  
It automates installing drivers for **TP-Link USB Wi-Fi adapters (V2 / V3)**.

The main goal of this automation is to install drivers that allow **monitor mode** and **packet injection** *where the driver and chipset support those features*.

> ⚠️ PIPY FOX does **not** create, modify, or own any drivers.  
> It only automates the installation process.  
> All rights and responsibility for the drivers belong to their original authors.

---

## What this project does

- Uses **one Python file** (`pipy_fox.py`)
- Runs fully in the terminal (CLI)
- Shows simple animations during installation
- Downloads required driver files from upstream sources
- Installs the driver automatically
- Deletes downloaded files after installation
- Prompts the user to delete the installer script itself (self-destruct)

---

## Supported models

This project targets **TP-Link USB Wi-Fi adapters V2 / V3**.

Some newer revisions of the same models use the **same Realtek chipset** and behave exactly like V2 / V3.  
If your adapter uses the same chipset, it will usually work the same way.

> V1 adapters are plug-and-play and are **not** targeted by this project.

---

## Requirements

- Kali Linux or Parrot OS  
- Python **3.8 or newer**
- Root / `sudo` access
- Internet connection (to download drivers)

---

## Installation & Usage (Step-by-Step)

## STEP 1 
Plug in the adapter and verify detection

Open a terminal and run:
```bash
lsusb
```

##STEP 2 Clone the repository
```
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

##STEP 3 Run PIPY FOX
```
sudo python3 pipy_fox.py
```

##STEP 4 Reboot
```
sudo reboot
```
