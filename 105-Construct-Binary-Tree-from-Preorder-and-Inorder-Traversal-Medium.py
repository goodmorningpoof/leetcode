# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterate through preorder list. For every root, find it in the inorder list (use hashmap for fast lookup otherwise
#  you have O(N^2) time complexity (noob). When you find the root in the inorder list, everything to the left will be in the left 
# subtree, everything to the right of that root value will be in a right subtree. Therefore recursively call the function
# to find the respective root for the left and right subtrees knowing the bounds.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # in order to not have to go through inorder to find the root every time, let's store the indexes
        # in a hashmap for fast lookup, otherwise our solution would be O(N^2)
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        current = 0
        def parse_inorder(left, right):
            # base case
            if left > right:
                return None

            nonlocal current 
            root = preorder[current]
            current += 1

            middle = mapping[root]

            node = TreeNode(root)
            node.left = parse_inorder(left, middle - 1)
            node.right = parse_inorder(middle + 1, right)

            return node
        
        return parse_inorder(0, len(inorder) - 1)
    
