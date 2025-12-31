import os
import shutil
import subprocess
import time
import sys
import itertools
import zipfile
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinner_animation(message, duration=5):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{Fore.YELLOW}{message} {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\r", end="")

def globe_spin(duration=3):
    frames = ['🌍', '🌎', '🌏']
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f"\r{Fore.CYAN}Downloading driver files... {frame}")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\r", end="")

def dying_fox():
    clear()
    frames = [
        r"  (\_/)" ,
        r"  (x_x)  *ACK*",
        r" <(__)>  goodbye...",
        r"  || ||"
    ]
    for frame in frames:
        print(Fore.RED + frame)
        time.sleep(1)

logo = f"""
{Fore.MAGENTA}
░█████████  ░██████░█████████  ░██     ░██    ░██████████  ░██████   ░██    ░██
░██     ░██   ░██  ░██     ░██  ░██   ░██     ░██         ░██   ░██   ░██  ░██
░██     ░██   ░██  ░██     ░██   ░██ ░██      ░██        ░██     ░██   ░██░██
░█████████    ░██  ░█████████     ░████       ░█████████ ░██     ░██    ░███
░██           ░██  ░██             ░██        ░██        ░██     ░██   ░██░██
░██           ░██  ░██             ░██        ░██         ░██   ░██   ░██  ░██
░██         ░██████░██             ░██        ░██          ░██████   ░██    ░██
"""

def banner():
    clear()
    print(logo)
    input(f"\n{Fore.GREEN}[ PRESS ENTER TO CONTINUE ]")

model_text = f"""
{Fore.MAGENTA}
░██████████░██                 ░██       ░██ ░███    ░██ ░█████████  ░██████   ░██████  ░███    ░██
    ░██    ░██                 ░██       ░██ ░████   ░██ ░██    ░██ ░██   ░██ ░██   ░██ ░████   ░██
    ░██    ░██                 ░██  ░██  ░██ ░██░██  ░██       ░██        ░██       ░██ ░██░██  ░██
    ░██    ░██         ░██████ ░██ ░████ ░██ ░██ ░██ ░██      ░██     ░█████    ░█████  ░██ ░██ ░██
    ░██    ░██                 ░██░██ ░██░██ ░██  ░██░██     ░██     ░██       ░██      ░██  ░██░██
    ░██    ░██                 ░████   ░████ ░██   ░████     ░██    ░██       ░██       ░██   ░████
    ░██    ░██████████         ░███     ░███ ░██    ░███     ░██    ░████████ ░████████ ░██    ░███
"""

def disclaimer():
    clear()
    print(model_text)
    print(f"""
{Fore.YELLOW}
┌────────────────────────────────────────────────────────────────────────────┐
│                                DISCLAIMER                                  │
│  Installs drivers for the TP-Link TL-WN722N adapter (RTL8188eus chipset).  │
│  Requires Debian/Ubuntu-like system with sudo privileges.                  │
└────────────────────────────────────────────────────────────────────────────┘
""")
    input(f"\n{Fore.GREEN}[ PRESS ENTER TO CONTINUE ]")

def download_tarball(repo_url, dest_dir):
    """Fallback: download GitHub repo as tarball and extract."""
    archive = "repo.tar.gz"
    try:
        print(Fore.CYAN + "[*] Downloading tarball...")
        subprocess.run(["wget", f"{repo_url}/archive/refs/heads/master.tar.gz", "-O", archive], check=True)
        print(Fore.CYAN + "[*] Extracting archive...")
        shutil.unpack_archive(archive, dest_dir)
        # The extracted folder name ends with -master
        extracted = next(d for d in os.listdir(dest_dir) if d.endswith("-master"))
        os.rename(os.path.join(dest_dir, extracted), dest_dir)
        os.remove(archive)
        return True
    except Exception as e:
        print(Fore.RED + f"[✗] Tarball fallback failed: {e}")
        return False

def install_driver():
    if os.geteuid() != 0:
        print(Fore.RED + "[✗] Please run this script with sudo or as root.")
        sys.exit(1)

    repo_dir = "rtl8188eus"
    if os.path.isdir(repo_dir):
        print(Fore.YELLOW + f"[!] Removing existing '{repo_dir}' folder.")
        shutil.rmtree(repo_dir)

    globe_spin(4)
    repo_url = "https://github.com/aircrack-ng/rtl8188eus"
    cloned = False

    # Attempt git clone
    try:
        print(Fore.CYAN + "[*] Cloning repository via Git...")
        subprocess.run([
            "git", "clone", repo_url + ".git", repo_dir
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        cloned = True
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "[✗] Git clone failed:")
        print(Fore.RED + e.stderr.strip())

    # Fallback to tarball if clone failed
    if not cloned:
        if input(Fore.YELLOW + "[?] Clone failed. Try tarball fallback? (y/n): ").lower() == 'y':
            success = download_tarball(repo_url, repo_dir)
            if not success:
                print(Fore.RED + "[✗] Could not obtain source. Exiting.")
                sys.exit(1)
        else:
            sys.exit(1)

    spinner_animation("Building & installing driver...", 5)
    try:
        subprocess.run(["make", "-C", repo_dir, "dkms-install"], check=True)
        subprocess.run(
            ["tee", "/etc/modprobe.d/blacklist-rtl8xxxu.conf"],
            input="blacklist rtl8xxxu\n", text=True,
            stdout=subprocess.DEVNULL, check=True
        )
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[✗] Build/install error: {e}")
        sys.exit(1)

    print(Fore.GREEN + "\n[✓] Driver installed successfully!")
    time.sleep(1)
    dying_fox()

    if input(Fore.YELLOW + "\n[?] Delete this installer script? (y/n): ").lower() == 'y':
        try:
            os.remove(os.path.abspath(__file__))
            print(Fore.RED + "[!] Script deleted.")
        except Exception:
            pass

    if input(Fore.YELLOW + "\n[?] Reboot now to apply changes? (y/n): ").lower() == 'y':
        subprocess.run(["sudo", "reboot"])


def main():
    banner()
    disclaimer()
    install_driver()

if __name__ == '__main__':
    main()
