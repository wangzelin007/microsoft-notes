# 二叉树的前序遍历
# Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:
# 1
#   2
# 3
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.recur(root)
        return self.ans

    def recur(self, root):
        if not root:
            return
        self.ans.append(root.val)
        self.recur(root.left)
        self.recur(root.right)

# 迭代
class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

# Morris 遍历 时间复杂度：O(n) 空间复杂度：O(1)
# 新建临时节点，令该节点为 root；
# 如果当前节点的左子节点为空，将当前节点加入答案，并遍历当前节点的右子节点；
# 如果当前节点的左子节点不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点：
# 如果前驱节点的右子节点为空，将前驱节点的右子节点设置为当前节点。然后将当前节点加入答案，并将前驱节点的右子节点更新为当前节点。当前节点更新为当前节点的左子节点。
# 如果前驱节点的右子节点为当前节点，将它的右子节点重新设为空。当前节点更新为当前节点的右子节点。
# 重复步骤 2 和步骤 3，直到遍历结束。
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        p1 = root  # 当前开始遍历的节点
        while p1:
            p2 = p1.left  # 记录当前节点的左子树
            if p2:
                while p2.right and p2.right != p1:  # 找到当前左子树的最右侧节点，且这个节点在指向根节点之前。
                    p2 = p2.right
                if not p2.right:  # 如果最右侧节点没有只想根节点，创建它与根节点的链接，然后往下一个左子树根节点移动。
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:  # 当左子树最右侧节点指向根节点，说明已经回到了根节点并重复了之前的操作，同时我们已经处理完了最右侧节点，还原现场。
                    p2.right = None
            else:
                res.append(p1.val)
            p1 = p1.right  # 一直往右走
        return res
