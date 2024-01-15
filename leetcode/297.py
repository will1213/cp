# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        s = ''
        q = deque([root])
        q2 = deque([])
        going = False
        while q:
            temp = q.popleft()
            if temp:
                s += f'{temp.val},'
                if temp.left or temp.right:
                    going |= True
                else:
                    going |= False
                q2.append(temp.left)
                q2.append(temp.right)                
            else:
                s += f'null,'   
            if not q and going:
                q = q2
                q2 = deque([])
                going = False
        return s
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        q = deque([])
        nodes = data.split(',')
        nodes.pop()
        ans = None
        if nodes[0] != 'null':
            ans = TreeNode(int(nodes[0]))
            q.append(ans)
            index = 1
            while q and index < len(nodes):
                node = q.popleft()
                if nodes[index] != 'null':
                    node.left = TreeNode(int(nodes[index]))
                    q.append(node.left)
                index += 1
                if nodes[index] != 'null':
                    node.right = TreeNode(int(nodes[index]))
                    q.append(node.right)
                index += 1
        return ans
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))