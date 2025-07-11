class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        res = 0
        s = s[::-1]

        for i in range(len(s)):
            res += num_dict.get(s[i])

            if i > 0:
                if (
                        s[i] == "I" and s[i-1] in ["V", "X"]
                        or (s[i] == "X" and s[i-1] in ["L", "C"])
                        or (s[i] == "C" and s[i-1] in ["D", "M"])
                    ):
                    res -= 2 * num_dict.get(s[i])
        
        return res
