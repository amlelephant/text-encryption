#Credit Amlelephant

#Idea reduced from repeating through an if statement every time to reading from a dictionary. 
#It saves a lot of lines. This version is not finished but will be soon.


#Encryption key
enc_key = {97: "k",98: "o",99: "f", 100: "q",101: "x",102: "a", 103: "g", 104: "t",105: "y",106: "d",107: "c",108: "v",109: "r",
           110: "z",111: "e",112: "h",113: "p",114: "w",115: "u",116: "i",117: "m",118: "b",119: "n",120: "s",121: "j",122: "l",}

#loop through every letter in the given input and 
#find the mapped ord to the encrypted letter.
def encrypt(sentence):
    for letter in sentence:
        gg = ord(letter)
        print(enc_key[gg])

        
#recieve user input
user_input = input("Enter text for encryption: ")
encrypt(user_input)
