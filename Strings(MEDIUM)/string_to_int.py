class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Check if string is empty after removing spaces
        if i == n:
            return 0

        # Check sign
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        result = 0

        # Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        result *= sign

        # Clamp to 32-bit signed integer range
        INT_MIN = -(2**31)
        INT_MAX = (2**31) - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
