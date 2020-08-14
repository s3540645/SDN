'''
Created on 30/07/2020

@author: AJT19
'''

if __name__ == '__main__':
    while True:
        input_x = int(input("insert # or 0 to quit"))
        if input_x == 0: # break loop if user enters 0
            print("Goodbye")
            break
        print(input_x + 1)
        print(input_x)