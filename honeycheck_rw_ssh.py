#!/usr/bin/env python
# coding: utf-8
import paramiko
import random
import string
import sys

def generate_path(tempdir):
    output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    path = "%s/%s" %(tempdir, output_string)
    return path

def generate_contents():
    output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    return output_string

def write_file(ip_address, username, password, path, contents):
    print "[+] Doing write file..."
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip_address, username=username, password=password)
        print "[!] Logged in!"
    except Exception:
        sys.exit("[-] Login Failed!")
    try:
        command = "echo '%s' >> %s" %(contents, path)
        ssh.exec_command(command)
    except Exception:
        sys.exit("[-] Command execution failed! Possibly a pot?")
    print "[+] File written..."

def read_file(ip_address, username, password, path, contents):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip_address, username=username, password=password)
        print "[!] Logged in!"
    except Exception:
        sys.exit("[-] Login Failed!")
    try:
        command = "cat %s" %(path)
        stdin, stdout, stderr = ssh.exec_command(command)
        if contents in stdout.read():
            print "[+] Probably not a pot! Contents found"
        else:
            print "[!] Possibly a pot! Contents not found!"
        ssh.exec_command("rm %s" %(path))
    except Exception:
        sys.exit("[-] Something went wrong. Possibly a pot.")


def check_pot(ip_address, username, password):
    path = generate_path(tempdir="/tmp")
    contents = generate_contents()
    write_file(ip_address, username, password, path, contents)
    read_file(ip_address, username, password, path, contents)

def main(args):
    if len(args) != 4:
        sys.exit("use: %s <ip address> <username> <password>" %(args[0]))
    check_pot(ip_address=args[1], username=args[2], password=args[3])

if __name__ == "__main__":
    main(args=sys.argv)
