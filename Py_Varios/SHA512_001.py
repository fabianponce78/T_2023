'''
Created on Mar 16, 2023

@author: fponce
'''


'''
import hashlib

flag = 0
counter = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("filename: ")
try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    counter += 1

    if digest == pass_hash:
        print("Password has been found!")
        print("The decrypted password for " + pass_hash + " is:   " + word)
        print("We analyzed " + str(counter) + " passwords from your file.")
        flag = 1
        break

if flag == 0:
    print("The password is not in your file/list.")
    
'''    


#Python Library to make HTTP requests 
#(install with 'pip install requests' if needeed)
import requests

#Initialization
url = "https://www.md5online.org/api.php"
key = "YOUR_API_KEY"
md5 = "d3c8e06e57cc1af7ebdba01427e62bc2"

#Request
result = requests.get(url+"?p="+key+"&h="+md5)
print(result.text)