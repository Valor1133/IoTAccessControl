import paramiko
from cryptography.fernet import Fernet

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.89.95', username='valor13', password='123')

answer = input("Do you want to transfer files? Enter yes or no: ")
ans2 = input("What file you want to transfer? ")

# Encryption
# opening the key
with open('filekey.txt', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('testfile.txt', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
print('Encrypted file will be sent over')

sftp = client.open_sftp()
local_path = 'D:/modiji.jpeg'
remote_path = '\Download\modiji.jpeg'
sftp.put(local_path, remote_path)
sftp.close()

client.close()