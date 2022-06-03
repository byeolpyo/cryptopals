from binascii import unhexlify, hexlify
import sys

if __name__ == "__main__":
    infile = open(sys.argv[1], "r")
    pt = bytes(infile.read(), "utf-8")
    key = sys.argv[2]
    key = key * (1 + len(pt)//len(key))
    key = key.encode()
    ct = bytes(a ^ b for a, b in zip(pt, key))
    print(ct.hex())
