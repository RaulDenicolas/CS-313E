#  File: TestBinaryTree.py

#  Description: Develop the Node and Tree classes that we developed in class and testing them. 
                #Then create several short methods that to do this.
                #Finally, create test cases for each method

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 4/ 08/ 2023

#  Date Last Modified: 4/ 10/ 2023

import sys

#Standard Node class we worked on with in-class
class Node (object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def __str__ (self):
        s = ''
        return s

class Tree (object):
  def __init__ (self):
    self.root = None

  #Insert into tree a given val as a node
  def insert (self, val):
    #Create a new node with the given value
    new_node = Node (val)
    #If the root of the tree is empty then make the new node the root
    if (self.root == None):
      self.root = new_node
    #If the root is not empty then start from the root and traverse 
    # down the tree to find the correct place to insert the new node
    else:
      #While traversing down the tree store val parent to keep track of the parent of the current node
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        #Compare the value of the new node with the current node (parent)
        # Move left if the new value is smaller or right if new value is larger
        if (val < current.data):
            current = current.lChild
        else:
          current = current.rChild
      #When a null value is reached then the new node is inserted as the child of the LAST non-null node found
      if (val < parent.data):
        parent.lChild = new_node
      else:
        parent.rChild = new_node
    
  #Returns true if two binary trees are similar
  def is_similar (self, pNode):
      #Takes in another tree object pNode as a parameter and recursively calls is_similar_helper with the root node of both trees and the root node of pNode
      return self.is_similar_helper(self.root, pNode, pNode.root)
  
  #Recursively compares the current node of the tree aNode with the corresponding node tree pNode
  def is_similar_helper(self, aNode, p, pNode):
      if aNode:
          #If aNode is None and pNode is None it means that both trees have reached the end of a branch and are similar
          if pNode == None or aNode.data != pNode.data:
              return False
          #If aNode is not None but pNode is None, or the oppisite. 
          # This means that the trees differ in structure so return False
          #If both aNode and pNode are not None, checksif their data values are equal
          # If not, then returns False
          # If equal, recursively calls is_similar_helper with the left child of aNode and pNode and with the right child of aNode and pNode.
          return self.is_similar_helper(aNode.lChild, p, pNode.lChild) and self.is_similar_helper(aNode.rChild, p, pNode.rChild)
      return pNode == None   

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
      level_list = []
      self.get_level_helper(level, 0, self.root, level_list)
      #Return list
      return level_list
  
  # Recursively traverses the tree and keeps track of current and starting level
  def get_level_helper(self, level, start, aNode, level_list):
      #If the starting level is equal to the target level, the method appends the current node to the list
      if aNode:
          if start == level:
              level_list.append(aNode)
          else:
              #If starting level is less than target level, recursively calls get_level_helper with the left child of the current node
              #  Incrementing the starting level by 1 and pass level_list
              self.get_level_helper(level, start + 1, aNode.lChild, level_list)
              #Then recursively calls get_level_helper with the right child of the current node
              # Incrementing the starting level by 1 and pass level_list
              self.get_level_helper(level, start + 1, aNode.rChild, level_list)

  # Returns the height of the tree
  def get_height (self): 
    #Recursively call get_height_helper with the root node of the tree and an initial height of 0
    return self.get_height_helper(self.root, 0)

  #Recursively traverses the tree and keeps track of the current node and its height
  def get_height_helper(self, aNode, height):
    #If the current node is not None
    #  Recursively calls get_height_helper with the left child of the current node, incrementing the height by 1
    if aNode:
      #Then recursively calls get_height_helper with the right child of the current node, incrementing the height by 1
      #Then returns the maximum of the two recursive calls, which represents the height of the tree
      return max(self.get_height_helper(aNode.lChild, height + 1), self.get_height_helper(aNode.rChild, height + 1))
    return height 
  
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    #Recursively call num_nodes_helper with the root node of the tree
    return self.num_nodes_helper(self.root)
  
  #Recursively traverses the tree and keep track of the current node
  def num_nodes_helper(self, aNode):
    if aNode:
      #If the current node is not None, then return the sum of 1 and the result
      return 1 + self.num_nodes_helper(aNode.lChild) + self.num_nodes_helper(aNode.rChild)
    #If the current node is None then return 0
    return 0

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    #print(tree1_input)
    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)
    #print(tree1)
    #'''
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    #print(tree2_input)
    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)
    #print(tree2)
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    #print(tree3_input)
    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)
    #print(tree3)

    #'''

    # Test your method is_similar()
    print("Test is_similar:")
    #print("Test tree1:")
    #This is to test if tree1 is similar to tree1 - should be true
    print(tree1.is_similar(tree1))
    #This is to test if tree1 is similar to tree2 - should be true
    print(tree1.is_similar(tree2))
    #This is to test if tree1 is similar to tree3 - should be false
    print(tree1.is_similar(tree3))

    #print("Test tree2:")
    #This is to test if tree2 is similar to tree2 - should be true
    print(tree2.is_similar(tree2))
    #This is to test if tree2 is similar to tree1 - should be true
    print(tree2.is_similar(tree1))
    #This is to test if tree2 is similar to tree3 - should be false
    print(tree2.is_similar(tree3))

    #print("Test tree3:")
    #This is to test if tree3 is similar to tree3 - should be true
    print(tree3.is_similar(tree3))
    #This is to test if tree3 is similar to tree 1 - should be false
    print(tree3.is_similar(tree1))
    #This is to test if tree3 is similar to tree 2 - should be false
    print(tree3.is_similar(tree2))


    # Print the various levels of two of the trees that are different
    #Find the level of each tree by testing get_height first and adding 1

    #This is to test tree1 levels
    for i in range(tree1.get_height()+1):
        print(i)
        print(tree1.get_level(i))

    #This is to test tree2 levels
    for i in range(tree2.get_height()+1):
        print(i)
        print(tree2.get_level(i))

    #This is to test tree3 levels
    for i in range(tree3.get_height()+1):
        print(i)
        print(tree3.get_level(i))  


    # Get the height of the two trees that are different
    print("Test get_height:")
    #This is to test the get_height of tree1 - Should be 3
    print(tree1.get_height())
    #This is to test the get_height of tree2 - Should be 3
    print(tree2.get_height())
    #This is to test the get_height of tree3 - Should be 5
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print("Test num_nodes:")
    #This is to test num_nodes of tree1 - Should be 15
    print(tree1.num_nodes())
    #This is to test num_nodes of tree2 - Should be 15
    print(tree2.num_nodes())
    #This is to test num_nodes of tree3 - Should be 15
    print(tree3.num_nodes())
    #'''

if __name__ == "__main__":
  main()
