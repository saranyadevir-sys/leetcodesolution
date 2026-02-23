class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit signed integer boundaries
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        # Determine sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x != 0:
            # Get the last digit
            pop = x % 10
            # Remove the last digit from x
            x //= 10
            
            # Check for overflow before updating res
            # If current res is already greater than (MAX_INT / 10), 
            # multiplying by 10 will definitely overflow.
            if res > MAX_INT // 10:
                return 0
            
            res = (res * 10) + pop
        
        # Apply the original sign
        res *= sign
        
        # Final check to ensure it's within range (for negative edge cases)
        if res < MIN_INT or res > MAX_INT:
            return 0
            
        return res
