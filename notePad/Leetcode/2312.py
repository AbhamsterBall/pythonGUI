import math
from typing import List


class Solution1:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        pr = {(h, w): p for h, w, p in prices}
        f = [[0] * (n + 1) for _ in range(m + 1)]
        print(f)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print(f)
                f[i][j] = max(pr.get((i, j), 0),
                              max((f[i][k] + f[i][j - k] for k in range(1, j)), default=0),  # 垂直切割
                              max((f[k][j] + f[i - k][j] for k in range(1, i)), default=0))  # 水平切割
        print(f[0][0])
        return f[m][n]


print(Solution1().sellingWood(m=3, n=5, prices=[[1, 4, 2], [2, 2, 7], [2, 1, 3]]))

print("————————————————————————————————————————————————————")

# 记忆化搜索：使用备忘录避免重复计算来跳过重叠子问题的计算方式
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        pr = {(x - 1, y - 1): p for x, y, p in prices}
        print(pr)
        f = [[0] * n for _ in range(m)]
        for i in range(m):  # 从小到大计算出最大解，录入f数组（备忘录）
            for j in range(n):
                f[i][j] = max(pr.get((i, j), 0), max((f[k][j] + f[i - 1 - k][j] for k in range(math.ceil((i - 1) / 2) + 1)), default=0),
                              max((f[i][q] + f[i][j - 1 - q] for q in range(math.ceil((j - 1) / 2) + 1)), default=0))
        return f[m - 1][n - 1]

print(Solution().sellingWood(m=3, n=5, prices=[[1, 4, 2], [2, 2, 7], [2, 1, 3]]))
print(Solution().sellingWood(m=4, n=6, prices=[[3,2,10],[1,4,2],[4,1,3]]))
