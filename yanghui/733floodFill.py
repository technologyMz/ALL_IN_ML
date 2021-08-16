class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
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

    def floodFill_2(self, image, sr: int, sc: int, newColor: int): # 用队列
        import collections
        oldColor = image[sr][sc]
        due = collections.deque([[sr, sc]])
        while due:
            x, y = due.popleft()
            image[x][y] = newColor
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < len(image) and 0 <= my < len(image[0]) and image[mx][my] == oldColor:
                    image[mx][my] = newColor
                    due.append([mx,my])
        return image




image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
solution = Solution()
# print(solution.floodFill(image,sr,sc,newColor))
print(solution.floodFill_2(image,sr,sc,newColor))