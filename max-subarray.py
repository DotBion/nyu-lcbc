class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lo_max = nums[0]
        gl_max = nums[0]
        
        for i in range(1, len(nums)):
            lo_max = max(nums[i], nums[i] + lo_max) 
            gl_max = max(lo_max, gl_max)
        return gl_max
            
            
