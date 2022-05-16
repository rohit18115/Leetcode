class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and flag == True and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            elif digits[i] == 9 and flag == True:
                digits[i] = 0
                flag = True
            elif flag == True:
                digits[i] = digits[i] + 1
                flag = False

        return digits
