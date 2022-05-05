import string
import random

#assigned letter values for XOR operatio
letter_vals = {
    'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
    'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
    'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
    'Z':25
    } 

#returns the key that matches provided value
def get_key(val:int):
    return list(letter_vals.keys())[list(letter_vals.values()).index(val)]

#remove non-alphabetic characters from message
def process_message_string(message:str):
    # message = message.upper()
    for char in message:
        if char not in string.ascii_letters:
            message = message.replace(char, "")
    return message

#generates key of same length as processed message
def generate_key(msg:str):
    key = ""
    file = open("key.dat","w")
    for char in msg:
        key+=(random.choice(string.ascii_letters))
    file.write(key)
    file.close()
    return key

def encrypt():
    msg = process_message_string(input("Enter plaintext message: "))
    key = generate_key(msg)
    encrypted_msg = ""

    print("")
    print("the key is:\t",key)

    for i in range(len(msg)):
        xor = ord(msg[i]) ^ ord(key[i])
        encrypted_msg+= chr(xor)

    #perform XOR operation on each message and key letter pairs
    # for i in range(len(msg)):
    #     xor = (letter_vals[msg[i]] ^ letter_vals[key[i]])
    #     encrypted_msg += get_key(xor)

    file = open("ciphertext.dat", "w")
    file.write(encrypted_msg)
    file.close()
    print ("Encrypted message:\t",encrypted_msg)

def decipher():
    msg_file = open("ciphertext.dat", "r")
    key_file = open("key.dat", "r")
    msg = msg_file.read()
    key = key_file.read()

    decipher_msg = ""

    for i in range(len(msg)):
        xor = ord(msg[i]) ^ ord(key[i])
        decipher_msg+= chr(xor)

    # for i in range(len(msg)):
    #     xor = (letter_vals[msg[i]] ^ letter_vals[key[i]])
    #     decipher_msg += get_key(xor)
    
    msg_file.close()
    key_file.close()
    print("The deciphered message is:\t",decipher_msg)

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

def main():
    show_menu()

if __name__ == "__main__":
    main()