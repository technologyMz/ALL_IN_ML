class Solution:

    def updateMatrix_BFS(self, mat):
        if not mat:
            return mat

        for sr in range(len(mat)):
            for sl in range(len(mat[0])):
                



mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
solution = Solution()
merged_tree = solution.updateMatrix(mat)
print(merged_tree)
