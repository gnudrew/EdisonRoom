from TreeNode import TreeNode

class Solution:
    def preorder(self, root):
        if root is None:
            return None

        self.result = []
        self.helper(root)
        return self.result

    def helper(self,n):
        if n:
            self.result.append(n.val)
            self.helper(n.left)
            self.helper(n.right)

#Build a simple tree
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#Do a preorder traversal
s = Solution()
print(s.preorder(root))
