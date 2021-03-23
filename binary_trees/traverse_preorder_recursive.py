from TreeNode import TreeNode

class Solution:
    def preorder(self, root):
        if root is None:
            return None

        result = []
        self.helper(root,result)
        return result

    def helper(self,n,result):
        if n:
            result.append(n.val)
            self.helper(n.left,result)
            self.helper(n.right,result)

#Build a simple tree
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#Do a preorder traversal
s = Solution()
print(s.preorder(root))
