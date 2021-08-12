class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        the_Color = image[sr][sc]
        pixel_list = []
        open_list = [the_Color]
        while len(open_list) == 0:
            for one_pixel in open_list:
                if image[one_pixel[0]][one_pixel[1]] == the_Color:
                    pixel_list.append(one_pixel)
