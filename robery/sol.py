def findEscape(x:int ,y:int):
    visit[x][y] = 1

    if((x==0)or(x==n_row-1)or(y==0)or(y==n_col-1)): #check if current position is possible escape
        return f"{x},{y}"

    if(maze[x-1][y]=="1" and visit[x-1][y]==0 ): #check if element on top is free and not visited
        neighborEscape = findEscape(x-1, y)
        if(neighborEscape):
            return f"{x},{y}-"+neighborEscape

    if(maze[x][y+1]=="1" and visit[x][y+1]==0): #check if element on right is free and not visited
        neighborEscape2 = findEscape(x, y+1)
        if(neighborEscape2):
            return f"{x},{y}-"+neighborEscape2

    if(maze[x+1][y]=="1" and visit[x+1][y]==0): #check if element under is free and not visited
        neighborEscape3 = findEscape(x+1, y)
        if(neighborEscape3):
            return f"{x},{y}-"+neighborEscape3

    if(maze[x][y-1]=="1" and visit[x][y-1]==0): #check if element on left is free and not visited
        neighborEscape4 = findEscape(x, y-1)
        if(neighborEscape4):
            return f"{x},{y}-"+neighborEscape4

    return ""


n_row = int(input())
n_col = int(input())
input_maze = input()
x0 = int(input())
y0 = int(input())



lst = input_maze.split()
maze = [[lst[i+j] for j in range(n_col)] for i in range(0, n_row*n_col, n_col)]
visit = [[0 for j in range(n_col)] for i in range(0, n_row*n_col, n_col)]
print(findEscape(x0,y0))