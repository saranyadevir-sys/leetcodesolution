class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        # Map digits to letters as seen on a telephone keypad
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            # If the combination is done
            if len(path) == len(digits):
                result.append("".join(path))
                return
            
            # Get letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before trying the next one
                path.pop()
        
        backtrack(0, [])
        return result
Letter Combinations of a Phone Number
