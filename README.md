# wmi-python
Wmi-python is piece of python script with help of .net. It is help to easily execute wmi query in python

## Installation

Use the package manager [pip](https://pypi.org/project/pythonnet) to install pythonnet.

```bash
pip install pythonnet
```

## Usage

```python
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

```



## License
[MIT](https://choosealicense.com/licenses/mit/)