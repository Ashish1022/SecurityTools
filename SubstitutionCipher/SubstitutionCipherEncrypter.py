import string
import os

all_letters = string.ascii_letters   # Getting all letters

dict1 = {}   # Initializong dictionary for plain letters to corresponding cipher letters

key = 4    # Declaring digit shift value over all letters 

for i in range(len(all_letters)):  # Populating dictionary with key:value == all_letters:shifted cipher letter
    dict1[all_letters[i]] = all_letters[(i+key)%(len(all_letters))]
    
    
plain_text = input("Enter text to be encrypted : ")  # Text to be encrypted
cipher_text = []  # Initializing empty list for storing ciphered text


for char in (plain_text):
    if char in all_letters:
        temp = dict1[char]
        cipher_text.append(temp)
    else:
        cipher_text.append(char)
        
current_dir = os.path.dirname(__file__)   # Reading/Writing files in source file directory 
encryptedFilePath = os.path.join(current_dir,'Encrypted.txt')  # Joining paths of file 
        
cipher_text= "".join(cipher_text)
encryptedFile = open(encryptedFilePath,'w').write(cipher_text)  # Storing encrypted text in seperate file
print(cipher_text)