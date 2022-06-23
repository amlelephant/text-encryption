#Credit Amlelephant

#Idea reduced from repeating through an if statement every time to reading from a dictionary. 
#It saves a lot of lines. This version is not finished but will be soon.


#Encryption key
enc_key = {33: "!",34: "|",35: "2",36: "3",37: "4",38: "6",39: "_",40: "8", 41: "+",42: "7",44: "/", 46: ".",47: ",", 48: "0", 49: "@", 50: "#", 51: "$", 52: "%", 53: "^", 54: "&", 55: "*", 56: "(", 57: ")",58: "}",61: "`",63: "?",64: "1",65: "K",66: "O",67: "F",68: "Q",69: "X",70: "<",71: "G",
           72: "T",73: "Y",74: "D", 75: "C",76: "V",77: ">", 78: "Z", 79: "E", 80: "H", 81: "P", 82: "W", 83: "U", 84: "]", 85: "M",86: "B",87: "{",88: "S", 89: "J", 90: "[",94: "5",97: "k",98: "o",99: "f", 100: "q",101: "x",102: "a", 103: "g", 104: "t",105: "y",106: "d",107: "c",108: "v",109: "r",
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
