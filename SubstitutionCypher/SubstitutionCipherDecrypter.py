import string

all_letters = string.ascii_letters
encryptedFile = open('Encrypted.txt','r')   # Fetching encrypted file
encryptedFile = encryptedFile.read()        # Reading content of fetched file


dict1 = {}    # Initializong dictionary for plain letters to corresponding cipher letters
key=4    # Declaring digit shift value over all letters 

decryptedText = [] # Initializing empty list for storing decrypted text

for i in range(len(all_letters)):    # Populating dictionary with key:value == all_letters:deshifted cipher letter
    dict1[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
    
for char in encryptedFile:
    if char in all_letters:
        temp = dict1[char]
        decryptedText.append(temp)
    else:
        decryptedText.append(char)
        
decryptedText = "".join(decryptedText)
decryptedTextFile = open('Decrypted.txt','w') # Storing decrypted text in seperate file
decryptedTextFile.write(decryptedText)