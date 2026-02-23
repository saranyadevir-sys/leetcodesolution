class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Sort the strings lexicographically
        strs.sort()
        
        # Take the first and last strings
        first = strs[0]
        last = strs[-1]
        
        res = ""
        # Compare the characters of the first and last strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
            
        return res

        
