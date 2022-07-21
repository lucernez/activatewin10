import os
def activate(version):
    if version == 2 or version == "2":
        os.system("slmgr /ipk 8N67H-M3CY9-QT7C4-2TR7M-TXYCV")
        os.system("slmgr /skms kms.digiboy.ir")
        os.system("slmgr /ato")
    elif version == 1 or version == "1":
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms kms.xspace.in")
        os.system("slmgr /ato")
def main():
    version = int(input("Enter your version: \n1-Windows 10 home\n2-Windows 10 Pro"))
    activate(version=version)
if __name__ == "__main__":
    main()