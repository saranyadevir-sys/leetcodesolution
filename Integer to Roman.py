class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of values and symbols in descending order
        # Includes the special subtractive cases (900, 400, 90, 40, 9, 4)
        sym_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = ""
        
        for value, symbol in sym_map:
            # While the number is larger than the current Roman value
            while num >= value:
                res += symbol
                num -= value
                
        return res

        
