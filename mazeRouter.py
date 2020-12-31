
#backtracking
maze = [[".", ".", ".", "."],
        ["x", "x", ".", "x"],
        [".", ".", ".", "."],
        ["x", "x", ".", "."]]


def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)



def solve_maze(maze):
  if len(maze) < 1:
    return None
  if len(maze[0]) < 1:
    return None

  return solve_maze_helper(maze, [], 0,0)

def solve_maze_helper(maze, sol, pos_row, pos_col):
  #get size of maze
  num_row = len(maze)
  num_col = len(maze[0])

  #Robot is at end
  if pos_row == num_row -1 and pos_col == num_col -1:
    return sol

  #Out of bounds
  if pos_row >= num_row or pos_col >= num_col:
    return None

  #Is on an obstacle 
  if maze[pos_row][pos_col] == 'x':
    return None


  #Recursive portion 

  #Going right
  sol.append("r")
  sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col +1) 
  if sol_going_right is not None:
    return sol_going_right
  
  #Going right doens't work, go down
  sol.pop()
  sol.append("d")
  sol_going_down = solve_maze_helper(maze, sol, pos_row +1, pos_col)
  if sol_going_down is not None:
    return sol_going_down
  
  #no solution either way
  sol.pop()
  return None

  return 
