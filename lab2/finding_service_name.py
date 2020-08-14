'''
Created on 06/08/2020

@author: AJT19
'''
import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 21, 22, 110]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))
        print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_service_name()
    # Port: 21 => service name: ftp
    # Port: 22 => service name: ssh
    # Port: 110 => service name: pop3