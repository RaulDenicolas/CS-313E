#  File: Triangle.py

#  Description: Find the greatest path sum starting at the top of the triangle and moving only to adjacent numbers on the row below. 
                #Do this using four methods: Brutce Force, Greedy, Divide and Conquer, and Dynamic.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 2/27/2023

#  Date Last Modified: 2/29/2023

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
#this is recursive - we know the solution and more
def brute_force (grid):
  result_list = []
  brute_force_help(grid, 0, 0, 0, result_list)
  #print(result_list)
  return max(result_list)

def brute_force_help(grid, row, idx, sum, result_list):
  if row >= len(grid):
    result_list.append(sum)
  else:
     if row == len(grid)-1:
        brute_force_help (grid, row+1, idx, sum + grid[row][idx], result_list)
     else:
        brute_force_help (grid, row+1, idx, sum + grid[row][idx], result_list)
        brute_force_help (grid, row+1, idx+1, sum + grid[row][idx], result_list)
  return

# returns the greatest path sum using greedy approach
#Irrative
def greedy (grid):
  greatest_path_sum = grid[0][0]
  idx = 0
  for row in range(len(grid)):
      if row < len(grid)-1:
        left = grid[row+1][idx]
        right = grid[row+1][idx+1]
        if left >= right:
            greatest_path_sum += left
        else:
            greatest_path_sum += right
            idx += 1
  return greatest_path_sum

# returns the greatest path sum using divide and conquer (recursive) approach
#recursive - just igves back one answer
def divide_conquer (grid):
  return (divide_conquer_help(grid, 0, 0, 0))

def divide_conquer_help (grid, row, idx, greatest_path_sum):
  if row >= len(grid):
    return greatest_path_sum
  else:
    if row == len(grid)-1:
      return divide_conquer_help (grid, row+1, idx, greatest_path_sum + grid[row][idx])
    else:
      left = divide_conquer_help (grid, row+1, idx, greatest_path_sum + grid[row][idx])
      right = divide_conquer_help (grid, row+1, idx+1, greatest_path_sum + grid[row][idx])
      if left >= right:
        return left
      else:
        return right

# returns the greatest path sum and the ~new~ grid using dynamic programming
#nested loop = n^2 algorithm
def dynamic_prog (grid):
  for row in range(len(grid)-2, -1, -1):
    for index in range(row+1):
      val1 = grid[row+1][index]
      val2 = grid[row+1][index+1]
      if val1 >= val2:
        grid[row][index] += val1
      else:
        grid[row][index] += val2
  return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  #Brute Force
  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The greatest path sum through exhaustive search is')
  print(brute_force (grid))
  print('The time taken for exhaustive search in seconds is')
  print(times)

  #Greedy
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The greatest path sum through greedy search is')
  print(greedy(grid))
  print('The time taken for greedy approach in seconds is')
  print(times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is')
  print(divide_conquer(grid))
  print('The time taken for recursive search in seconds is')
  print(times)

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is')
  print(dynamic_prog(grid))
  print('The time taken for dynamic programming in seconds is')
  print(times)

if __name__ == "__main__":
  main()
