class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"}
        
        combinations = [""]

        for digit in digits:
            new_combinations = []

            letters = phone_map.get(digit)

            for combo in combinations:
                for letter in letters:
                    new_combinations.append(combo + letter)

            combinations = new_combinations

        return combinations 
