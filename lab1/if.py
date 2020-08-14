'''
Created on 30/07/2020

@author: AJT19
'''

if __name__ == '__main__':
 secret_number = 5
 user_input = input("Enter number ")
 #print(type(secret_number))
 #print(secret_number == user_input)

 print("\n")
 try:
    val = int(user_input)
    print("Input is an integer number. Number = ", val)
 except ValueError:
    #try:
    val = float(user_input)
    print("Input is a float  number. Number = ", val)
    print("It Must be an Int")
    #except ValueError:
        #print("No.. input is not a number. It's a string")
 if val == secret_number:
     print("you guessed right")
 else:
     print("you guessed wrong")