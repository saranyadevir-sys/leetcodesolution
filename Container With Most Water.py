class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate width
            width = right - left
            
            # Calculate height (the limiting factor)
            h = min(height[left], height[right])
            
            # Update the maximum area found so far
            current_area = width * h
            if current_area > max_area:
                max_area = current_area
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
