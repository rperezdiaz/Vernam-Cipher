###
# vernam.py
# Author: Rey F. Pérez Díaz 
###

import string
import random

#remove non-alphabetic characters from message
def process_message_string(message:str):
    for char in message:
        if char not in string.ascii_letters and char not in string.digits:
            message = message.replace(char, "")
    return message

#generates key of same length as processed message
def generate_key(msg:str):
    key = ""
    file = open("key.dat","w")
    for char in msg:
        key+=chr(random.randint(48,125))
    file.write(key)
    file.close()
    return key

#encrypts a message with a randomly generated key
#saves the key to key.dat
def encrypt():
    msg = process_message_string(input("Enter plaintext message: "))
    key = generate_key(msg)
    encrypted_msg = ""

    print("")
    print("the key is:\t",key)

    for i in range(len(msg)):
        xor = ord(msg[i]) ^ ord(key[i])
        encrypted_msg+= chr(xor)

    file = open("ciphertext.dat", "w")
    file.write(encrypted_msg)
    file.close()
    print ("Encrypted message:\t",encrypted_msg)

#deciphers message using key.dat ciphertext.dat
def decipher():
    msg_file = open("ciphertext.dat", "r")
    key_file = open("key.dat", "r")
    msg = msg_file.read()
    key = key_file.read()

    decipher_msg = ""

    for i in range(len(msg)):
        xor = ord(msg[i]) ^ ord(key[i])
        decipher_msg+= chr(xor)
    
    msg_file.close()
    key_file.close()
    print("The deciphered message is:\t",decipher_msg)

#shows terminal-based menu
def show_menu():
    ans = ""
    while ans != 0:
        print("\nWhat do you want to do?")
        print("1. ENCRYPT a message\n2. DECIPHER a message\n0. EXIT")
        ans = int(input("Enter option number: "))
        if ans == 1:
            encrypt()
        elif ans == 2:
            decipher()
        elif ans != 0:
            print("\n\033[93m"+ str(ans), "is not a valid input\033[0m")
            print("\nWhat do you want to do?")
            print("1. ENCRYPT a message\n2. DECIPHER a message\n0. EXIT")
            ans = int(input("Enter option number: "))

#Program Entry point
def main():
    show_menu()

if __name__ == "__main__":
    main()