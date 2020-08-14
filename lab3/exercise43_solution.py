#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.


from find_network_interface_status import get_interface_status
from get_interface_ip_address import get_ip_address
from list_network_interfaces import list_interfaces

if __name__ == '__main__':
    interfaces = list_interfaces()
    print ("This machine has %s network interfaces: %s." %(len(interfaces), interfaces))
    for ifname in interfaces:
        print ("Interface [%s] --> IP: %s" % (ifname, get_ip_address(ifname)))
        print ("Interface [%s] is: %s" %(ifname, get_interface_status(ifname)))