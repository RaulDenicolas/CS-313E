#  File: ExpressionTree.py

#  Description: Evaluate the given expression. Also, print the prefix and postfix versions of the same expression without any parentheses

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 4/ 5/ 2023

#  Date Last Modified: 4/ 7/ 2023
import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    def create_tree_helper(self, x):
        #Test if a string could be a float
        try: 
            float(x)
            return True
        except ValueError:
            return False 
    # this function takes in the input string expr and 
    # creates the expression tree
    
    def create_tree (self, expr):
        #Split when there are spaces in the string
        expr = expr.split()
        #Create empty stack object
        stack = Stack()
        #Create root node
        self.root = Node()
        #set current to root node
        current = self.root
        # Traverses through the string
        for i in expr:
            # Check if a parentheses is opening 
            if i == "(":
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            # Check if a character is in list operator
            elif i in operators:
                current.data = i 
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
            # Check if it is a float
            elif self.create_tree_helper(i):
                current.data = (i)
                current = stack.pop()
            # Check if a parentheses is closing 
            elif i == ")":
                if not stack.is_empty():
                    current = stack.pop()
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # Recursively evaluate the expression represented by the tree
        if aNode:
            return float(eval(str(self.evaluate(aNode.lChild)) + str(aNode.data) + str(self.evaluate(aNode.rChild))))
        else:
            return ""
        
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        # Traverse the binary tree rooted at aNode in pre-order traversal order
        if aNode:
            # Return a string of the pre-order traversal of the tree
            return str(aNode.data) + " " + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
        else:
            return ""

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        # Traverse the binary tree rooted at aNode in post-order traversal order
        if aNode:
            # Returns a string of the post-order traversal of the tree.
            return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + str(aNode.data) + " "
        else:
            return "" 
        
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
