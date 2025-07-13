class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s_list = list(s)

        for i in range(len(s)):
            if s_list[i].lower() in ["a", "e", "u", "i", "o"]:
                vowels.append(s_list[i])
                s_list[i] = "_"
        
        for i in range(len(s)):
            if s_list[i] == "_":
                s_list[i] = vowels.pop()

        return "".join(s_list)
        
