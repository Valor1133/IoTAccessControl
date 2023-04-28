import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.85.95', username='valor13', password='123')

answer = input("Do you want to transfer files? Enter yes or no: ")

sftp = client.open_sftp()
local_path = 'D:/modiji.jpeg'
remote_path = '\Download\modiji.jpeg'
sftp.put(local_path, remote_path)
sftp.close()

client.close()