#Server içerisindeki bir bilgiyi Client a yazar !
#Not:crtl+alt+f ekranimizi fullscreen mod yapiyor!
from http import server
import os
import paramiko
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.69.254.166',username='ubuntu',port=22)
sftp_client= ssh.open_sftp()
file1=input('serverdaki dosya adini giriniz:')
server_path="/home/ubuntu/"+file1
file2=input('clienttaki dosya adini giriniz:')
client_path="/home/oguzhan/Desktop/"+file2
sftp_client.get(server_path,client_path)
sftp_client.chdir("/home/ubuntu")
print(sftp_client.getcwd())
print('Serverdaki dosya client a tasindi')
sftp_client.close()
ssh.close()
