class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for num in nums:
            if dict_.get(num) == True:
                return True
            dict_[num] = True
        return False