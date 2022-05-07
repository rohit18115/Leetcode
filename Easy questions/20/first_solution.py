class Solution:
    def isValid(self, s: str) -> bool:
        s_list = []
        for i in s:
            if len(s_list) == 0:
                s_list.append(i)
            elif s_list[-1] == "{" and i == "}":
                s_list.pop()
            elif s_list[-1] == "[" and i == "]":
                s_list.pop()
            elif s_list[-1] == "(" and i == ")":
                s_list.pop()
            else:
                s_list.append(i)

        return len(s_list) == 0
