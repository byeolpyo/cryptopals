#cryptopals set 1 challenge 1 solver
#fun fact - this is the first and last one that throws an exception given an invalid argument
import sys
from binascii import unhexlify, b2a_base64

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
        quit()
    text = sys.argv[1]
    res = b2a_base64(unhexlify(text))
    print(res)
