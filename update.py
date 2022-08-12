import os
import platform

update = input("Would you like to update your machine?:\n")
if update.lower() == "yes":
    x = "debian"
    v = "arch"
    z = "fc"
    print("Checking distro...")
    if v in platform.platform(): # Arch updating
        os.system('sudo pacman -Syu')
        os.system('yay -Syu')
    elif x in platform.platform(): # Debian updating
        os.system('sudo apt update && sudo apt upgrade -y')
    elif v in platform.platform(): # Fedora updating
        os.system('sudo dnf update && sudo dnf upgrade -y')
    else:
        print("Could not find OS in selection.")
        exit()
    # Update should be done.
    print("Done updating.")
else:
    exit()
