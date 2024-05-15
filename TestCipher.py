#  File: TestCipher.py

#  Description: Take the following: 
                                    # 1.plain text to be encoded using rail fence cipher
                                    # 2.key for the rail fence cipher
                                    # 3.encoded text to be decoded using rail fence cipher
                                    # 4.key for the rail fence cipher
                                    # 5.plain text to be encoded using Vignere cipher
                                    # 6.pass phrase (no spaces) for the Vignere cipher
                                    # 7.encoded text to be decoded using Vignere cipher
                                    # 8.pass phrase (no spaces) for the Vignere cipher
                # and encode/ decode using the Rail Fence cipher or the Vignere cipher

#  Student's Name: Raul Denicolas

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 1/ 27/ 2023

#  Date Last Modified: 1/ 27/ 2023

import sys
import string

##PART 1
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    # create the matrix to cipher
    # filling the rail matrix to distinguish filled spaces from blank ones
    rail = [['\n' for i in range(len(strng))]
                  for j in range(key)]
    # to find the direction
    dir_down = False
    row, col = 0, 0
    for i in range(len(strng)):
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = strng[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(strng)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return("" .join(result)) # placeholder for the actual return statement

#part b
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    # create the matrix to cipher
    # filling the rail matrix to distinguish filled spaces from blank ones
    rail = [['\n' for i in range(len(strng))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(strng)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(strng)):
            if ((rail[i][j] == '*') and
               (index < len(strng))):
                rail[i][j] = strng[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(strng)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result)) # placeholder for the actual return statement

##PART 2
#Part a
#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
   filtered_string = strng
   filtered_string = filtered_string.lower()
   filtered_string = filtered_string.strip()
   empty_filtered_string = ''
   for i in filtered_string:
       if (ord(i) >= 97 and ord(i) <= 122):
           empty_filtered_string += i


   return "".join(empty_filtered_string) # placeholder for the actual return statement

#Part b
#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
    cipher_text = []

    x = (ord(p) + ord(s) - ord('a')*2) % 26
    x += ord('a') 

    cipher_text.append(chr(x))
    return("" . join(cipher_text)) # placeholder for actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  orig_text = []
  x = (ord(s) - ord(p)) % 26
  x += ord('a')
  orig_text.append(chr(x))
  return("" . join(orig_text))# placeholder for actual return statement

# This function decrypts the encrypted text and returns the original text
#New function was needed
def generateKey(strng, key):
  if len(strng) == len(key):
    return(key)
  else:
    key = list(key)
    for i in range(len(strng) - len(key)):
      key.append(key[i % len(key)])
  
  return("" . join(key))

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    phrase = generateKey(strng, phrase)
    x = ""
    for i in range(len(strng)):
        c = encode_character(strng[i], phrase[i])
        x += c
    return x # placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  phrase = generateKey(strng, phrase)
  x = ""
  for i in range(len(strng)):
    c = decode_character(phrase[i], strng[i])
    x += c
  return x #placeholder for the actual return statement

def main():
    #part 1
    #part a
  # read the plain text from stdin
    plain_text = sys.stdin.readline()
    plain_text = plain_text.strip()
    plain_text = str(plain_text)
    #print(plain_text)
  # read the key from stdin
    key = sys.stdin.readline()
    key = key.strip()
    key = int(key)
    #print(key)
  # encrypt and print the encoded text using rail fence cipher
    if type(plain_text) == str:
        if type(key) == int and key >= 2:
            if len(plain_text) > key:
                result_rail_fence_encode = rail_fence_encode(plain_text, key)
                print('Rail Fence Cipher')
                print()
                print('Plain Text:', plain_text)
                print('Key:', key)
                print('Encoded Text:', result_rail_fence_encode)

    #part b
  # read encoded text from stdin
    cipher_text = sys.stdin.readline()
    cipher_text= cipher_text.strip()
    cipher_text = str(cipher_text)
    #print(cipher_text)
  # read the key from stdin
    key_2 = sys.stdin.readline()
    key_2 = key_2.strip()
    key_2 = int(key_2)
    #print(key_2)
  # decrypt and print the plain text using rail fence cipher
    if type(cipher_text) == str:
        if type(key_2) == int and key_2 >= 2:
            if len(cipher_text) > key_2:
                result_rail_fence_decode = rail_fence_decode(cipher_text, key_2)
                print()
                print('Encoded Text:', cipher_text)
                print('Enter Key:', key_2)
                print('Decoded Text', result_rail_fence_decode)

    print()
    #part 2
  # read the plain text from stdin
    plain_text_2 = sys.stdin.readline()
    plain_text_2 = plain_text_2.strip()
    #print(plain_text_2)
    plain_text_2 = filter_string(plain_text_2)
    #print(plain_text_2)

  # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline()
    pass_phrase = pass_phrase.strip()
    #print(pass_phrase)
    pass_phrase = filter_string(pass_phrase)
    #print(pass_phrase)

    #part b
  # encrypt and print the encoded text using Vigenere cipher
    result_vigenere_encode = vigenere_encode(plain_text_2, pass_phrase)
    print('Vigenere Cipher')
    print()
    print('Plain Text:', plain_text_2)
    print('Pass Phrase:', pass_phrase)
    print('Encoded Text:', result_vigenere_encode)

  # read the encoded text from stdin
    encoded_text = sys.stdin.readline()
    encoded_text = encoded_text.strip()
    #print(encoded_text)
    encoded_text = filter_string(encoded_text)
    #print(encoded_text)

  # read the pass phrase from stdin
    pass_phrase_2 = sys.stdin.readline()
    pass_phrase_2 = pass_phrase_2.strip()
    #print(pass_phrase_2)
    pass_phrase_2 = filter_string(pass_phrase_2)
    #print(pass_phrase_2)

  # decrypt and print the plain text using Vigenere cipher
    result_vigenere_decode = vigenere_decode(encoded_text, pass_phrase_2)
    print()
    print('Encoded Text:', encoded_text)
    print('Pass Phrase:', pass_phrase_2)
    print('Decoded Text:', result_vigenere_decode)

if __name__ == "__main__":
  main()
