from TreeNode import TreeNode

# STRATEGY:
# --> Use a preorder traversal
# --> Use another variable to keep track of the level
#   --> how about a hashmap.. <int>depth => [val1, val2, ...]

def levelorder(root):
    # recursive step
    levels = {} # <int> => []
    recurse(root,levels)

    # parse hashmap to expected output
    res = []
    for i in range(max(levels.keys())+1):
        res.append(levels[i])
    return res

def recurse(cur_node, levels, depth=0):
    # process current node
    if depth not in levels:
        levels[depth] = []
    levels[depth].append(cur_node.val)
    # process left child
    if cur_node.left:
        recurse(cur_node.left, levels, depth + 1)
    # process right child
    if cur_node.right:
        recurse(cur_node.right, levels, depth +1 )

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