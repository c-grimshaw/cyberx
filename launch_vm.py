"""
Short script to support different connection proxies for different VM boxes
through VMRC.

Change the constants at the top of the file, and then save this script. 

Use the file extension *.pyw in order to suppress the Python console
window from launching when using this script as a shortcut.
"""
from subprocess import call

# CHANGE: Server Address + Port
PROXY_URI = "http://rmcg.wins.cyber.x:9001/"
# CHANGE: VMRC URL for remote VM
MACHINE_IP = "vmrc://123.456.789.000/?moid=000"
# CHANGE: Absolute path to the preferences.ini file used by VMRC
CONFIG_PATH = r"C:\Users\Charlie\AppData\Roaming\VMware\preferences.ini"

# NO CHANGE (on default install): Absolute path to VMRC executable
VMRC_PATH = r"C:\Program Files (x86)\VMware\VMware Remote Console\vmrc.exe"


def main():
    """Read config, change proxy settings, re-write config, launch VMRC"""
    with open(CONFIG_PATH, encoding="utf-8") as file:
        config = file.readlines()

    for i, line in enumerate(config):
        if "pref.remoteVMConnProxy.uri" in line:
            config[i] = f"pref.remoteVMConnProxy.uri = {PROXY_URI}\n"
            break

    with open(CONFIG_PATH, encoding="utf-8", mode="w") as file:
        file.writelines(config)

    call([VMRC_PATH, MACHINE_IP])


if __name__ == "__main__":
    main()
