class Solution:
    def jump(self, nums: List[int]) -> int:
        i,j=0,0
        jump=0
        while j < len(nums)-1:
            far=0
            for i in range(i,j+1):
                if i+nums[i]>far:
                    far=i+nums[i]
            i=j+1
            j=far
            jump=jump+1

        return jump