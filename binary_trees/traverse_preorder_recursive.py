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

#built a simple tree
root = TreeNode(val=0)
root.left = TreeNode(val=1)
root.right = TreeNode(val=2)
root.left.left = TreeNode(val=4)
root.left.right = TreeNode(val=5)

s = Solution()
print(s.preorder(root))
