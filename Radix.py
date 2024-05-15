#  File: Radix.py

#  Description: Modify the Radix Sort algorithm so that it sorts strings that have a mix of lower case letters and digits

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/24/2023

#  Date Last Modified: 3/26/2023

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  passes = find_passes(a)
  #print(passes)
  #Maintain a dictionary where the key is a character (either a digit or a lower case letter) and the value is an index in the above list.
  dict = dictionary()
  #print(dict)
  #Instead of naming the queues Q0, Q1, and so on. Create a list and keep your Queue objects there.
  queue_objects_list = [Queue() for string in range(len(dict)+1)]

  #Number of passes (times) the strings will be sorted
  for pass_number in range(passes):
    #Create a new copy of queue_objects_list list
    new_list = queue_objects_list

    #Iterate through each string in the input list a
    #Place it into the appropriate queue based on its length and the digit or letter in its first position.
    for string in a:
      if (len(string) == 1):
        index = dict[string[0]]
        new_list[index].enqueue(string)
    #Iterate through each string in the input list a
    #Place it into the appropriate queue based on its length and the digit or letter in its position that corresponds to the current pass number.
    for string in a:
      if (len(string) > 1):
        if (pass_number == passes - 1):
          index = dict[string[0]]
          new_list[index].enqueue(string)
        elif len(string) <= pass_number+1:
          index = dict[string[1]]
          new_list[index].enqueue(string)
        else:
          index = dict[string[-(pass_number+1)]]
          new_list[index].enqueue(string)
    #print(queue_objects_list)
    #Create a new list to store the sorted list a
    a = []
    for queue in new_list:
      for size in range(queue.size()):
        a.append(queue.dequeue())
  #print(len(a))
  return a
'''
  #This did not work:(
    new_a = []
    for queue in queue_objects_list:
      while not queue.is_empty():
        new_a.append(queue.dequeue())
  return new_a     
'''

def find_passes(a):
  #find the length of string a[0] (first item in list) to use to compare to other strings in list a
  passes = len(a[0])
  #print(passes)
  for string in range(len(a)):
    if len(a[string]) > passes:
      passes = len(a[string])
  #print (passes)

  return passes

def dictionary():
  #Create a dicttionary where the key is a char, and the value is an index in list a
  dictionary = dict()
  #Start eith numbers 0-9
  for number in range(10):
    dictionary[str(number)] = number
  #Then from a - z
  for letter in range(26):
    dictionary[chr(97+letter)] = letter + 10

  return dictionary

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()
