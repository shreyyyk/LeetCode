class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashy=set(nums)
        for i in range(1,len(hashy)+2):
            if i in hashy:
                continue
            else:
                return i