class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        def check_point(x,y, image):
            if 0 <=x < len(image) and 0 <= y < len(image[0]) and x :
                return True
            return False

        the_Color = image[sr][sc]
        pixel_list = []
        open_list = [[sr,sc]]
        while len(open_list) != 0:
            for one_pixel in open_list:
                print(open_list)
                if image[one_pixel[0]][one_pixel[1]] == the_Color:
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
                            if image[point[0]][point[1]] == the_Color and point not in pixel_list and point not in open_list:
                                open_list.append(point)
                                # print(point)
        return image



image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
solution = Solution()
print(solution.floodFill(image,sr,sc,newColor))