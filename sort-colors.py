class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red = 0
        # white = 0
        # blue = 0

        # for i in nums :
        #     if i == 0 :
        #         red+=1
        #     elif i==1 :
        #         white+=1
        #     elif i==2 :
        #         blue+=1

        # #rewrite the nums array
        # for i in range(red) :
        #     nums[i] = 0
        # for i in range(red, red+white) :
        #     nums[i] = 1
        # for i in range(red+white, red+white+blue) :
        #     nums[i] = 2

        #[2,0,2,1,1,0]

        p0 = 0
        p1 = 0
        p2 = len(nums) - 1 

        while p1<=p2 :
            if nums[p1] == 0 :
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p1+=1
                p0+=1
            elif nums[p1] == 2 :
                nums[p2], nums[p1] = nums[p1], nums[p2]
                #p1+=1
                p2-=1
            elif nums[p1] == 1 :
                p1+=1
        return nums
