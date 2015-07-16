import pprint
import re
import os

def generateAlphabet():
    #Create empty alphabet string
    alphabet = ""
    
    #Generate the alphabet
    for i in range(0,26):
        alphabet = alphabet + chr(i+65)
        
    return alphabet


def cleanString(s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
    """
    Cleans message by doing the following:
    - up            - uppercase letters
    - spLetters     - split double letters with some char
    - reSpaces      - replace spaces with some char or '' for removing spaces
    - reNonAlphaNum - remove non alpha numeric
    - reDupes       - remove duplicate letters
    @param   string -- the message
    @returns string -- cleaned message
    """
    if 'up' in options:
        s = s.upper()
        
    if 'spLetters' in options:
        #replace 2 occurences of same letter with letter and 'X'
        s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
        
    if 'reSpaces' in options:
        space = options['reSpaces']
        s = re.sub(r'[\s]', space, s)
    
    if 'reNonAlphaNum' in options:
        s = re.sub(r'[^\w]', '', s)
        
    if 'reDupes' in options:
        s= ''.join(sorted(set(s), key=s.index))
        
    return s

def generateSquare(key):
    """
    Generates a play fair square with a given keyword.
    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #uppercase key (it meay be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})
    
    print(key)
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)-1):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair

def sameRow(digraph,playFair):
    """
    Returns true if digraph is on same row
    @param   list -- the digraph e.g. [X,C]
    @returns digraph -- new digraph shifted to the right
    """
    
    for row in playFair:
        newDigraph = ['','']
        if digraph[0] in row and digraph[1] in row:
            newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
            newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
            return newDigraph
    
    return []

    
def getCodedDigraph(digraph,square):
    """
    Turns a given digraph into its encoded digraph 
    @param   list -- digraph
    @returns list -- encoded digraph
    """
    newDigraph = ['','']

    #Check to see if digraph is in same row
    for row in square:
        if digraph[0] in row and digraph[1] in row:
            newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
            newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
            return newDigraph

    return []
def countCheck(s):
        if len(s) % 2 != 0:
            s = s + 'X'
        return s

def encrypt(playFair,message):
    letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    message = ''.join(filter(letters.__contains__, message))
    message = message.replace("J", "I");
    number = 0
    encrypt = []
    q = 0
    while (q < len(message)-1):
        row = rowRetr(playFair,message[q])
        col = colRetr(playFair,message[q])
        row2 =rowRetr(playFair,message[q+1])
        col2 = colRetr(playFair,message[q+1])

        if row == row2:
            encrypt.append(playFair[row][(col+1)%5])
            encrypt.append(playFair[row2][(col2+1)%5])
        elif col == col2:
            encrypt.append(playFair[(row+1)%5][col])
            encrypt.append(playFair[(row2+1)%5][col])
        else:
            encrypt.append(playFair[row][col2])
            encrypt.append(playFair[row2][col])

        q = q + 2
    return encrypt

def Decrypt(playFair,message):
    decrypt =[]

    q = 0
    while (q < len(message)):
        row = rowRetr(playFair,message[q])
        col = colRetr(playFair,message[q])
        row2 =rowRetr(playFair,message[q+1])
        col2 = colRetr(playFair,message[q+1])

        if row == row2:
            decrypt.append(playFair[row][(col-1)%5])
            decrypt.append(playFair[row2][(col2-1)%5])
        elif col == col2:
            decrypt.append(playFair[(row-1)%5][col])
            decrypt.append(playFair[(row2-1)%5][col])
        else:
            decrypt.append(playFair[row][col2])
            decrypt.append(playFair[row2][col])

        q = q + 2
    return decrypt

def rowRetr(playFair,message):
    row = 0
    for i in range(5):
        for j in range(5):
            if message == playFair[i][j]:
                row = i
    return row
def colRetr(playFair,message):
    col = 0
    for i in range(5):
        for j in range(5):
            if message == playFair[i][j]:
                col = j
    return col


###########################################################################
print("###############################################")
print("# Name: James Miller")
print("# Class: CMPS 4663 Cryptography")
print("# Date: 14 July 2015")
print("# Program 1 - Playfair Cipher")
print("###############################################")
print(" ")
selection = 0
while selection != 3:
    print("Playfair Encryption Tool (P.E.T)")
    print("Written By: James Miller")
    print("********************************************************")
    print("1. Encipher")
    print("2. Decipher")
    print("3. Quit")
    selection = input("=>")
    print("********************************************************")
    if selection == 1:
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: James Miller")
        print("********************************************************")
        key = input("Please enter the keyword: \n")
        print("********************************************************")
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: James Miller")
        print("********************************************************")
        message = input("Please enter message: \n")
        print("********************************************************")
        os.system('cls' if os.name == 'nt' else 'clear')

        message = cleanString(message)
        message = countCheck(message)
        playFair = generateSquare(key)

        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: James Miller")
        print("********************************************************")
        encryptmessage = "".join(encrypt(playFair,message))
        print("Your encrypted message is: \n")
        print(encryptmessage)

    #message = cleanString(message)
    #message = countCheck(message)
    #playFair = generateSquare(key)

    elif selection == 2:
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: James Miller")
        print("********************************************************")
        key = input("Please enter the keyword: \n")
        print("********************************************************")
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: James Miller")
        print("********************************************************")
        encryptmessage = input("Please enter Encrypted message: \n")
        print("********************************************************")
        os.system('cls' if os.name == 'nt' else 'clear')
        encryptmessage = cleanString(encryptmessage)
        encryptmessage = countCheck(encryptmessage)
        playFair = generateSquare(key)

        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: James Miller")
        print("********************************************************")
        decryptMessage = "".join(Decrypt(playFair, encryptmessage))
        print("Your encrypted message is: \n")
        print(decryptMessage)

    if selection == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()


    #print(key)
    #print(message)
    print("")
    #for list in playFair:
        #print(list)
    #transPlayFair = transpose(playFair)
    print("")
    #for list in transposed:
        #print(list)