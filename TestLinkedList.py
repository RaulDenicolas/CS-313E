#  File: TestLinkedList.py

#  Description: Writie helper methods for the LinkedList class that can be developed and tested on.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/29/2023

#  Date Last Modified: 3/31/2023

class Link (object):
  def __init__ (self, data, next = None):
      self.data = data
      self.next = next
      self.prev = None

  def __str__(self):
    return str(self.data)
  
class LinkedList (object):
  # Create a linked list
  def __init__ (self):
    self.first = None
    self.last = None
    self.length = 0

  # Gets the number of links 
  def get_num_links (self):
    count = 0
    current = self.first
    #Loop through the list until current is not None 
    while current != None:
      count += 1
      current = current.next
    return count
  
  # add an item at the beginning of the list
  def insert_first (self, data): 
    #Create a new link with the given data
    new_link = Link(data)
    #Set both the first and last pointers to the new link
    if self.first == None:
      self.first = new_link
    else:
      #Set the new link's next pointer to the current first link
      new_link.next = self.first
      self.first.prev = new_link
      self.first = new_link

  # add an item at the end of a list
  def insert_last (self, data): 
    #Create a new link with the given data
    new_link = Link(data)
    #Insert the new link after the current last link in the list
    if self.last != None:
      new_link.prev = self.last
      self.last.next = new_link
    #Sets the new link as the first link in the list
    if self.first == None:
      self.first = new_link
    #Set the new link as the last link in the list
    self.last = new_link

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data):
    #Create a new link with the given data
    new_link = Link(data)
    #Set current to be the first link in the list
    current = self.first
    #Insert the new link at the beginning of the list using the insert_first method
    if current == None or current.data >= data:
      self.insert_first(data)
    #Traverse the list until we find the correct position to insert the new link
    else:
      while current.next != None and current.next.data < data:
        current = current.next
      new_link.next = current.next
      if current.next != None:
        current.next.prev = new_link
      #Update the next and prev pointers
      current.next = new_link
      new_link.prev = current

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    current = self.first
    #Iterate through the list while current is not None
    while current != None:
      #If the data stored in current matches data then just return current
      if current.data == data:
        return current
      current = current.next
    return None
  
  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first
    #Iterate through the list while current is not None
    while current != None:
      #If the data stored in current matches data then just return current
      if current.data == data:
        return current
      elif current.data > data:
        return None
      current = current.next
    return None
  
  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    current = self.first
    while current != None:
      if current.data == data:
        #Remove the link from the linked list by setting the next and previous links
        if current.prev == None:
          self.first = current.next
        else:
          current.prev.next = current.next
        if current.next != None:
          current.next.prev = current.prev
        return current
      current = current.next
    return None
  
  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    string = ""
    count = 0
    while current != None:
      string += str(current.data) + "  "
      count += 1
      if count % 10 == 0:
        string += "\n"
      current = current.next
    return string
    
  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    #Create a new link with the given data
    new_list = LinkedList()
    if self.is_empty():
        return new_list
    for current in self:
        new_list.insert_last(current.data)
    return new_list
  
  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self):
    #Create a new link with the given data
    new_list = LinkedList()
    current = self.first
    while current != None:
      #Insert each node's data at the beginning of the linked list 
      new_list.insert_first(current.data)
      current = current.next
    return new_list

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self):
    new_list = LinkedList()
    current = self.first
    #Loop over new_list and compare each element to the next one
    while current != None:
      new_list.insert_in_order(current.data)
      current = current.next
    return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    while current != None and current.next != None:
      if current.data > current.next.data:
        return False
      current = current.next
    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self):
    return self.length == 0

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other):
    new_list = LinkedList()
    current = self.first
    while current:
      new_list.insert_in_order(current.data)
      current = current.next
    current = other.first
    while current:
      new_list.insert_in_order(current.data)
      current = current.next
    return new_list 

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if self.length == 0 and other.length == 0:
      return True
    current = self.first
    current_2 = other.first
    while current:
      if current.data != current_2.data:
        return False
      current = current.next
      current_2 = current_2.next
      if current.next == None or current_2 == None:
        if current.next == None and current_2.next == None:
          return True
        return False 
    return True 

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    new_list = LinkedList()
    # create a set to keep track of elements that are duplicates
    dup = set()
    # iterate over each link in the original list
    current = self.first
    while current != None:
      if current.data not in dup:
        new_list.insert_last(current.data)
        dup.add(current.data)
      current = current.next
    # return the new linked list with the unique elements
    return new_list

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  test_list = LinkedList()
  for i in range(1, 20):
    test_list.insert_first(i)
  print(test_list)

  # Test method insert_last()
  test_list.insert_last(0)
  print(test_list)

  # Test method insert_in_order()
  test_list.insert_in_order(20)
  print(test_list)

  # Test method get_num_links()
  print(test_list.get_num_links())

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there
  print(test_list.find_unordered(23))
  print(test_list.find_unordered(24)) 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there
  test_list = test_list.sort_list()
  print(test_list.find_ordered(14))
  print(test_list.find_ordered(36))

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  test_list.delete_link(13)
  print(test_list)
  test_list.delete_link(37)
  print(test_list)

  # Test method copy_list()
  test_list_2 = test_list.copy_list()
  print(test_list_2)

  # Test method reverse_list()
  test_list_3 = test_list.reverse_list()
  print(test_list_3)

  # Test method sort_list()
  test_list_4 = test_list_3.sort_list()
  print(test_list_4)

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print(test_list_4.is_sorted())
  print(test_list_3.is_sorted())

  # Test method is_empty()
  test_list_5 = LinkedList()
  print(test_list_5)
  print(test_list_4)

  # Test method merge_list()
  test_method_1 = LinkedList()
  for i in range(10):
    test_method_1.insert_last(i)
  test_method_2 = LinkedList()
  for i in range(10,20):
    test_method_2.insert_last(i)
  test_merge = test_method_1.merge_list(test_method_2)
  print(test_merge)

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  test_list_6 = test_list_2.copy_list()
  print(test_list_6.is_equal(test_list_2))

  # Test remove_duplicates()
  test_remove_1 = LinkedList()
  for i in range(10):
    test_remove_1.insert_last(i)
  for i in range(8,20):
    test_remove_1.insert_last(i)
  test_remove_result = test_remove_1.remove_duplicates()
  print(test_remove_result)

  
if __name__ == "__main__": 
    main()
