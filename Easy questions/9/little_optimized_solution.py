def isPalindrome(x):
    n = str(x)
    xlen = len(n)
    return all(
        [True if n[i] == n[xlen - 1 - i] else False for i in range(int(xlen / 2))]
    )


value = isPalindrome(-121)
print(value)
