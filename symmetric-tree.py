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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:                                 # 先判断根节点是否为空
            return True
        return self.isMirror(root.left, root.right)  # 分成左子树和右子树判断

    def isMirror(self, p, q):                        # 判断两棵树是否是镜像树
        if not p and not q:                          # 根节点都为空，是
            return True
        if not p or not q:                           # 其中有一棵为空，不是
            return False
        l = self.isMirror(p.left, q.right)           # p的左子树和q的右子树是否相同
        r = self.isMirror(p.right, q.left)           # p的右子树和q的左子树是否相同
        return p.val == q.val and l and r            # 值相等，并且p的左=q的右，p的右=q的左
