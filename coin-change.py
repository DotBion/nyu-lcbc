class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amount):
            if amount == 0:
                return 0
            return  min([float('inf')]+[dp(amount-coin)+1 for coin in coins if coin<=amount])
        ans = dp(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans
                
        
