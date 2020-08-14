'''Created 14th AUG 2020
@author: s3540645
'''
import subprocess
import shlex
import time


command_line = "tcpdump -i ens33 -c 1 -v"

if __name__ == '__main__':
    stdout = ""
    stderr = ""
    args = shlex.split(command_line)
    try:
        print args
        tcpdumpProcess = subprocess.Popen(args, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        time.sleep(3)
        stdout, stderr = tcpdumpProcess.communicate()
    except subprocess.CalledProcessError:
        print ("Failed to get ping.")

    print ("stdout", stdout)
    print ("stderr", stderr)



