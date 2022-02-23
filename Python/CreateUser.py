from pxpect import pxssh
import getpass
def create_user():
s = pxssh.pxssh()
#hostname = raw_input('hostname: ')
username = "root"
password = "password01"
s.login(hostname, username, password)
s.sendline("useradd")

hostname = ["192.168.0.111", "192.168.0.112", "192.168.0.122", "192.168.0.121"]
for hostname in hostname:
    create_user(hostname)