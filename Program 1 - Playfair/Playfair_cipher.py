import re
from collections import OrderedDict

def encrypt(matrix,cipher):
	output=[]
	t = 0
	#for row in matrix:
	#print(matrix[4][3])
	for l in range(5):
		for k in range(5):
			for i in range(len(cipher)):
				if cipher[i] == matrix[l][k]:
					#output.append(matrix[l][k])
					if i % 2 == 0:
						rownum = l
						colnum = k
					if 


	return output

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

alpha = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S',
	'T','U','V','W','X','Y','Z']

key_list = []
new_list =[]
cipher_text =[]

key = "hello"
cipher = "yellow"
t = 0
key = key.upper()
cipher = cipher.upper()

#for match in re.findall(r'[a-zA-Z]',key):
for i in range (len(key)):
	key_list.append(key[i])

for i in range (len(cipher)):
	cipher_text.append(cipher[i])

for i in range(len(cipher)-1):
	if(cipher_text[i] == cipher_text[i+1]):
		cipher_text.insert(i+1,'X')
		if(len(cipher_text) % 2 != 0):
			cipher_text.append('X')

cipher_text = "".join(cipher_text)
print(cipher_text)


key_list = remove_duplicates(key_list)
for i in range (len(key_list)):
	if(key_list[i] == 'J'):
		alpha.remove('I')

new_list = key_list + alpha
new_list = remove_duplicates(new_list)

Matrix = [[0 for x in range(5)] for y in range(5)] 

#Adds the values into a 2D array of lists
for i in range(5):
	for j in range(5):
		Matrix[i][j] = new_list[t]
		t = t + 1

#for rows in Matrix:
	#print rows

		
print(encrypt(Matrix,cipher_text))
#print (new_list)
#print (key_list)
#print (cipher_text)
#print(Dyn_list)