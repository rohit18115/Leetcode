def lengthOfLastWord(self, s):
    cnt = 0
    for v in reversed(s):
        if v.isspace():
            if cnt:
                break
        else:
            cnt += 1
    return cnt
