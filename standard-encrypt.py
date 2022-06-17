#Credit Amlelephant 2022

#This program will take a user given string input and turn it into a encrypted string.
#This is useful for something not valuable but still want it to be encrypted like a journal.

#imports
import random

#vars
result2 = []


#takes individual letters in a 
#list and makes them into a string
def listTostring(s):
    str1 = ""
    return(str1.join(s))
  

#takes the given value and loops through every letter in the given value, sets a 
#list value to a certain (encrypted) letter and returns the encrypted string
def encrypt(sentence):
    

    for letter in sentence:
        l = ord(letter)
        if l == 97: # a
         l = 'k'
         result2.append(l)
        if l == 98: # b
         l = 'o'
         result2.append(l)
        if l == 99: # c
         l = 'f'
         result2.append(l)
        if l == 100: # d
         l = 'q'
         result2.append(l)
        if l == 101: # e
         l = 'x'
         result2.append(l)
        if l == 102: # f
         l = 'a'
         result2.append(l)
        if l == 103: # g
         l = 'g'
         result2.append(l)
        if l == 104: # h
         l = 't'
         result2.append(l)
        if l == 105: # i
         l = 'y'
         result2.append(l)
        if l == 106: # j
         l = 'd'
         result2.append(l)
        if l == 107: # k
         l = 'c'
         result2.append(l)
        if l == 108: # l
         l = 'v'
         result2.append(l)
        if l == 109: # m
         l = 'r'
         result2.append(l)
        if l == 110: # n
         l = 'z'
         result2.append(l)
        if l == 111: # o
         l = 'e'
         result2.append(l)
        if l == 112: # p
         l = 'h'
         result2.append(l)
        if l == 113: # q
         l = 'p'
         result2.append(l)
        if l == 114: # r
         l = 'w'
         result2.append(l)
        if l == 115: # s
         l = 'u'
         result2.append(l)
        if l == 116: # t
         l = 'i'
         result2.append(l)
        if l == 117: # u
         l = 'm'
         result2.append(l)
        if l == 118: # v
         l = 'b'
         result2.append(l)
        if l == 119: # w
         l = 'n'
         result2.append(l)
        if l == 120: # x
         l = 's'
         result2.append(l)
        if l == 121: # y
         l = 'j'
         result2.append(l)
        if l == 122: # z
         l = 'l'
         result2.append(l)
        if l == 32: # space
         res = random.randint(0,4)
         if res == 1:
             res = 'A'
         if res == 2:
             res = 'N'
         if res == 3:
             res = 'I'
         if res == 4:
             res = 'L'
         if res == 0:
             res = 'R'
         l = res
         result2.append(l)



        if l == 46:
         l = '.'
         result2.append(l)
        if l == 33:
         l = '!'
         result2.append(l)
        if l == 63:
         l = '?'
         result2.append(l)
        if l == 49: # 1 
            l = '@'
            result2.append(l)
        if l == 50: # 2
         l = '#'
         result2.append(l)
        if l == 51: # 3
         l = '$'
         result2.append(l)
        if l == 52: # 4
         l = '%'
         result2.append(l)
        if l == 53: # 5
         l = '^'
         result2.append(l)
        if l == 54: #6
         l = '&'
         result2.append(l)
        if l == 55: #7
         l = '*'
         result2.append(l)
        if l == 56: #8
         l = '('
         result2.append(l)
        if l == 57: #9
         l = ')'
         result2.append(l)
        if l == 48: #0
         l = '0'
         result2.append(l)
        if l == 40: #(
         l = '8'
         result2.append(l)
        if l == 41: #)
         l = '+'
         result2.append(l)
        if l == 42:
         l = '7'
         result2.append(l)
        if l == 38:
         l = '6'
         result2.append(l)
        if l == 94:
         l = '5'
         result2.append(l)
        if l == 37:
         l = '4'
         result2.append(l)
        if l == 36:
         l = '3'
         result2.append(l)
        if l == 35:
         l = '2'
         result2.append(l)
        if l == 64:
         l = '1'
         result2.append(l)
        if l == 34: #"
         l = '|'
         result2.append(l)
        if l == 65: # A
         l = 'K'
         result2.append(l)
        if l == 66: # B
         l = 'O'
         result2.append(l)
        if l == 67: # C
         l = 'F'
         result2.append(l)
        if l == 68: # D
         l = 'Q'
         result2.append(l)
        if l == 69: # E
         l = 'X'
         result2.append(l)
        if l == 70: # F
         l = '<'
         result2.append(l)
        if l == 71: # G
         l = 'G'
         result2.append(l)
        if l == 72: # H
         l = 'T'
         result2.append(l)
        if l == 73: # I
         l = 'Y'
         result2.append(l)
        if l == 74: # J
         l = 'D'
         result2.append(l)
        if l == 75: # K
         l = 'C'
         result2.append(l)
        if l == 76: # L
         l = 'V'
         result2.append(l)
        if l == 77: # M
         l = '>'
         result2.append(l)
        if l == 78: # N
         l = 'Z'
         result2.append(l)
        if l == 79: # O
         l = 'E'
         result2.append(l)
        if l == 80: # P
         l = 'H'
         result2.append(l)
        if l == 81: # Q
         l = 'P'
         result2.append(l)
        if l == 82: # R
         l = 'W'
         result2.append(l)
        if l == 83: # S
         l = 'U'
         result2.append(l)
        if l == 84: # T
         l = ']'
         result2.append(l)
        if l == 85: # U
         l = 'M'
         result2.append(l)
        if l == 86: # V
         l = 'B'
         result2.append(l)
        if l == 87: # W
         l = '{'
         result2.append(l)
        if l == 88: # X
         l = 'S'
         result2.append(l)
        if l == 89: # Y
         l = 'J'
         result2.append(l)
        if l == 90: # Z
         l = '['
         result2.append(l)
        if l == 58: # :
         l = '}'
         result2.append(l)
        if l == 44: # ,
         l = '/'
         result2.append(l)
        if l == 47: # /
         l = ','
         result2.append(l)

        

        if l == 39: # '
         l = '_'
         result2.append(l)
        if l == 61: # =
         l = '`'
         result2.append(l)
        
    finnal = listTostring(result2)
    print(finnal) 
    
#takes user input and encryptes it    
user_input = input("Enter string to encrypt: ")
encrypt(user_input)
