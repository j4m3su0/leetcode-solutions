class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""

        for a, b in zip(word1, word2):
            merged_string += (a + b)

        merged_string += word1[len(word2):]
        merged_string += word2[len(word1):]

        return merged_string
        
