class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def search(idx: int, target: int) -> bool:
            # target reached → valid subset found
            if target == 0:
                return True
            
            # no numbers left or target overshot
            if idx < 0 or target < 0:
                return False
            
            # explore: include current element OR skip it
            include = search(idx - 1, target - nums[idx])
            exclude = search(idx - 1, target)
            return include or exclude

        total = sum(nums)

        # odd total means equal split impossible
        if total % 2 == 1:
            return False

        return search(len(nums) - 1, total // 2)
