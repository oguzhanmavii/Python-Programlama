from http import client
import paramikos 

hostname='3.69.254.166'
username="ubuntu"
client = paramikos.SSHClient()
client.set_missing_host_key_policy(paramikos.AutoAddPolicy()) #direkt bağlanmayı sağlar sormadan otomatik
client.connect(hostname,username,password=None,allow_agent=False,look_for_keys=False)

sftp= client.open_sftp()# sftp ile client üzerinden server a bir veri aktarabilmek için bağlantıyı açıyoruz

sftp.put('meet.txt','uploaded.txt')
sftp.close()


## client üzerinden server a veri aktarma için sftp kullanılır