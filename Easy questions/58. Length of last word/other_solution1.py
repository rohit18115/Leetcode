def lengthOfLastWord(self, s):
    # (going backwards) find first non-space char
    for i in range(len(s) - 1, -2, -1):
        if i == -1 or s[i] != " ":
            break

    # keep going until a space or end of string
    for j in range(i, -2, -1):
        if j == -1 or s[j] == " ":
            return i - j
