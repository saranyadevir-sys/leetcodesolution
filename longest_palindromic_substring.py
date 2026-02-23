class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Case 1: Odd length palindrome (center is s[i])
            len1 = self._expandAroundCenter(s, i, i)
            # Case 2: Even length palindrome (center is between s[i] and s[i+1])
            len2 = self._expandAroundCenter(s, i, i + 1)
            
            # Get the maximum length found at this center
            max_len = max(len1, len2)
            
            # Update the global start and end if a longer palindrome is found
            if max_len > (end - start):
                # Calculate new start/end based on max_len
                # Note: max_len - 1 handles both even and odd cases correctly
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]

    def _expandAroundCenter(self, s, left, right):
        # Expand as long as pointers are in bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the length of the palindrome found
        # (right - 1) - (left + 1) + 1 simplifies to right - left - 1
        return right - left - 1
