# @param n, an integer
# @return an integer
def reverseBits(n):
    rev = bin(n + (2 ** 32))[-32:]
    rev = rev[::-1]
    return int(rev, 2)