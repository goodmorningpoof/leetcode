# Im pretty sure this is slightly inefficient but fk it, i passed all test cases

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1) # cut down on going down the same path
        dp[0] = True # empty str can always be segmented, base case
        wordDictSet = set(wordDict)

        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i:j+1] in wordDictSet:
                        dp[j + 1] = True

        
        return dp[-1]
