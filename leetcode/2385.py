# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        graph[root.val] = set()
        def helper(node):
            if node:
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val].add(node.val)
                    helper(node.left)
                if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val].add(node.val)
                    helper(node.right)
            return
        helper(root)
        ans = 0

        if graph[start]:
            iteration = [start]
            while iteration:
                temp = []
                for i in iteration:
                    stack = list(graph[i])
                    while stack:
                        last = stack.pop()
                        graph[last].remove(i)
                        if not graph[last]:
                            del graph[last]
                        else:
                            temp.append(last)
                ans += 1
                iteration = temp

        return ans