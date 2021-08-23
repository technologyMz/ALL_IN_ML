class Solution:
    def floodFill_BFS(self, image, sr: int, sc: int, newColor: int):   #不用队列，用数组，分别存放当前点和扩展出的点
        def check_point(x,y, image):
            if 0 <=x < len(image) and 0 <= y < len(image[0]) and x :
                return True
            return False

        oldColor = image[sr][sc]
        pixel_list = []
        open_list = [[sr,sc]]
        while len(open_list) != 0:
            for one_pixel in open_list:
                print(open_list)
                if image[one_pixel[0]][one_pixel[1]] == oldColor:
                    pixel_list.append(one_pixel)
                    image[one_pixel[0]][one_pixel[1]] = newColor
                    open_list.remove(one_pixel)
                    add_list = [[one_pixel[0] - 1,  one_pixel[1]],
                                [one_pixel[0] + 1, one_pixel[1]],
                                [one_pixel[0], one_pixel[1] - 1],
                                [one_pixel[0], one_pixel[1] + 1]]
                    for point in add_list:
                        if check_point(point[0], point[1], image):
                            # print(point)
                            if image[point[0]][point[1]] == oldColor and point not in pixel_list and point not in open_list:
                                open_list.append(point)
                                # print(point)
        return image

    def floodFill_BFS2(self, image, sr: int, sc: int, newColor: int): # 用队列
        import collections
        oldColor = image[sr][sc]
        if oldColor == newColor:  #需要考虑初始点颜色和newcolor相同的情况
            return image
        due = collections.deque([[sr, sc]])
        image[sr][sc] = newColor
        while due:
            x, y = due.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                print(mx,my)
                if 0 <= mx < len(image) and 0 <= my < len(image[0]):
                    print(image[mx][my])
                    if image[mx][my] == oldColor:
                        image[mx][my] = newColor
                        due.append([mx,my])
        return image

    def floodFill_DFS(self, image, sr: int, sc: int, newColor: int): # 用队列
        import collections
        oldColor = image[sr][sc]
        if oldColor == newColor:  #需要考虑初始点颜色和newcolor相同的情况
            return image
        due = collections.deque([[sr, sc]])
        while due:
            x, y = due[-1]
            if image[x][y] == oldColor:
                image[x][y] =newColor
            num_add = 0
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                print(mx,my)
                if 0 <= mx < len(image) and 0 <= my < len(image[0]) and [mx,my] not in due and image[mx][my] == oldColor:
                    due.append([mx,my])
                    num_add =1
                    break
            if num_add == 0:
                due.pop()
                # image[x][y] = newColor

        return image

    def floodFill_DFS2(self, image, sr: int, sc: int, newColor: int): # 用递归
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                        dfs(mx, my)

        if currColor != newColor:
            dfs(sr, sc)
        return image




image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
solution = Solution()
# print(solution.floodFill(image,sr,sc,newColor))
print(solution.floodFill_DFS(image,sr,sc,newColor))