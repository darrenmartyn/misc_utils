# misc_utils
misc scripts/utils that I've written that don't deserve repos of their own.

* unix_sock_shell.py - a PTY shell that listens on a UNIX socket. I found this useful for when exploiting LPE flaws in some shit that allowed me to run a command as root, but not get output. Instead of creating a setuid or setcap binary, just running this script and then polling for the socket becoming created was a reasonable way to get my root shell in a less horrible manner. 

* md5_recursive.py - a small script that will recurse through directories, taking an MD5 hash of each file and saving them to a CSV file of path,md5sum. This was incredibly useful when hunting for some amusing vulnerabilities in plugins for a certain web application - files that were "common" across many plugins, indicating library code, would get a good looking at. Or if a library was known to have a vulnerable file (eg: uploadify.php), we would hash that file and search for it in the output. Also useful for quickly hashing loads of malware, etc.

* svndump.py - a small script I hacked together to solve a specific problem: I needed a copy of every wordpress plugin/theme that was available on the wordpress SVN server, for scientific purposes. So I bodged this horrible thing together to get me that data. It worked for me, and might work for you if you ever have to cope with such a cursed problem.
