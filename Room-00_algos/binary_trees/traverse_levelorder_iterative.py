from TreeNode import TreeNode
from collections import deque

# STRATEGY:
# --> Start at root, adding it to a queue, q.
# --> Process all elements in q, keeping track with size of this level, s.
#   --> add current node's value to list, ans.
#   --> add left, then right children to the q.

def levelorder(root):
    if root is None:
        return []
    #define data structures
    res = []
    cur_level = []
    q = deque() #push=append(); pop=popleft()
    q.append(root)

    #do the looping
    while q:
        size = len(q)
        i = 0
        while i < size:
            cur_node = q.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            i += 1
        res.append(cur_level)
        cur_level = []

    return res

# build a simple tree
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1.5)
root.left.right.left = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(2)
root.right.left = TreeNode(18)

print(levelorder(root))