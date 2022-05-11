class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        else:
            haystack = haystack.split(needle)
            if len(haystack) == 1:
                return -1
            else:
                return len(haystack[0])
