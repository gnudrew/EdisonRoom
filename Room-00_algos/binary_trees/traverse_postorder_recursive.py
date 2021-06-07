from TreeNode import TreeNode

class Solution:
    def postorder(self,root):
        result = []
        self.recurse(root,result)
        return result #list of node values

    def recurse(self,node,result):
        if node is None:
            return None
        self.recurse(node.left,result)
        self.recurse(node.right,result)
        result.append(node.val)
        print(result)

# Build a tree
root = TreeNode(0)
root.left = TreeNode(-1)
root.left.right = TreeNode(1)

# Traverse the tree in postorder
s = Solution()
ans = s.postorder(root)
print(ans)