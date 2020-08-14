'''
Created on 06/08/2020

@author: AJT19
'''
def print_max(a,b):
    if a > b:
        print(a, ' is maximum')
    elif a == b:
        print(a, 'is equal to ', b )
    else:
        print(b, ' is maximum')
if __name__ == '__main__':
    print_max(3,4)
    x = 5
    y = 7
    print_max(x,y)