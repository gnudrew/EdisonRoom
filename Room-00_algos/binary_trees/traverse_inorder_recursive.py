from TreeNode import TreeNode

class Solution:
    def __init__(self):
        self.result = []

    def inorder(self,root):
        if root is None:
            return None

        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)

# Build a tree
root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(0)
root.left.left.right = TreeNode(-2)

s = Solution()
s.inorder(root)
print(s.result)
