# _*_ coding: utf-8 _*_
# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
# 示例 1:
# 输入:
# [
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 设 f(i, j)f(i,j) 为从棋盘左上角走至单元格 (i ,j)(i,j) 的礼物最大累计价值，
# 易得到以下递推关系：f(i,j) 等于 f(i,j-1) 和 f(i-1,j) 中的较大值加上当前单元格礼物价值 grid(i,j)。
# f(i,j)=max[f(i,j−1),f(i−1,j)]+grid(i,j)
# 特殊情况f(0,0) f(0,j) f(i,0)
class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) # m*n
        # 特殊处理 f(0,0) f(0,j) f(i,0)
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
