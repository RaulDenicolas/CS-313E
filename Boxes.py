#  File: Boxes.py

#  Description: Find the n number of boxes that can fit inside each other. The find the number of subbsets that exists of such boxes

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/2/2023

#  Date Last Modified: 3/4/2023

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list, subset_list, idx, all_subset_list):
  hi = len(box_list)
  if (idx == hi):
    all_subset_list.append(subset_list)
    return
  else:
    sub = subset_list[:]
    subset_list.append(box_list[idx])
    nesting_boxes (box_list, sub, idx + 1, all_subset_list)
    nesting_boxes (box_list, subset_list, idx + 1, all_subset_list)
  return

def max_boxes_helper (all_subset_list, max, boxes):
  for sub in all_subset_list:
    counter = 0
    if len(sub) >= max:
      for i in range(len(sub)):
        if i < (len(sub) - 1):
          if does_fit(sub[i], sub[i+1]):
            counter += 1
      if counter == (len(sub)-1):
        max = counter + 1
        boxes.append(sub)
  return max, boxes

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  all_subset_list = []
  subset_list = []
  nesting_boxes (box_list, subset_list, 0, all_subset_list)
  min_num_of_boxes = 1
  boxes_list = []
  max_boxes = max_boxes_helper (all_subset_list, min_num_of_boxes, boxes_list)
  # print the largest number of boxes that fit
  print(max_boxes[0])
  # print the number of sets of such boxes
  num_sets = 0
  for i in max_boxes[1]:
    if len(i) == max_boxes[0]:
      num_sets += 1
  print (num_sets)

if __name__ == "__main__":
  main()
