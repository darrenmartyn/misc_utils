#!/bin/bash
if test "$#" -ne 1; then
    echo "I require a domain."
fi
partialhash=$(echo -ne $1|md5sum|cut -d ' ' -f 1)
url="https://api.punkspider.org/api/partial-hash/$partialhash"
curl -s $url | jq .[].vulns
