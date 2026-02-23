class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Edge cases: 
        # 1. Negative numbers are not palindromes.
        # 2. Numbers ending in 0 are not palindromes (unless the number is 0).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            # Extract last digit and add to reversed_half
            reversed_half = (reversed_half * 10) + (x % 10)
            # Remove last digit from x
            x //= 10
            
        # For even length: x == reversed_half (e.g., 12 | 12)
        # For odd length: x == reversed_half // 10 (e.g., 1 | 12 -> 1 == 1)
        return x == reversed_half or x == reversed_half // 10

        
