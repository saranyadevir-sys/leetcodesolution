class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
            
        # Step 3: Read digits
        res = 0
        while index < len(s) and s[index].isdigit():
            # Convert char to int and add to result
            digit = int(s[index])
            res = (res * 10) + digit
            index += 1
            
        # Apply sign
        res *= sign
        
        # Step 4: Rounding (Clamping to 32-bit range)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
