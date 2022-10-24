import base64
import re
import json
import os.path

# FILE = "sample.PNG"


class CheckFile:
    """ "
    The class has 2 function
        - generate a hex for the file
        - check the hex if it matches the file signature

    If the hex doesn't match the file signature it will return corrupt

    """

    def __init__(self):
        """only initialize the class"""
        pass

    def get_hex(self, file):
        """Get the hex value of the file"""
        with open(file, "rb") as f:
            hexdata = base64.b16encode(f.read(32)).decode("utf-8")
            fileType = os.path.splitext(file)

        return hexdata, fileType[1].lower()

    def check_data(self, hex, fileType):
        """check the hex value from the json if its corrupted"""
        f = open("hex.json")
        data = json.load(f)

        for types in data:
            for key, value in types.items():
                if key == fileType:
                    if re.search(f"{value}.+", hex):
                        hexCode = hex
                        if hexCode == hex:
                            return "notCorrupted"
                    else:
                        return "corrupted"

        f.close()
