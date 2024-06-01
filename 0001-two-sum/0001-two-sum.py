class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for idx,value in enumerate(nums):
            rem=target-value
            if rem in visited:
                return [idx,visited[rem]]
            else:
                visited[value]=idx