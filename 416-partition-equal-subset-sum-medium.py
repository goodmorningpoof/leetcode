# 1-d dp problem
# link: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 1 partition = half of total sum
        # If half of total sum / 2 is odd number, then you can't have equal partitions
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        # dp[i] = True if we can form sum i using some subset of nums
        dp = [False] * (target + 1)
        dp[0] = True # base case: sum of 0 is always possible with no elements
        
        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        

        return dp[target]
