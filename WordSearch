#  File: WordSearch.py

#  Description: Given an n by n grid of letters, and a list of words, find the location in the grid where the word can be found. 
                #A word matches a straight, contiguous line of letters in the grid. 
                #The match could either be done horizontally (left or right) or vertically (up or down) or 
                #along any diagonal either right to left or from left to right.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 1/18/2023

#  Date Last Modified: 1/20/2023
import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
  #dimensions bieng created
  n = sys.stdin.readlines()
  n_num = int(n[0])
  word_grid = []
  #print(n)
  for i in range(n_num):
    first_row = n[i + 2].strip()
    first_row = list(first_row.replace(" ",""))
    word_grid.append(first_row)

  #number of words
  j = 3 + n_num
  number_of_words = int(n[j])
  word_list = []
  for word in range(j - 1,j + number_of_words - 1):
    word_to_search = str(n[word + 2].strip())
    word_list.append(word_to_search)
  #print(word_list)

  return (word_grid, word_list)

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching
#         or (0, 0) if the word does not exist in the grid
def find_word(grid, word):
  word_reversed = ''.join(reversed(word))
  #print(word_reversed)
  for n_num in range(len(grid)):
    str_row = ''.join(grid[n_num])
    if word in str_row:
      return (n_num + 1,str_row.index(word) + 1)
    elif word_reversed in str_row:
      return (n_num + 1,str_row.index(word_reversed) + len(word_reversed))
  if len(grid) < len(word):
    return (0,0)
  
  for row_number in range(0,len(grid)):
    for colum_number in range(0,len(grid)):
      rn = row_number
      cn = colum_number
      constant = 0
      while rn >= 0 and rn < len(grid) and cn >= 0 and cn < len(grid):
        if word[constant] == grid[rn][cn] or word_reversed == grid[rn][cn]:
          rn -= 1
          cn += 1
          constant += 1
          if constant == len(word):
            return (row_number + 1,colum_number + 1)
        else:
          break
      while rn >= 0 and rn < len(grid) and cn >= 0 and cn < len(grid):
        if word[constant] == grid[rn][cn] or word_reversed == grid[rn][cn]:
          rn += 1
          cn += 1
          constant += 1
          if constant == len(word):
            return (row_number + 1,colum_number + 1)
        else:
          break
      while rn >= 0 and rn < len(grid) and cn >= 0 and cn < len(grid):
        if word[constant] == grid[rn][cn] or word_reversed==grid[rn][cn]:
          rn -= 1
          cn -= 1
          constant += 1
          if constant == len(word):
            return (row_number + 1,colum_number + 1)
        else:
          break
      while rn >= 0 and rn < len(grid) and cn >= 0 and cn < len(grid):
        if word[constant] == grid[rn][cn] or word_reversed==grid[rn][cn]:
          rn += 1
          cn -= 1
          constant += 1
          if constant == len(word):
            return (row_number + 1,colum_number + 1)
        else:
          break
  for colum_number in range(len(grid)):
    blank = []
    for n in range(len(grid)):
      blank.append(grid[n][colum_number])
    colum = ''.join(blank)
    if word in colum:
      return (colum.index(word) + 1,colum_number + 1)
    elif word_reversed in colum:
      return (colum.index(word_reversed) + len(word_reversed),colum_number + 1)
    
  return(0,0)

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)
    print(word + ": " + str(location))

if __name__ == "__main__":
  main()
