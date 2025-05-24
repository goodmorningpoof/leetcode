# https://leetcode.com/problems/word-break/

# i tried to comment my code, but if youre still lost, theres a video i made for this a bit ago:
# https://youtu.be/owCi6ZUWCTA?si=xKrdFtS77BRe18Z7

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1) 
        dp[0] = True # empty str can always be segmented
        wordDictSet = set(wordDict) # fast lookup, O(1)
        maxWordLen = max(len(word) for word in wordDict) if wordDict else 0
        
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, min(i + maxWordLen, len(s))): # substring shouldn't exceed max word length in wordDict
                    if s[i:j+1] in wordDictSet:
                        dp[j + 1] = True

        
        return dp[len(s)]
