from Wmi_helper import WMISearcher


def baseboard():
    try:
        params = ["Manufacturer", "Product", "SerialNumber", "Status", "Version"];
        wmisercher = WMISearcher('Win32_BaseBoard', params)
        baseboard = wmisercher.get()
        return baseboard
    except  Exception as ex:
        print(ex)
        return baseboard
    
if __name__ == "__main__":
    print(baseboard())