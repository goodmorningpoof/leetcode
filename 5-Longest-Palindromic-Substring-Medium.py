# very obvious a brute force is not feasible because you have to scan through the original string and to scan each substring you have another linear scan again and again, so overall you have crazy exponential time complexity, 
#so something more clever is needed

# To check if a string like "aba" is a palindrome, we can either:
# 1. start from the outside and compare the two characters OR
# 2. start in the middle and expand outwards and do the comparison that way

# Which is better? option 2. This way we can do a linear scan through the original string and do the comparison at each character and expand outwards. This will be O(N^2) but the brute force is significantly more inefficient so this is best.
# For ex: for 'babdf', we start at 'b' and check to the left and right, of course there is nothing to the left so b itself is the longest palindrome so far. We move onto the character 'a', we expand outwards and we see 'bab' is 
#the longest palindrome so far
# We keep doing this as we linearly scan through the string and we will find the longest palindrome. That being said, we have to handle the edge case of where we have an even length of characters for a palindrome like 'abba', 
# the way to handle this is set the pointers next to each other not at the same starting position


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest_len = 0

        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i # pointers at center position right now
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_len:
                    start = l
                    longest_len = r - l + 1
                r += 1
                l -= 1
            
            # even length palindromes
            l, r = i, i + 1
    
            # this is the same code as above, so you honestly could probably put it in a function
            # in an interview you might want to do that obviously but yeah
            # only difference is where we set the pointers for odd and even palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_len:
                    start = l
                    longest_len = r - l + 1
                r += 1
                l -= 1

        # string splicing creates a copy, we dont want to be doing that to store the palindrome every time we find a new longest palindrome so do the string splicing down here rather than above, just a little bit more efficient
        return s[start:start + longest_len] 
