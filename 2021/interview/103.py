# 二叉树锯齿形层序遍历
# Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
# Example 1:
#     3
#  9     20
#      15  7
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:
# Input: root = []
# Output: []
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        count = -1
        if not root:
            return res
        stack = [(root, 0)]
        while stack:
            i = stack.pop(0)
            if i[0] != None:
                if i[1] != count:
                    res.append([])
                    count = i[1]
                res[i[1]].append(i[0].val)
                stack.append((i[0].left, i[1]+1))
                stack.append((i[0].right, i[1]+1))
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        return res

    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])
        f = True
        ans = []
        while q:
            tmp = collections.deque([])
            for _ in range(len(q)):
                n = q.popleft()
                if f:
                    tmp.append(n.val)
                else:
                    tmp.appendleft(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            f = not f
            ans.append(list(tmp))
        return ans

    def zigzagLevelOrder3(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return list(map(list, self.ans))

    def dfs(self, root, level):
        if not root: return
        if len(self.ans) == level: self.ans.append(collections.deque())
        if level % 2 == 0:
            self.ans[level].append(root.val)
        else:
            self.ans[level].appendleft(root.val)
        if root.left: self.dfs(root.left, level + 1)
        if root.right: self.dfs(root.right, level + 1)