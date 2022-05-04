def hammingWeight(n, count=0):
    print(bin(n))
    return hammingWeight(n & n - 1, count + 1) if n != 0 else count


print(hammingWeight(0b1101))
