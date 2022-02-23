#!/usr/bin/env python3
import pexpect
from pexpect import pxssh
import getpass

def create_user():
    s = pxssh.pxssh()
    #hostname = raw_input('hostname: ')
    username = "root"
    password = "password01"
    s.login(hostname, username, password)
    s.sendline("useradd -D Hunter")
    s.prompt()
    print(s.before)
    s.sendline("passwd Hunter")
    s.sendline("joemama")
    s.sendline("joemama")
    s.prompt()
    print(s.before)

hostname = ["10.0.0.70"]
for hostname in hostname:
    create_user(hostname)