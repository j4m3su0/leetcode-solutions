class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hash_table.keys():
                return [i, hash_table.get(complement)]
            else:
                hash_table.update({nums[i] : i})
        
        return []
