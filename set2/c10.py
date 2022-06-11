import sys
from Crypto.Cipher import AES

def xor_bytes(a, b):
    return bytes(aa ^ bb for (aa, bb) in zip(a, b))

def pad_block(inp, leng):
    if len(inp) % 16 == 0:
        return inp
    padlength = leng-(len(inp)%16)
    res = inp + bytes(padlength*[padlength])
    return res
    

if __name__ == "__main__":
    infile = open(sys.argv[1], "r")
    ct = ""
    for line in infile:
        stripl = line.rstrip()
        ct += stripl
    infile.close()

    infile = open(sys.argv[3], "r")
    IV = ""
    for line in infile:
        stripl = line.rstrip()
        IV += stripl
    infile.close()


    ct = bytes(ct, "utf-8")
    IV = bytes(IV[:16], "utf-8")
    key = bytes(sys.argv[2], "utf-8")
    cip = AES.new(key, AES.MODE_ECB)


    ct = pad_block(ct, 16)
    key = pad_block(key, 16)
    IV = pad_block(IV, 16)

    blocks = [bytes(ct[i:i+16]) for i in range(0, len(ct), 16)]
    blocks = [IV] + blocks

    res = b''
    for i in range(1, len(blocks)):
        bl_xor = xor_bytes(blocks[i-1], blocks[i])
        res += cip.encrypt(bl_xor)
    print(res)
