class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setToStore = set(nums)
        result = 0

        for n in setToStore:
            if n - 1 not in setToStore:
                current_num = n
                length = 1
                while current_num + 1 in setToStore:
                    current_num += 1
                    length += 1
                result = max(result, length)
        return result