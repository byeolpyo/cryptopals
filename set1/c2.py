import sys
from binascii import unhexlify

if __name__ == "__main__":
    a = unhexlify(sys.argv[1])
    b = unhexlify(sys.argv[2])
    res = bytes(aa ^ bb for (aa, bb) in zip(a, b))

    print(res)
