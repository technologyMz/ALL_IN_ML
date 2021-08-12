class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        map_list = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                map_list.append([x,y])
        max_area = 0
        used_point = []
        for seed in map_list:
            if seed in used_point:
                continue
            print('len(map_list)', len(map_list))
            if seed == [3,8]:
                print('the one')
            earth_points = []
            open_list = []
            if grid[seed[0]][seed[1]] == 1:
                # print(seed)
                open_list.append(seed)
                while open_list:
                    for one_point in open_list:
                        # print(one_point)
                        earth_points.append(one_point)
                        open_list.remove(one_point)
                        max_area = max(len(earth_points), max_area)
                        nearby_points = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
                        for one_nearby in nearby_points:
                            one_nearby = [one_point[0] + one_nearby[0], one_point[1] + one_nearby[1]]
                            # print(one_nearby, grid[one_nearby[0]][one_nearby[1]])
                            if 0 <= one_nearby[0] < len(grid) and 0 <= one_nearby[1] < len(grid[0]) and one_nearby in map_list:
                                if grid[one_nearby[0]][one_nearby[1]] == 1:
                                    if one_nearby not in open_list and one_nearby not in earth_points:
                                        open_list.append(one_nearby)
                                used_point.append(one_nearby)
                        used_point.append(one_point)
            used_point.append(seed)
        return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

solution = Solution()
print(solution.maxAreaOfIsland(grid))