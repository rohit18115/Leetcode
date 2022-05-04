class Solution:
    def isPalindrome(self, x):
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x > 0:
            temp = x
            rev_int_elements = []
            while temp > 0:
                digit = temp % 10
                rev_int_elements.append(digit)
                temp = temp // 10
            org_int_elements = rev_int_elements[::-1]
            return rev_int_elements == org_int_elements
        elif x == 0:
            return True
        else:
            return False
