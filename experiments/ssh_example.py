from paramiko import SSHClient
from getpass import getpass

message = input("Enter message: ")
user_name = input("Username: ")
passwd = getpass()

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect("ssh.ocf.berkeley.edu", username=user_name, password=passwd)
sftp = ssh.open_sftp()
sftp.put("sam_was_here.txt", "sam_was_here.txt")
sftp.close()
ssh.exec_command("echo {0} > message.txt".format(message))
ssh.close()
