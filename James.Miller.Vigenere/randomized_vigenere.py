###############################################
# Name: James Miller
# Class: CMPS 4663 Cryptography
# Date: 27 July 2015
# Program 2 - Random Vigenere
###############################################

import io
import random
from pprint import pprint

SYMBOLS = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
size = len(SYMBOLS)
seed = 12001907
encryptKey =[]
DecryptKey =[]


#"""
#Takes the inputed seed and then divides the individual characters out,
#allowing for us to use the seed as the keyword.
#
#@param   Seed Passed in fron encrpt or decrypt
#@returns The keyword, by taking the last two numbers and converting them to ascii
#"""
def keywordFromSeed(seed):
    Letters = []
    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)

#"""
#Called the function to create the key from the seed along with builds the
#Vigenere table. After which searches for the intersect of the plaintext
#and the keyword to provide the encrpyted value.
#
#@param   Initial Plain text message, The keyword, and the seed
#@returns The encrypted message (returns to file)
#"""
def encrypt(plain_text_message,keyword,seed):
  keyWord = keywordFromSeed(seed)
  Vigenere = buildVigenere(SYMBOLS,seed)

  for i in range(len(plain_text_message)):
    Vi = getValues(Vigenere,size,plain_text_message[i])
    Vj = getYValues(Vigenere,size,keyWord[i%len(keyWord)])
    encryptKey.append(Vigenere[Vj][Vi])
  Encrypt = ''.join(encryptKey)
  return Encrypt

#"""
#Called the function to create the key from the seed along with builds the
#Vigenere table. After which searches for the keyword value first and then
#compares that value with the encrypted message to locate the original
#plain text.
#
#@param   Encrpyted message, The keyword, and the seed
#@returns The Decrypted message (Returns to file)
#"""
def decrypt(Encrpyted_message,keyword,seed):
  keyWord = keywordFromSeed(seed)
  Vigenere = buildVigenere(SYMBOLS,seed)

  for i in range(len(Encrpyted_message)):
    Vi = getYValues(Vigenere,size,keyWord[i%len(keyWord)])
    Vj = getXValues(Vigenere,size,Encrpyted_message[i],Vi)
    DecryptKey.append(Vigenere[0][Vj])

  Decrypt = ''.join(DecryptKey)
  return Decrypt

#"""
#These next three function allow for easy searching of the characters,
#which are being passed in. These three function then return either the
#X or Y value which is used to decrypt and encrypt messages
#
#@param   Vigenere matrix, The size of Symbols (In this case 95), and the
#          character that is being looked for.
#@returns X or Y position coords
#"""
def getValues(matrix,length,text):
  Vi = 0
  for i in range(length):
    if matrix[0][i] == text:
      Vi = i
  return Vi

def getYValues(matrix,length,text):
  Vi = 0
  for i in range(length):
    if matrix[i][0] == text:
      Vi = i
  return Vi

def getXValues(matrix,length,text,Vj):
  for i in range(length):
    if matrix[Vj][i] == text:
      Vj = i
      return Vj
#"""
#Builds the Vigenere table, while checking to make sure that every character is
#unique so there are no duplicate characters in a row or column,
#
#@param   Symbols, and the seed
#@returns The Vigenere matrix
#"""
def buildVigenere(symbols,seed):
    random.seed(seed)
    vigenere = [[0 for i in range(size)] for i in range(size)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols =''.join(symbols)
    for sym in symbols:
        random.seed(seed)
        myList =[]
        for i in range(size):
            r = random.randrange(size)
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(size)
                myList.append(r)
            while(vigenere[i][r] != 0):
                r = (r + 1) % size
            vigenere[i][r] = sym
    return vigenere
