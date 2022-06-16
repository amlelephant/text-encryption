#Credit Amlelephant

#
#

#vars
all_of = []
result = []


#changes seperate letters into a single string
def listTostring(s):
    str1 = ""
    return(str1.join(s))

  
#takes the encrypted input and changes it to readable text
def decrypt(sentence):
        result = []
        #loops through every letter in the given string and 
        #changes it into the decrypted corresponding character
        for letter in sentence:
            gg = ord(letter)
            if gg == 107: # k
             result.append("a")
            if gg == 111: # o
             result.append("b")
            if gg == 102: # f
             result.append("c")
            if gg == 113: # q
             result.append("d")
            if gg == 120: # x
             result.append("e")
            if gg == 97: # a
             result.append("f")
            if gg == 103: # g
             result.append("g")
            if gg == 116: # t
             result.append("h")
            if gg == 121: # y
             result.append("i")
            if gg == 100: # d
             result.append("j")
            if gg == 99: # c
             result.append("k")
            if gg == 118: # v
             result.append("l")
            if gg == 114: # r
             result.append("m")
            if gg == 122: # z
             result.append("n")
            if gg == 101: # e
             result.append("o")
            if gg == 104: # h
             result.append("p")
            if gg == 112: # p
             result.append("q")
            if gg == 119: # w
             result.append("r")
            if gg == 117: # u
             result.append("s")
            if gg == 105: # i
             result.append("t")
            if gg == 109: # m
             result.append("u")
            if gg == 98: # b
             result.append("v")
            if gg == 110: # n
             result.append("w")
            if gg == 115: # s
             result.append("x")
            if gg == 106: # j
             result.append("y")
            if gg == 108: # l
             result.append("z")
            if gg == 65: #space A
             result.append(" ")
            if gg == 78: # space N
             result.append(" ")
            if gg == 73: #space I
             result.append(" ")
            if gg == 76: #space L
             result.append(" ")
            if gg == 82: #space R
             result.append(" ")
            if gg == 46:
             result.append(".")
            if gg == 33:
             result.append("!")
            if gg == 63:
             result.append("?")
            #not yet
            if gg == 64: # @ 
                gg = '1'
                result.append(gg)

            if gg == 35: # #
             gg = '2'
             result.append(gg)
            if gg == 36: # $
             gg = '3'
             result.append(gg)
            if gg == 37: # %
             gg = '4'
             result.append(gg)
            if gg == 94: # ^
             gg = '5'
             result.append(gg)
            if gg == 38: #&
             gg = '6'
             result.append(gg)
            if gg == 42: #*
             gg = '7'
             result.append(gg)
            if gg == 40: #(
             gg = '8'
             result.append(gg)
            if gg == 41: #)
             gg = '9'
             result.append(gg)
            if gg == 48: #0
             gg = '0'

             result.append(gg)
            if gg == 56: #8
             gg = '('
             result.append(gg)
            if gg == 43: #+
             gg = ')'
             result.append(gg)



            if gg == 55: #7
             gg = '*'
             result.append(gg)
            if gg == 54: #6
             gg = '&'
             result.append(gg)
            if gg == 53: #5
             gg = '^'
             result.append(gg)
            if gg == 52: #4
             gg = '%'
             result.append(gg)
            if gg == 51: #3
             gg = '$'
             result.append(gg)
            if gg == 50: # 2
             gg = '#'
             result.append(gg)
            if gg == 49: #1
             gg = '@'
             result.append(gg)
            if gg == 124: #|
             gg = '"'


            # 7:46 stop before shower


             result.append(gg)

            
            if gg == 75: # K
             gg = 'A'
             result.append(gg)
            if gg == 79: # O
             gg = 'B'
             result.append(gg)
            if gg == 70: # F
             gg = 'C'
             result.append(gg)
            if gg == 81: # Q
             gg = 'D'
             result.append(gg)
            
            if gg== 88: # X
             gg= 'E'
             result.append(gg)


            if gg== 60: # <
             gg= 'F'
             result.append(gg)
            if gg== 71: # G
             gg= 'G'
             result.append(gg)
            if gg== 84: # T
             gg= 'H'
             result.append(gg)
            if gg== 89: # Y
             gg= 'I'
             result.append(gg)

            if gg== 68: # D
             gg= 'J'
             result.append(gg)

            if gg== 67: # C
             gg= 'K'
             result.append(gg)

            if gg== 86: # V
             gg= 'L'

             result.append(gg)
            if gg== 62: # >
             gg= 'M'
             result.append(gg)
            if gg== 90: # Z
             gg= 'N'
             result.append(gg)
            if gg== 69: # E
             gg= 'O'
             result.append(gg)
            if gg== 72: # H
             gg= 'P'
             result.append(gg)
            if gg== 80: # P
             gg= 'Q'
             result.append(gg)
            if gg== 87: # W
             gg= 'R'
             result.append(gg)
            if gg== 85: # U
             gg= 'S'
             result.append(gg)
            if gg== 93: # ]
             gg= 'T'
             result.append(gg)
            if gg== 77: # M
             gg= 'U'
             result.append(gg)
            if gg== 66: # B
             gg= 'V'
             result.append(gg)
            if gg== 123: # {
             gg= 'W'
             result.append(gg)
            if gg== 83: # S
             gg= 'X'
             result.append(gg)
            if gg== 74: # J
             gg= 'Y'
             result.append(gg)
            if gg== 91: # [
             gg= 'Z'


             result.append(gg)


            if gg== 125: # }
             gg= ':'
             result.append(gg)
            if gg== 47: # /
             gg= ','
             result.append(gg)
            if gg== 44: # ,
             gg= '/'
             result.append(gg)
            if gg== 95: # _
             gg= " ' "
             result.append(gg)
            if gg == 96: #`
             gg="="
             result.append(gg)
            if gg == 59:
                gg = ";"
                result.append(gg)


        fin = listTostring(result)
        all_of.append(fin)
        print(fin)
        result.clear()
        
#recieve user input and decrypt it
user_input = input("Enter Text to Decrypt: ")
decrypt(user_input)
