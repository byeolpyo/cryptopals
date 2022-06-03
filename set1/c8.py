import sys
from collections import Counter

if __name__ == "__main__":
    ifile = open(sys.argv[1], "r")
    line_num = 1
    for line in ifile:
        ct = []
        for i in range(0,len(line)-8,8):
            ct.append(line[i:i+8])
        cnt = Counter(ct)
        k = cnt.most_common()
        if k[0][1] != 1:
            print(f'Found potential ECB encrypted text:')
            print(line)
        line_num += 1
    ifile.close()
