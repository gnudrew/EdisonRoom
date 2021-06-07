from TreeNode import TreeNode

# ALGORITHM:
# Simple but non-intuitive trick here.
# --> Take the approach from preorder.
# --> Reverse order children added to stack.
# --> Reverse the list at the end.
# PRESTO!

class Solution:
    def postorder(self,root):
        if root is None:
            return None
        s = [root] #stack of nodes
        res = [] #traversal values
        while s:
            cur_node = s.pop()
            res.append(cur_node.val)
            if cur_node.left:
                s.append(cur_node.left)
            if cur_node.right:
                s.append(cur_node.right)
        return list(reversed(res))

# build a sample tree
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1.5)
root.right = TreeNode(3)

print(Solution().postorder(root))