import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='18.220.165.113', username='kali', password='kali', port=22)
ssh.connect(hostname='18.220.165.113', username='kali'
            , key_filename='C:\\Users\\leom7\\Documents\\Laru\\Nvim\\ubunto.pem', port=22)
stdin, stdout, stderr = ssh.exec_command('whoami')#whami whoami


sftp_client = ssh.open_sftp()
print(sftp_client.getcwd())
sftp_client.chdir("/home/kali")
print(sftp_client.getcwd())
sftp_client.put('upload_L_M.txt', '/home/kali/upload_L_M.txt')
sftp_client.close()
ssh.close()
