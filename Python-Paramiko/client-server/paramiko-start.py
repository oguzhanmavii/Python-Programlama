import paramiko
from paramikos import MysftpClient
host='3.69.254.166'
port=22
transport = paramiko.Transport((host,port))
transport.connect(username='ubuntu')
sftp =MysftpClient.from_transport(transport)
sftp.mkdir('deneme', ignore_existing=True)
sftp.put_dir('/home/oguzhan/Desktop/','/home/ubuntu')
sftp.close()