https://leetcode.com/problems/sort-colors/

# Dutch National Flag Problem (One pass approach)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        # keep 0s on left, 2s on the right and 1s in the middle, swap when necessary
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1 # dont want to increment i below in this case, we dont want i to move because maybe we moved 0 instead of a 1 to the middle, consider this [0,1,2,0]
            i += 1  
     
            
        
