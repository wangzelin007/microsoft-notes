# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
# 如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

# [["a","b","c","e"],
#  ["s","f","c","s"],
#  ["a","d","e","e"]]
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
#
# 示例 2：
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

# DFS 解析：
# 递归参数： 当前元素在矩阵 board 中的行列索引 i 和 j ，当前目标字符在 word 中的索引 k 。
# 终止条件：
# 返回 false ： (1) 行或列索引越界 或 (2) 当前矩阵元素与目标字符不同 或 (3) 当前矩阵元素已访问过 （ (3) 可合并至 (2) ） 。
# 返回 true ： k = len(word) - 1 ，即字符串 word 已全部匹配。
# 递推工作：
# 标记当前矩阵元素： 将 board[i][j] 修改为 空字符 '' ，代表此元素已访问过，防止之后搜索时重复访问。
# 搜索下一单元格： 朝当前元素的 上、下、左、右 四个方向开启下层递归，使用 或 连接 （代表只需找到一条可行路径就直接返回，不再做后续 DFS ），并记录结果至 res 。
# 还原当前矩阵元素： 将 board[i][j] 元素还原至初始值，即 word[k] 。
# 返回值： 返回布尔量 res ，代表是否搜索到目标字符串。
# 时间复杂度 O(3^K MN)： 最差情况下，需要遍历矩阵中长度为 KK 字符串的所有方案，时间复杂度为 O(3^K)；矩阵中共有 M*N 个起点，时间复杂度为 O(MN)。
# 方案数计算： 设字符串长度为 K ，搜索中每个字符有上、下、左、右四个方向可以选择，舍弃回头（上个字符）的方向，剩下 3 种选择，因此方案数的复杂度为 O(3^K)。
# 空间复杂度 O(K)： 搜索过程中的递归深度不超过 K ，因此系统因函数调用累计使用的栈空间占用 O(K) (因为函数返回后，系统调用的栈空间会释放）。
# 最坏情况下 K = MN，递归深度为 MN ，此时系统栈使用 O(MN)的额外空间。
# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i,j,k):
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!=word[k]: return False
            if k == len(word)-1: return True
            board[i][j] = ''
            res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            board[i][j] = word[k]
            return res

        for i in range(board):
            for j in range(board[0]):
                if dfs(i,j,0): return True
        return False