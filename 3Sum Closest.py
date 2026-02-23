class Solution(object):
    def threeSumClosest(self, nums, target):
        # Sort the array to use the two-pointer technique
        nums.sort()
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find the exact target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the sum comparison to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
