class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in n_dict:
                return [n_dict[complement], index]
            n_dict[num] = index
        
        return []