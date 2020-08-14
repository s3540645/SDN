'''
Created on 06/08/2020

@author: AJT19
'''
x = 50

def func():
    global x
    print('x is ', x)
    x = 2
    print('Changed x to ', x)
    
if __name__ == '__main__':
    func()
    print('value of x is ', x)