from TreeNode import TreeNode

# STRATEGY:
# --> process parent node before children.
# --> process left child before right child.
# ALGORITHM:
# 1. add root node to a stack, s.
# 2. while s is not empty, pop the top element from it and add its value to the result array, res.
# 3. push the popped node's children to s, first right, then left. That way, the left gets poppped first from the stack.

class Solution:
    def preorder(self,root):
        if root is None:
            return None
        
        s = [root] #stack of nodes
        res = [] #traversal values
        while s:
            cur_node = s.pop()
            res.append(cur_node.val)
            if cur_node.right:
                s.append(cur_node.right)
            if cur_node.left: #LIFO
                s.append(cur_node.left)
        return res

# build a sample tree
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1.5)
root.right = TreeNode(3)

print(Solution().preorder(root))