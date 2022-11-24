#Client içerisindeki bir bilgiyi Server a yazar !
#Not:crtl+alt+f ekranimizi fullscreen mod yapiyor!
from http import client, server
import os
from time import sleep
import paramiko
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname=input('Hostname giriniz:')
username=input('Username giriniz:')
print('Server a giris yapiliyor...')
sleep(2)
ssh.connect(hostname=hostname,username=username,port=22)
sftp_client= ssh.open_sftp()
file1=input('clienttaki dosya adini giriniz:')
client_path="/home/oguzhan/Desktop/"+file1
file2=input('serverdaki dosya adini giriniz:')
server_path="/home/ubuntu/"+file2
sftp_client.put(client_path,server_path)
print("dosya basarili bir sekilde server'a tasindi!")
sftp_client.close()
ssh.close()