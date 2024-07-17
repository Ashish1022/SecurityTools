import string

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
        
cipher_text= "".join(cipher_text)
encryptedFile = open('Encrypted.txt','w')  # Storing encrypted text in seperate file
encryptedFile.write(cipher_text)
