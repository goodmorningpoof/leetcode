# link: https://leetcode.com/problems/binary-tree-right-side-view/

# Go level by level, take right-most node and add to res array, pretty simple me thinks
# idk why you would need a video for this problem, but if you do: https://www.youtube.com/watch?v=7FXEPyvIN3Y
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # base case check
        if not root:
            return []

        queue = collections.deque([root])
        res = []
        while queue:
            level_len = len(queue)

            for i in range(level_len):
                node = queue.popleft()
                
                if i == level_len - 1: #right mode node
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
        return res
        
        
