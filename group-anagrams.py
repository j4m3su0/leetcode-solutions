class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = dict()

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in hash_table.keys():
                hash_table.get(sorted_string).append(string)
            else:
                hash_table.update({sorted_string : [string]})
        
        return [group for group in hash_table.values()]
        
