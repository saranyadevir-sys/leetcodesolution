class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map to store the last seen index of each character
        char_map = {}
        max_length = 0
        left = 0
        
        for i, char in enumerate(s):
            # If character is a duplicate and within the current window
            if char in char_map and char_map[char] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_map[char] + 1
            
            # Update the last seen index of the character
            char_map[char] = i
            
            # Calculate and update the maximum length found so far
            current_window_size = i - left + 1
            if current_window_size > max_length:
                max_length = current_window_size
                
        return max_length
