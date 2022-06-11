import sys

if __name__ == "__main__":
    inp = bytes(sys.argv[1], "utf-8")
    padlength = int(sys.argv[2])-len(inp)
    res = inp + bytes(padlength*[padlength])
    print(res)
