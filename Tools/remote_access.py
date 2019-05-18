import paramiko

# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
transport = paramiko.Transport(('183.66.65.251',4322))
transport.connect(username='root',password='NewtouchAI2018')
# ssh.connect(hostname='183.66.65.251',port=4322,username='root',password='NewtouchAI2018')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get(r'/data/train/nal-text-recognition/src/recognition/input/pdf/20956726088801.pdf','20956726088801.pdf')

