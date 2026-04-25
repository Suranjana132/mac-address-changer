
#!/usr/bin/env python3

import subprocess
import argparse
import re

# -------- ARGPARSE --------
parser = argparse.ArgumentParser(description="MAC Address Changer Tool")

parser.add_argument("-i", "--interface", help="Network Interface", required=True)
parser.add_argument("-m", "--mac", help="New MAC Address", required=True)

args = parser.parse_args()

# -------- VALIDATION --------
def is_valid_mac(mac):
    pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$"
    return re.match(pattern, mac)

# -------- LOGIC --------
if is_valid_mac(args.mac):
    print(f"\n[+] Changing MAC address for {args.interface} to {args.mac}")

    subprocess.call(["ifconfig", args.interface, "down"])
    subprocess.call(["ifconfig", args.interface, "hw", "ether", args.mac])
    subprocess.call(["ifconfig", args.interface, "up"])

    print("[+] MAC address changed successfully ✅")

    # -------- VERIFY --------
    print("\n[+] Current MAC address:")
    result = subprocess.run(
        ["ifconfig", args.interface],
        capture_output=True,
        text=True
    )
    print(result.stdout)

else:
    print("[-] Invalid MAC address ❌")
