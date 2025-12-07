class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dp(i, j):
            if j == len(s):
                if s[i:j] in wordDict:
                    return True
                else:
                    return False
            
            if s[i:j] in wordDict:
                take = dp(j, j+1)
                skip = dp(i, j+1)
                return take or skip
            else:
                return dp(i, j+1)
        wordDict = set(wordDict)
        return dp(0, 1)
        
        
