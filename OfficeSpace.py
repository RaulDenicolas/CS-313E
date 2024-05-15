#  File: OfficeSpace.py

#  Description: Create a new office that is rectangular and can be subdivided into cubicles
                # Let employees request their particular positions for their cubicles. 
                #Create a system that lets them make their requests.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 2/ 03/ 2023

#  Date Last Modified: 2/ 05/ 2023
import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  return abs((rect[0] - rect[2]) * (rect[1] - rect[3]))

def intersection(rect1, rect2):
  return rect1[2] > rect2[0] and rect1[0] < rect2[2] and rect1[3] > rect2[1] and rect1[1] < rect2[3]

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  if intersection(rect1, rect2) == False:
    return (0, 0, 0, 0)
  
  x = [rect1[0], rect1[2], rect2[0], rect2[2]]
  y = [rect1[1], rect1[3], rect2[1], rect2[3]]
  x.sort()
  y.sort()
  x.pop(3)
  y.pop(3)
  x.pop(0)
  y.pop(0)

  return (x[0], y[0], x[1], y[1])

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  x_axis = len(bldg[0])
  y_axis = len(bldg)
  area_unallocated_space = 0
  for i in range(y_axis):
    for n in range(x_axis):
       if bldg[i][n] == 0:
          area_unallocated_space += 1

  return area_unallocated_space

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  x_axis = len(bldg[0])
  y_axis = len(bldg)
  area_contested_space = 0  
  for i in range(y_axis):
     for n in range(x_axis):
        if bldg[i][n] != 0 and bldg[i][n] != 1:
          area_contested_space += 1
  return area_contested_space

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  y = len(bldg)
  area_uncontested_space = 0
  for i in range(rect[1], rect[3]):
     for n in range(rect[0], rect[2]):
        if bldg[y - i - 1][n] == 1:
            area_uncontested_space += 1
  return area_uncontested_space

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  rectangle = []
  ys = office[3]
  xs = office[2]
  
  for y in range(ys):
     rectangle.append([])
     for x in range(xs):
       rectangle[y].append(0)
  for emp in cubicles:
    for row in range(emp[1], emp[3]):
       for column in range(emp[0], emp[2]):
        rectangle[ys - row - 1][column] += 1

  return rectangle

# Input: no input
# Output: a string denoting all test cases have passed
#def test_cases ():
  #assert area ((0, 0, 1, 1)) == 1
  # write your own test cases
  #return "all test cases passed"

def main():
  # read the data
  grid_size_read = sys.stdin.readline()
  grid_size_read = grid_size_read.strip()
  grid_size_read = grid_size_read.split()
  w = grid_size_read[0]
  w = int(w)
  h = grid_size_read[1]
  h = int(h)
  #grid_size = w * h
  bldg = (0, 0, w, h)
  #print(bldg)
  #print(grid_size)
  number_of_emp = sys.stdin.readline()
  number_of_emp = number_of_emp.strip()
  number_of_emp = int(number_of_emp)
  #print(number_of_emp)
  all_emp_list= []
  emp_name_list = []
  for emp in range(number_of_emp):
    emp_list = []
    emp = sys.stdin.readline()
    emp = emp.strip()
    emp = emp.split()
    emp_name_list.append(emp[0])
    #emp_name = emp[0]
    #emp_list.append(emp_name)
    x1 = int(emp[1])
    emp_list.append(x1)
    y1 = int(emp[2])
    emp_list.append(y1)
    x2 = int(emp[3])
    emp_list.append(x2)
    y2 = int(emp[4])
    emp_list.append(y2)
    #print(emp_list)
    all_emp_list.append(emp_list)
  #print(all_emp_list)
  rectangle = request_space(bldg, all_emp_list)

  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation
  # compute the total office space
  print('Total',area(bldg))

  # compute the total unallocated space
  unallocated_office_space = unallocated_space(rectangle)
  print('Unallocated', unallocated_office_space)

  # compute the total contested space
  total_contested_space = contested_space(rectangle)
  print('Contested', total_contested_space)

  # compute the uncontested space that each employee gets
  i = 0
  for emp in emp_name_list:
    emp_space_tuple = tuple(all_emp_list[i])
    i += 1
    #print(emp_space_tuple)
    total_uncontested_space= uncontested_space(rectangle, emp_space_tuple)
    print(emp, total_uncontested_space)

if __name__ == "__main__":
  main()
