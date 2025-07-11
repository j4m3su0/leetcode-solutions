class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        current_prefix = strs[0]  

        for i in range(1, len(strs)):
            for j in range(0, min(len(current_prefix), len(strs[i]))):
                if current_prefix[j] != strs[i][j]:
                    current_prefix = strs[i][:j]
                    break
                else:
                    if j + 1 == min(len(current_prefix), len(strs[i])) and len(current_prefix) > len(strs[i]):
                        current_prefix = strs[i]
        
        return current_prefix                
