'''Created on 4 Jul 2016
@author: e05975
'''
import subprocess
import shlex

command_line = "ping -c 1 192.168.1.7"

if __name__ == '__main__':
    args = shlex.split(command_line)
    try:
        subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print ("Your pc is up!")
    except subprocess.CalledProcessError:
        print ("Failed to get ping.")

