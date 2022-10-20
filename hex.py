import binascii
import re

FILE = "sample.jpg"

expression = "(?P<id>\w+?)_INIT\s*?=.*?'h(?P<hexValue>[0-9a-fA-F]*)"
regex = re.compile(expression)


def get_hex(file):
    with open(file, "rb") as f:
        hexdata = binascii.hexlify(f.read(3))

        if hexdata != b"ffd8ff":
            print("corrupted image")
        else:
            print("not corrupted")
    # print(f" hexcode = {hexdata}")


def main():
    get_hex(FILE)


if __name__ == "__main__":
    main()
