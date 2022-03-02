"""
Short script to support different connection proxies for different VM boxes.

Change the constants at the top of the file, and then save this script.

Use the file extension *.pyw in order to suppress the Python console
window from launching when using this script as a shortcut.
"""
from fileinput import FileInput
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
    """Modify config in-place, launch VMRC"""
    with FileInput(files=CONFIG_PATH, encoding="utf-8", inplace=True) as file:
        for line in file:
            if "pref.remoteVMConnProxy.uri" in line:
                print(f"pref.remoteVMConnProxy.uri = {PROXY_URI}", end="")
            else:
                print(line, end="")

    call([VMRC_PATH, MACHINE_IP])


if __name__ == "__main__":
    main()
