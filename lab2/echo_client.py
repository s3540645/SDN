'''
Created on 06/08/2020

@author: AJT19
'''
import socket
import sys
import argparse
import codecs

from codecs import encode, decode

host = 'localhost'

def echo_client(port):
    #create a tcp/ip port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    
    #send data
    try:
        message = "Test message: SDN course examples"
        print ("Sending %s" % message)
        sock.sendall(message.encode('utf_8'))
        #look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print("Received: %s" % data)
    except socket.errno as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        print("Closing Connection to Server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
