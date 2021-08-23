import collections


class Solution:
    # 和554很相近
    def orangesRotting(self, grid) -> int:
        if not grid:
            return -1
        n, m = len(grid), len(grid[0])
        zero_list = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2]
        q = collections.deque(zero_list)
        seen = set(zero_list)
        level = 0
        while q:
            size = len(q)
            while size:
                r, l = q.popleft()
                for nr, nl in [(r - 1, l), (r + 1, l), (r, l - 1), (r, l + 1)]:
                    if 0 <= nr < n and 0 <= nl < m and (nr, nl) not in seen:
                        seen.add((nr, nl))
                        if grid[nr][nl] == 1:
                            q.append((nr, nl))
                            grid[nr][nl] = 2
                size -= 1
            if q:
                level += 1
        if any(1 in row for row in grid):
            return -1
        return level


mat = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
mat = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
solution = Solution()
orangesRotting = solution.orangesRotting(mat)
print(orangesRotting)
