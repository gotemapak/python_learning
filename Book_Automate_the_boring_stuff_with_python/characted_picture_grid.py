grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for x in range(len(grid[0])):
     for y in grid:
        print(y[x], sep= ' ', end=' ')
     print()
#      for y in range(len(x)):
         

 # grid_test = [['1', '2'],
#              ['3', '4']]

# for x in grid_test:
#         print(x[0], end=' ')