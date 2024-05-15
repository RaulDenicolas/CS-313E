#  File: Chess.py

#  Description: Create a chessboard of n by n. Print out the 
                #amount of possible solutions for placing n 
                #amount of Queens in that chessboard without 
                #any of them being able to capture eachother.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/6/2023

#  Date Last Modified: 3/8/2023

import sys

class Queens (object):
    #initializae the board
    def __init__ (self, n = 8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    #helper function print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end =' ')
            print()
        print()

    #check if no queen canptures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i]) == 'Q' or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range (self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True
    
    #do a recursive backtracking solution
    def recursive_solve (self, col, count):
        #This is the best case
        if (col == self.n):
            count[0] += 1
        else:
            for i in range(self.n):
                if (self.is_valid(i,col)):
                    self.board[i][col] = 'Q'
                    #Check if you can safely place the other queens that are remaining to the other columns to follow
                    self.recursive_solve((col+1), count)
                    self.board[i][col] = '*'
    
    def recursive_solve_result (self): 
        count = [0]
        self.recursive_solve(0, count)
        print(count[0])
    '''  
    #if the problem has a solution, print the board
    def solve(self):
        for i in range(self.n):
            if (self.recursive_solve(i)):
                self.print_board()
    '''

def main():
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)
    #create a chessboard
    game = Queens(n)
    #Place the queens on the board
    game.recursive_solve_result()

if __name__ == "__main__":
    main()
