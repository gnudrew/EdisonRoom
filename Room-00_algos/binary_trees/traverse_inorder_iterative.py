from TreeNode import TreeNode

class Solution:
    def inorder(self,root):
        if root is None:
            return None

        s = [] #stack of nodes
        res = [] #traversal values
        cur_node = root

        while s or cur_node:
            goRight = not cur_node #True if cur_node is None
            if goRight is True:
                cur_node = s.pop()
                res.append(cur_node.val)
                cur_node = cur_node.right
            else: #go left
                s.append(cur_node)
                cur_node = cur_node.left                
            
        return res

# build a sample tree
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1.5)
root.right = TreeNode(3)

print(Solution().inorder(root))