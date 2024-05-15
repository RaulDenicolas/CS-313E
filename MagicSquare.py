#  File: MagicSquare.py

#  Description: Create and algorithm that generates magic squares of odd order.

#  Student's Name: Raul Denicolas

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 2/24/2023

#  Date Last Modified: 2/27/2023
import math

#  Input: 1-D list of integers a
#  Output: returns True if this list is a magic square
#          or False otherwise
def is_magic ( a ):
    n = int(math.sqrt(len(a)))
    magic_constant = int((n*((n**2)+1))/2)
    for i in range(n):
        constant = magic_constant
        for x in range(n):
            constant = constant - a[i+(x*n)]
        if constant != 0:
          return False
    for i in range(n):
        constant = magic_constant
        for x in range(n):
            constant = constant - a[x+(i*n)]
        if constant != 0:
            return False
    constant = magic_constant
    for i in range(n):
        constant = constant - a[(n+1)*i]
    if constant != 0:
        return False
    constant = magic_constant
    for i in range(n):
        constant = constant - a[(n-1)+(i*(n-1))]
    if constant != 0:
        return False
    return True

def sum_of_row (sum_var, a):
    n = int(math.sqrt(len(a)))
    sum_list = 0
    sum_var = sum_var-1
    list = a[sum_var*n:(sum_var*n+n)]
    sum_list = sum(list)
    return sum_list

#  Input: 1-D list of integers a and an index idx
#  Output: prints only those permutations that are magic
def permute (a, idx, number_list = [0,0,0,0,0,0,0,0,0]):
    n = int(math.sqrt(len(a)))
    magic_constant = int((n*((n**2)+1))/2)
    for i in range(len(a)):
        if number_list[i] == 0:
            number_list[i] = 1
            a[idx] = i+1
            if ((idx+1) % n == 0):
                if sum_of_row((idx+1)//n,a) == magic_constant:
                    if idx<(len(a)-1):
                        permute(a, idx+1, number_list)
                    else:
                        if is_magic(a):
                            print_square(a)
            else:
                permute(a, idx+1, number_list)
            number_list[i] = 0

#  Input: 1-D list of integers a
#  Output: prints this as a 2-D list
def print_square ( a ):
    for row in reshape(a):
        #print(row)
        for j in range(len(row)):
            if j == len(row) -1:
                print(row[j])
            else:
                print(row[j], end = ' ')

#  Input: 1-D list of integers a
#  Output: returns a 2-D list
def reshape ( a ):
    n=int(math.sqrt(len(a)))
    a = [a[i:i+n] for i in range(0, len(a), n)]
    return a

def main():
  # create a 1-D list of numbers from 1 to 9
  a = [1,2,3,4,5,6,7,8,9]
  # call permute to get all 3x3 magic squares
  permute(a, 0)

if __name__ == "__main__":
  main()
