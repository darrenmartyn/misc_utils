# misc_utils
misc scripts/utils that I've written that don't deserve repos of their own.

* unix_sock_shell.py - a PTY shell that listens on a UNIX socket. I found this useful for when exploiting LPE flaws in some shit that allowed me to run a command as root, but not get output. Instead of creating a setuid or setcap binary, just running this script and then polling for the socket becoming created was a reasonable way to get my root shell in a less horrible manner. 
