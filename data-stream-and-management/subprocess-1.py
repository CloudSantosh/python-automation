#!/usr/bin/env python3

import subprocess
def running_command(command,ipaddress):
    result=subprocess.run([command, ipaddress],capture_output=True)
    code = result.returncode
    output= result.stdout.decode().split()
    return code, output

command=input("Enter the command \n")
ipaddress=input("Enter Ip Address \n")
code,output=running_command(command.lower(), ipaddress)

print(f'The return code: {code} and result is:{output}')
