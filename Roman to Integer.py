class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        # Iterate up to the second to last character
        for i in range(len(s) - 1):
            curr_val = roman_map[s[i]]
            next_val = roman_map[s[i+1]]
            
            # Subtraction rule: if smaller value precedes larger value
            if curr_val < next_val:
                total -= curr_val
            else:
                total += curr_val
        
        # Always add the value of the last character
        total += roman_map[s[-1]]
        
        return total

        
