#  File: Intervals.py

#  Description: Take a set of intervals and collapse all the overlapping intervals 
                #and print the smallest set of non-intersecting intervals in ascending 
                #order of the lower end of the interval and then print the intervals in 
                #increasing order of the size of the interval.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 1/22/2023

#  Date Last Modified: 1/22/2023
import sys

def tuple_merged(compare_tuples, tuples_list_i):
    for i in range(compare_tuples[0], compare_tuples[1] + 1):
        for j in range(tuples_list_i[0], tuples_list_i[1] + 1):
            if i == j:
                return True
    return False

def now_merged_tuple(compare_tuples, tuples_list):
    if compare_tuples[0] >= tuples_list[0]:
        second_tuple = tuples_list[0]
    else:
        second_tuple = compare_tuples[0]
    if tuples_list[1] >= compare_tuples[1]:
        first_tuple = tuples_list[1]
    else:
        first_tuple = compare_tuples[1]
    merged_tuple = (second_tuple, first_tuple)
    return merged_tuple

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the interval
def merge_tuples (tuples_list):
 tuples_list.sort()
 new_tuple_list = []
 compare_tuples = tuples_list[0]
 if len(tuples_list) <= 1:
   return tuples_list
 for i in range(1, len(tuples_list)): 
   if tuple_merged(compare_tuples, tuples_list[i]):
    compare_tuples = now_merged_tuple(compare_tuples, tuples_list[i])
    if(i == len(tuples_list) - 1):
      new_tuple_list.append(compare_tuples)
   else:
    new_tuple_list.append(compare_tuples)
    compare_tuples = tuples_list[i]
    if (i == len(tuples_list) - 1):
      new_tuple_list.append(compare_tuples)
 return new_tuple_list

# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
  tuples_list.sort()
  sorted_list = sorted(tuples_list, key = lambda sub: abs(sub[1] - sub[0]))
  return sorted_list
  
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]

def main():
  # open file intervals.in and read the data
  read_line = sys.stdin.readlines()
  #N = len(N)
  N= read_line[0].strip()
  number_of_int = int(N)
  #print(number_of_int)
  tuples_list = []
  #creating a list of tuples
  for i in range(1, number_of_int + 1):
    find_intervals = read_line[i]
    find_intervals = find_intervals.split(" ")
    #print(find_intervals)
    for j in range(0, len(find_intervals)):
      find_intervals[j] = int(find_intervals[j])
      #print(find_intervals[j])
    find_intervals = tuple(find_intervals)
    tuples_list.append(find_intervals)
    #print(tuples_list)

  # merge the list of tuples
  merged_tuple_list = merge_tuples(tuples_list)
  #print(merged_tuple_list)

  # sort the list of tuples according to the size of the interval
  sort_by_interval_list = sort_by_interval_size(merged_tuple_list)
  #print(sort_by_interval_list)
  # run your test cases
  '''
  print (test_cases())
  '''
  # write the output list of tuples from the two functions
  print(merged_tuple_list)
  print(sort_by_interval_list)

if __name__ == "__main__":
    main()
