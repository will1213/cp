# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node, high, low):
            if node:
                nonlocal ans
                if node.val > high:
                    ans = max(ans, node.val - low)
                    high = node.val
                if node.val < low:
                    ans = max(ans, high - node.val)
                    low = node.val
                helper(node.left, high, low)
                helper(node.right, high, low)
            return
        helper(root, root.val, root.val)
        return ans
        