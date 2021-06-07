from TreeNode import TreeNode
from collections import deque
from traverse_levelorder_iterative import levelorder as f

from unittest import TestCase, main

class TestingTrav(TestCase):

    def test_case0(self):
        self.assertEqual(1,1)

    def test_case1(self):
        root = None
        self.assertEqual(f(root),[])

    def test_case2(self):
        root = TreeNode(0)
        self.assertEqual(f(root),[[0]])
        self.assertNotEqual(f(root),[0])

    def test_case3(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        self.assertEqual(f(root),[[10],[5,15]])

    def test_case4(self):
        root = TreeNode(0)
        self.assertEqual(f(root),[0])

if __name__ == '__main__':
    main()