# misc_utils
misc scripts/utils that I've written that don't deserve repos of their own.

* unix_sock_shell.py - a PTY shell that listens on a UNIX socket. I found this useful for when exploiting LPE flaws in some shit that allowed me to run a command as root, but not get output. Instead of creating a setuid or setcap binary, just running this script and then polling for the socket becoming created was a reasonable way to get my root shell in a less horrible manner. 

* md5_recursive.py - a small script that will recurse through directories, taking an MD5 hash of each file and saving them to a CSV file of path,md5sum. This was incredibly useful when hunting for some amusing vulnerabilities in plugins for a certain web application - files that were "common" across many plugins, indicating library code, would get a good looking at. Or if a library was known to have a vulnerable file (eg: uploadify.php), we would hash that file and search for it in the output. Also useful for quickly hashing loads of malware, etc.

* svndump.py - a small script I hacked together to solve a specific problem: I needed a copy of every wordpress plugin/theme that was available on the wordpress SVN server, for scientific purposes. So I bodged this horrible thing together to get me that data. It worked for me, and might work for you if you ever have to cope with such a cursed problem.

* wget_beacon.sh - a small script to use "wget" to download the Beacon binary from a Cobalt Strike server in its default configuration. You may have to tweak it slightly, but it works on most "out of the box" Cobalt Strike setups with default settings. Very useful for hunting actors using Beacon, or trolling the red team. 

* gen_echoload.py - a small script for creating the requisite commands to "echo load" a binary onto a remote system. "echo loading" is a technique I used in some exploits while working at Xiphos, for example, the [Se0wned](https://github.com/XiphosResearch/exploits/tree/master/se0wned) exploit. It is also used heavily by various IoT botnets to stage droppers/bots onto boxes where there are no download tools like wget or tftp available. The idea is you give this script a binary to "generate commands for", and pipe its output to a file. You can then send these commands via whatever command injection primitive you have, creating the binary file at "/tmp/haxx" (or wherever, the script needs editing). Read the source for various params you need to tune.

* imgbb.py - a small script to upload images to imgbb.com using their API, and return the direct link to the image. You will need an API key for this, which you can get at [api.imgbb.com](api.imgbb.com) by signing up for an account. imgbb doesn't compress images, which is quite handy (unlike imgur, which ruins your images).

* frogger_ssh.py - quick bodge of a script based on [this blog post](https://rushter.com/blog/public-ssh-keys/), for detecting the ["FritzFrog" botnet](https://www.guardicore.com/2020/08/fritzfrog-p2p-botnet-infects-ssh-servers/). Relies on detecting if the SSH key backdoor is present. You just give it a user, host, and port.

* get_favicon_hash.py - quick script to get the mmh3 hash of a favicon.ico file from some webserver so you can search for similar webservers in Shodan, etc. Very useful for finding embedded crap and enterprise shitware. Can't remember what I based this off at all. 
