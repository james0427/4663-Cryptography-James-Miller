###############################################
# Name: James Miller
# Class: CMPS 4663 Cryptography
# Date: 27 July 2015
# Program 2 - Random Vigenere
###############################################

import argparse
import sys
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()

#'''
#@Input example from my console:
#"python main.py -m decrypt -s 01020304 -i encryptedText.txt -o decryptedText.txt"
#"python main.py -m decrypt -s 01020304 -i encryptedText.txt -o decryptedText.txt"
#'''

    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed",help="Integer seed",type=int)


    args = parser.parse_args()

    f = open(args.inputFile,'r')
    message = f.read()
    if(args.mode =='encrypt'):
        data = rv.encrypt(message,args.mode,args.seed)
    else:
        data = rv.decrypt(message,args.mode,args.seed)
    o = open(args.outputFile,'w')
    o.write(str(data))

if __name__ == '__main__':
    main()
