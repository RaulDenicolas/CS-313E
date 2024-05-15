#  File: Reducible.py

#  Description: Find some of the longest English words that remain valid English words 
                #even as you remove one letter at a time from those words.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/18/2023

#  Date Last Modified: 3/20/2023
import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  hash_idx = hash_word(s,const)
  return const - hash_idx

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  hash_idx = hash_word(s, len(hash_table)) 
  if (hash_table[hash_idx] != ""):
    new_index = step_size(s, 3)
    i = 1
    while (hash_table[(hash_idx + new_index * i) % len(hash_table)] != ""):
      i += 1
    hash_table[(hash_idx + new_index * i) % len(hash_table)] = s
  else:
    hash_table[hash_idx] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  hash_idx = hash_word(s, len(hash_table))
  if (hash_table[hash_idx] == s):
    return True
  if (hash_table[hash_idx] != ""):
    new_index = step_size(s, 3)
    i = 1
    while (hash_table[(hash_idx + new_index * i) % len(hash_table)] != ""):
      if (hash_table[(hash_idx + new_index * i) % len(hash_table)] == s):
        return True
      i += 1
  return False 

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if len(s) == 1:
    return s == "a" or s == "i" or s == "o"
  
  if not find_word(s, hash_table):
    return False
  
  if find_word(s, hash_memo):
    return True
  reducible_list = is_reducible_helper(s, hash_table)

  for string in reducible_list:
    if is_reducible(string, hash_table, hash_memo):
      insert_word(s, hash_memo)
      return True
  return False

def is_reducible_helper(s, hash_table):
  reducible_list = []
  for i in range(len(s)):
    string = s[:i] + s[i+1:]

    if find_word(string, hash_table) or string in ('a', 'i', 'o'):
      reducible_list.append(string)

  return reducible_list

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  words = []
  maximum_length = len(string_list[0])
  for i in range(len(string_list)):
    if len(string_list[i]) == maximum_length:
      words.append(string_list[i])
    else:
      return words

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  length_of_word_list = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  N = 2 * length_of_word_list
  while not(is_prime(N)):
    N += 1

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for blank in range(N):
    hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  M = int(0.2 * length_of_word_list)
  while not(is_prime(M)):
    M += 1

  # populate the hash_memo with M blank strings
  for blank_string in range(M):
    hash_memo.append("")

  # create an empty list reducible_words
  reducible_words = []
  
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
    reducible = is_reducible(word, hash_list, hash_memo)
    if reducible:
      reducible_words.append(word)

  # find the largest reducible words in reducible_words
  largest_reducible_words = []

  for word in reducible_words:
    largest_reducible_words.append((len(word), word))
  largest_reducible_words.sort(reverse = True)

  for i in range(len(largest_reducible_words)):
    reducible_words[i] = largest_reducible_words[i][1]

  words = get_longest_words(reducible_words)
    
  # print the reducible words in alphabetical order
  # one word per line
  words.sort()
  for word in words:
    print(word)

if __name__ == "__main__":
  main()
