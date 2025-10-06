class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        post=[1]
        p = 1
        for i in range(1,len(nums)) :
            p = p*nums[i-1]
            pre.append(p)
            #post.append(p)
        print(pre)
        p=1
        for i in range(len(nums)-1,0,-1) :
            p = p*nums[i]
            post.append(p)
        #print(post)
        post.reverse()
        #print(post)
        for i in range(len(post)):
            pre[i] = pre[i]*post[i]
        return pre

             
