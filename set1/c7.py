import sys
import base64
from Crypto.Cipher import AES

if __name__ == "__main__":
    infile = open(sys.argv[1], "r")
    b64_ct = ""

    for line in infile:
        stripl = line.rstrip()
        b64_ct += stripl
    infile.close()
    ct = base64.b64decode(b64_ct)


    key = bytes(sys.argv[2], "utf-8")
    print(key)
    cip = AES.new(key, AES.MODE_ECB)
    pt = cip.decrypt(ct)
    pt = pt.decode("utf-8")
    

    ofile = open("result.txt", "w")
    print(pt, file=ofile)
    ofile.close()
