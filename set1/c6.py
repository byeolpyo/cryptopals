import sys
import base64
from binascii import b2a_base64, unhexlify
from collections import Counter

# brute force solutions and pick the best one based on how character frequency in the english language
def unxor(ct):
    freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.095, 6, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074, 20]
    letters = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    letters = list(map(ord, letters))
    maxscore = 0
    bestmatch = ''
    for i in range(0, 0xff):
        pt = bytes(a ^ i for a in ct)
        score = 0
        for ch in pt:
            if ch in letters:
                score += freq[letters.index(ch)%2]
        if score > maxscore:
            maxscore = score
            bestmatch = pt
    return (bestmatch, maxscore)

def second(a):
    return a[1]

def hammingdist(a, b):
    res = 0;
    for i in range(min(len(a), len(b))):
        res += bin(a[i] ^ b[i]).count("1");
    return res


if __name__ == "__main__":

    infile = open(sys.argv[1], "r")
    
    b64_ciphertext = ""
    
    for line in infile:
        stripl = line.rstrip()
        b64_ciphertext += stripl
    infile.close()

    hex_ciphertext = base64.b64decode(b64_ciphertext)

    #create a list of hamming ratios with keylengths
    values = []
    for i in range(2, 40):
        temp = []
        chunks = []
        distances = 0
        for x in range(0,len(hex_ciphertext)-i,i):
            chunks.append(hex_ciphertext[x:x+i])
        for x in range(len(chunks)-1):
            distances += hammingdist(chunks[x], chunks[x+1])/i
        normalized = distances/len(chunks)
        temp.append(normalized)
        temp.append(i)
        values.append(temp)



    #sort best guesses
    values.sort()
    keylength = values[0][1]

    #solve each chunk individually, then unscramble back to plaintext
    chunks = []
    for i in range(keylength):
        chunks.append(hex_ciphertext[i::keylength])
    scrambled_pt = []
    for chunk in chunks:
        res = unxor(bytes(chunk))
        scrambled_pt.append(res[0])
    output = '' 
    for x in range(len(scrambled_pt[0])):
        for i in range(keylength):
            try:
                print(chr(scrambled_pt[i][x]), end = '')
            except:
                break
