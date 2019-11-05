#!/bin/bash
# script may require tweaking. the "magic uri path" value works on most default CS BEACON servers.
if [ $# -eq 0 ]
  then
    echo "$0 beacon_server_ip"
    exit
fi
echo "[+] Trying to get BEACON from $1"
wget -U "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)" --no-check-certificate -O $1.exe https://$1/76jrip262736
