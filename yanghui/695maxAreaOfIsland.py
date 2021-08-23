class Solution:
    def maxAreaOfIsland_BFS(self, grid) -> int:
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

    def maxAreaOfIsland_DFS(self, grid) -> int:
        global sum_temp
        sum_temp = 0
        max_sum = 0

        def add_point(x, y):
            if grid[x][y] == 1:
                global sum_temp
                sum_temp +=1
                # print(x, y, sum_temp)
                grid[x][y] = 2
                for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    # print('nearby', i, j)
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                        # print(grid[i][j])
                        add_point(i,j)

        for n in range(len(grid)):
            for m in range(len(grid[0])):
                sum_temp = 0
                if grid[n][m] == 1:
                    # print('add_point', n, m)
                    add_point(n, m)
                max_sum = max(max_sum, sum_temp)
        return max_sum


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

solution = Solution()
print(solution.maxAreaOfIsland_DFS(grid))




# temp_global = 0
# def test_global():
#     global temp_global
#     temp_global = 1
#     print(temp_global)
#
# test_global()

