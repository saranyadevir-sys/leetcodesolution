class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            # Check if result is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: If pattern is finished
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' logic
            if j + 1 < len(p) and p[j+1] == '*':
                # Case 1: Use '*' as 0 occurrences
                # Case 2: Use '*' as 1+ occurrences (if first_match is true)
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # No '*', move normally
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)

