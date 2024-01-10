# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = 0
        def helper(node):
            if node:
                if node.val > high:
                    helper(node.left)
                    return
                elif node.val < low:
                    helper(node.right)
                    return
                else:
                    nonlocal ans
                    ans += node.val
                    helper(node.left)
                    helper(node.right)
            return
        helper(root)
        return ans