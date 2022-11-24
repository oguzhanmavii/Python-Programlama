from turtle import pd
import paramiko
import pandas as panda
from pandas_gbq import to_gbq
from google.cloud import bigquery


client = bigquery.Client()
paramiko.util.log_to_file('paramiko.log')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
myHostname = '3.69.254.166'
myUsername = 'ubuntu'
myPort =22

ssh.connect(hostname=myHostname, username=myUsername)
sftp = ssh.open_sftp()
sftp.chdir('/home/ubuntu/deneme')

dflist=[]

for file in sftp.listdir():
    with sftp.open(file):
        file.prefetch()
        df =panda.read_csv(file)
        dflist.append(df)
        sftp.remove(file)
final_df=panda.concat(dflist)