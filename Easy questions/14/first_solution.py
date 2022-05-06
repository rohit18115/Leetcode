def longestCommonPrefix(strs):
    str = ""
    count = 0
    el_len = [len(l) for l in strs]
    min_len = min(el_len)
    new_strs = [s[:min_len] for s in strs]
    print(new_strs)
    ref = new_strs[0]
    for i in range(len(ref)):
        for j in new_strs:
            if ref[i] == j[i]:
                count += 1
            else:
                return str
        if count == len(new_strs):
            str += ref[i]
            count = 0
    return str


print(longestCommonPrefix(["car", "carpet", "cargo"]))
