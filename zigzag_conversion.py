class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: If only one row or string is too short, no zigzag is possible
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows: a list of empty strings for each row
        rows = ["" for _ in range(numRows)]
        
        current_row = 0
        step = 1  # 1 means moving down, -1 means moving up
        
        for char in s:
            rows[current_row] += char
            
            # If we reach the top row, we must move down (step = 1)
            if current_row == 0:
                step = 1
            # If we reach the bottom row, we must move up (step = -1)
            elif current_row == numRows - 1:
                step = -1
            
            # Update the current row based on direction
            current_row += step
            
        # Join all row strings together
        return "".join(rows)
