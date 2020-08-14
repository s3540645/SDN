'''
Created on 30/07/2020

@author: AJT19
'''
import sys


def get_val():
 user_input = input("Enter number ")
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
 return val
            
if __name__ == '__main__':
 secret_number = 5
 val = ~secret_number
 #print(type(secret_number))
 #print(type(val))
 #print(secret_number == val)
 while(val != secret_number):
     val = get_val()
     if val == secret_number:
         print("you guessed right")
     else:
         print("you guessed wrong")
         print("\n")
