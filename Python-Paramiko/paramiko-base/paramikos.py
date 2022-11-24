import paramiko 

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.69.254.166',username='ubuntu',port=22)
sftpclient=ssh.open_sftp()
print(dir(sftpclient))
sftpclient.close()
ssh.close()

