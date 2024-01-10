# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(node, arr):
            if node:
                if node.left and node.right:
                    helper(node.left, arr)
                    helper(node.right, arr)
                elif node.left or node.right:
                    helper(node.left or node.right, arr)
                else:
                    arr.append(node.val)
            return
        ans = []
        helper(root1, ans)
        ans2 = []
        helper(root2, ans2)
        return ans == ans2