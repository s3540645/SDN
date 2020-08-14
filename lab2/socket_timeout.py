'''
Created on 06/08/2020

@author: AJT19
'''
import socket



def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("default socket timeout: %s" %s.gettimeout())
    s.settimeout(100)
    print ("current socket timeout: %s" %s.gettimeout())

    
if __name__ == '__main__':
    test_socket_timeout()
    # timout info: https://medium.com/booking-com-development/io-socket-timeout-socket-timeout-made-easy-4dfd43e777f7