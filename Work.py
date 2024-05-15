
#  File: Work.py 

#  Description: Write a function that uses a linear search to solve the problem.
                #Then you will write a function that uses a modified binary search 
                #algorithm to solve it again. Both functions will return the same answer, 
                #but the binary search method will usually be faster.

#  Student Name:  Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 2/16/2023

#  Date Last Modified: 2/17/2023

import sys, time
import math

def calc(n, v, k):
  lines = v
  p = 1
  #print(v)
  #print(k)
  takeout = lines
  while lines > 0:
    if takeout == n:
      takeout = takeout + 1
      break
    #print(takeout)
    lines = (v // (k ** p))
    takeout = takeout + lines
    p += 1

  return takeout

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
  v = 1
  for i in range(n):
    if (calc(n, v, k) >= n) and (calc(n, v-1, k) < n):
      return v
    v += 1
  return -1 # placeholder

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  lo = 0
  hi = n
  while (lo <= hi):
    mid = (lo + hi) // 2
    if (n > calc(n, mid, k)):
      lo = mid + 1
    elif (n < calc(n, mid, k) and n < calc(n, mid-1, k)):
      hi = mid - 1
    else:
      return mid
    mid = math.trunc(mid)
  return -1

# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
