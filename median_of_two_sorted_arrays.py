class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Ensure A is the smaller array
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Middle of A
            j = half - i - 2  # Corresponding middle of B
            
            # Get the four boundary values (handle out of bounds)
            ALeft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i + 1] if (i + 1) < len(A) else float("infinity")
            BLeft = B[j] if j >= 0 else float("-infinity")
            BRight = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Check if partition is correct
            if ALeft <= BRight and BLeft <= ARight:
                # Odd total elements
                if total % 2:
                    return float(min(ARight, BRight))
                # Even total elements
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2.0
            
            elif ALeft > BRight:
                # A's partition is too big, move left
                r = i - 1
            else:
                # A's partition is too small, move right
                l = i + 1
