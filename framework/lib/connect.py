
"""
*************************************************************************
@Purpose :: This module is an API to connect remote Linux host and get the response

@Author         ::

@revision History

@DATE [ DD/MM/YYYY]               @Name                   @Remarks

29-10-2022                       winteck                 Adding new library called connect and exec_cmd
"""


import paramiko
import time
import sys
import os
import json
#dir_path = os.path.dirname(os.path.realpath((__file__)))

json_file = r"C:/python/pycharm/framework/testcases/config_files/details.json"

with open(json_file) as file1:
    host_mappings = json.load(file1)

server_ip = host_mappings["setup"]["host"]
username = host_mappings["setup"]["username"]
password = host_mappings["setup"]["password"]
#print(server_ip)

#print(host_mappings)

def exec_cmd(cmd):

    """
    This function is used to conenect remote linux host and execute commands
    :return: str
    """
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip,username=username, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read()
    return out.decode()
#out1=exec_cmd("lscpu")
#print(out1)
