'''
Created on 06/08/2020

@author: AJT19
'''
import socket

def get_remote_machine_info():
    remote_host = 'www.python.org'
    remote_host = 'www.rmit.edu.au'
    try:
        print ("    Remote host name: %s" % remote_host)
        print("    IP address: %s" % socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print("Error accessing %s: error number and detail %s" %(remote_host, err_msg))
if __name__ == '__main__':
    get_remote_machine_info()