# link: https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # empty subset is a subset ig lol
        ans = []

        def bt(i, arr):
            
            # base case to break our recursion
            if i == len(nums):
                ans.append(arr.copy())
                return
            
            # take
            arr.append(nums[i])
            bt(i + 1, arr)
            
            # don't take (backtrack)
            arr.pop()
            bt(i + 1, arr)

        bt(0, [])
        print(ans)
        return ans

# subsets build out like this:
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]


    
        
