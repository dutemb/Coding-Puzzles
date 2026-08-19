class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i],0)+1
            if hashMap.get(nums[i])>1:
                return True
        return False
        