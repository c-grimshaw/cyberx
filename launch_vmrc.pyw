"""
Script to support different connection proxy settings for different VM instances.

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


def modify(file, setting):
    """Replace config key with user-defined value"""
    for line in file:
        if setting in line: print(f"{setting} = {PROXY_URI}", end="")
        else: print(line, end="")
            

def main():
    """Modify config, launch VMRC"""
    with FileInput(files=CONFIG_PATH, encoding="utf-8", inplace=True) as config:
        modify(config, "pref.remoteVMConnProxy.uri")

    call([VMRC_PATH, MACHINE_IP])


if __name__ == "__main__":
    main()
