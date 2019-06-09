#给定一个二叉树，检查它是否是镜像对称的。
#
#例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
#但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#    1
#   / \
#  2   2
#   \   \
#   3    3
#说明:
#
#如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False

            if p.val != q.val:
                return False
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        return isSameTree(root, root)
