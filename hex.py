import binascii
import base64
from multiprocessing.sharedctypes import Value
import re
import json
import os.path

FILE = "sample.PNG"


def get_hex(file):
    """Get the hex value of the file"""
    with open(file, "rb") as f:
        hexdata = base64.b16encode(f.read(32)).decode("utf-8")
        fileType = os.path.splitext(FILE)
        check_data(hexdata, fileType[1].lower())


def check_data(hex, fileType):
    """check the hex value from the json if its corrupted"""
    f = open("hex.json")
    data = json.load(f)

    for types in data:
        for key, value in types.items():
            if key == fileType:
                if re.search(f"{value}.+", hex):
                    hexCode = hex
                    if hexCode == hex:
                        print("not corrupted")
                else:
                    print("corrupt image")

    f.close()


def main():
    get_hex(FILE)


if __name__ == "__main__":
    main()
