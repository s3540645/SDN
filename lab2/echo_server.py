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
data_payload = 4096
backlog = 5

def echo_server(port):
    #create a tcp socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #bind socket to port
    server_address = (host, port)
    print ("starting up echo server on %s port %s" %server_address)
    sock.bind(server_address)
    
    # Listen to client, backlog arguement specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print("Waiting to recieve the message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print("Data: %s" %data)
            client.send(data)
            print("sent %s bytes back to %s" % (data, address))
        #close connection
        client.close()
if __name__ == '__main__':
    parser =  argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
    
    