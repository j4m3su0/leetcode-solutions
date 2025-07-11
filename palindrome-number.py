class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0
        
        res, sign, i = 0, 1, 0

        if s[0] == "-" or s[0] == "+":
            sign *= (int(s[0] + str(sign)))
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            if sign * res > 2**31 - 1:
                res = 2**31 - 1
            elif sign * res < -2**31:
                res = 2**31
            
            i += 1
        
        return sign * res
