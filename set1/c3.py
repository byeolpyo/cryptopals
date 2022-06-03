import sys

from binascii import unhexlify, hexlify
if __name__ == "__main__":
    ct = unhexlify(sys.argv[1])
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
    print(bestmatch.decode("utf-8"))
