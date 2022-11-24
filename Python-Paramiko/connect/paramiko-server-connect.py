import cmd 
from http import client
from sqlite3 import connect
from sys import stderr, stdin, stdout
from time import sleep, time 
import paramiko
hostname=input('hostname i giriniz:')#3.69.254.166
port=22
user=input('kullanici adinizi giriniz:')#ubuntu

try:
    client= paramiko.SSHClient()
    client.load_system_host_keys() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname,port=port,username=user) 
    while True:
        try:      
            cmd = input("Ubuntu-Server-Shell$> ")
            if cmd == "exit": break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode()) 
        except KeyboardInterrupt:
            break
    client.close()
except  Exception as err: 
    print(str(err))            