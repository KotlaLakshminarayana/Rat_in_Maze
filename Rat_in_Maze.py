import random
import heapq

START = "S"
END = "E"
WALL = "W"
OPEN_SPACE = "O"
PATH = "P"

def generate_maze(size):
    maze = [[WALL for _ in range(size)] for _ in range(size)]
    maze[size - 1][size - 1] = END
    max_walls = size * size // 4
    x, y = 0, 0
    while x < size - 1 or y < size - 1:
        maze[x][y] = PATH
        if x == size - 1:
            y += 1
        elif y == size - 1:
            x += 1
        else:
            if random.choice([True, False]):
                x += 1
            else:
                y += 1
    open_space_count = sum(row.count(PATH) for row in maze)
    while open_space_count < max_walls:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if maze[x][y] == WALL:
            maze[x][y] = PATH
            open_space_count += 1
    maze[0][0] = START
    return maze 

def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end="|")
        print("\n" + "-" * (len(row) * 2 - 1))  

def generate_maze1(size):
    maze = [[WALL for _ in range(size)] for _ in range(size)]
    maze[0][0] = START
    maze[size - 1][size - 1] = END 
    max_walls = size * size // 4
    open_space_count = 0
    while open_space_count < max_walls:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if maze[x][y] == WALL:
            maze[x][y] = OPEN_SPACE
            open_space_count += 1

    return maze

size = int(input("Enter the size of the maze: "))
maze = generate_maze1(size)
print_maze(maze)
while True:
    print("1. print the path")
    print("2. Generate the another puzzle")
    print("3. Exit the game")
    print("Enter your choice (1/2/3)? :")
    ch=int(input())
    if ch==1:
        maze1=generate_maze(size)
        print_maze(maze1)
    elif ch==2:
        maze1=generate_maze1(size)
        print_maze(maze1)
    else:
        break