def isPalindrome(x):
    n = str(x)
    xlen = len(n)
    for i in range(int(xlen / 2)):
        if n[i] != n[xlen - i - 1]:
            return False
    return True


value = isPalindrome(12345654321)
print(value)
