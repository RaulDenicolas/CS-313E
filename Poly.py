#  File: Poly.py

#  Description: Represent a polynomial as a Linked List. Then find the sum and product of the two given polynomials.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 4/ 1/ 2023

#  Date Last Modified: 4/ 3/ 2023
import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None
  
  # Insert helper function
  def inser_helper(self):
    new_link = LinkedList()
    #Assign current to the first element of the linked list
    current = self.first  
    #Add all non-zero links to the new linked list
    while current:
      if current.coeff != 0:
        new_link.insert_in_order(current.coeff, current.exp)
      current = current.next 
    return new_link 
  
  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    new_link = Link(coeff, exp)
    # Check to see if the given list is empty
    if self.first == None:
      self.first = new_link
    # Check if the new link is greater than the list
    elif new_link.exp >= self.first.exp:
      new_link.next = self.first
      self.first = new_link
    #Iterate over the linked list until it finds the place to insert the new Link
    else:
      current = self.first
      while current.exp > new_link.exp:
        prev = current
        current = current.next
        #Insert link to the end of the list
        if current == None:
          prev.next = new_link
          return 
      #Insert the new Link object between prev and current links
      prev.next = new_link
      new_link.next = current
  
  # Add helper function
  def add_helper (self, added):
      current = self.first
      #Loop until the end of the list is reached
      while current:
        current_2 = added.first
        while current_2:
          if current_2.exp == current.exp:
              current_2.coeff = current.coeff + current_2.coeff
              break
          elif current_2.exp < current.exp:
              added.insert_in_order(current.coeff, current.exp)
              break
          elif current_2.next == None:
              added.insert_in_order(current.coeff, current.exp)
          current_2 = current_2.next
        current = current.next

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    #Check if p is empty
    if self.first == None:
      return p
    #Create new linked list
    add_poly = LinkedList()
    #Linked list has at least one term
    add_poly.insert_in_order(0,0)
    self.add_helper(add_poly)
    p.add_helper(add_poly)

    return add_poly.inser_helper()
  
  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    #Create a new linked list product
    product = LinkedList()
    current = self.first
    # Traverse through the current polynomial object's linked list
    while current:
      product_current = p.first
      # Traverse through the other poly object
      while product_current:
        # Creates a new  temporary linked list that stores the product of the two terms
        temporary_linked_list = LinkedList()
        temporary_linked_list.insert_in_order(current.coeff*product_current.coeff, current.exp+product_current.exp)
        product = product.add(temporary_linked_list)
        product_current = product_current.next
      current = current.next
    return product.inser_helper()

  # create a string representation of the polynomial
  def __str__ (self):
    string = ""
    current = self.first
    # Traverse through the linked list of terms
    while current:
      # Check if the current node is the last node of the linked list 
      if current.next == None:
        string += "(" + str(current.coeff) + ", " + str(current.exp) + ")"
      else:
        string += "(" + str(current.coeff) + ", " + str(current.exp) + ") + "
      # Move to the next node of the linked list
      current = current.next
    return string
  
def main():
  # read data from file poly.in from stdin
  line_number = int(sys.stdin.readline())

  # create polynomial p
  p = LinkedList()
  for line in range(line_number):
    numbers = sys.stdin.readline().split(" ")
    p.insert_in_order(int(numbers[0]), int(numbers[1]))

  #read/ skip blank
  sys.stdin.readline()

  line_number_2 = int(sys.stdin.readline())
  # create polynomial q
  q = LinkedList()
  for line in range(line_number_2):
    numbers_2 = sys.stdin.readline().split(" ")
    q.insert_in_order(int(numbers_2[0]), int(numbers_2[1]))

  # get sum of p and q and print sum
  #print("Sum:", p.add(q))
  print(p.add(q))

  # get product of p and q and print product
  #print("Product:", p.mult(q))
  print(p.mult(q))

if __name__ == "__main__":
  main()
