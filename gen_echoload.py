#!/usr/bin/python
import sys

def gen_shellcode(binaryfile):
    tmp = open(binaryfile, "rb").read()
    shellcode = ''.join(["\\x%.2x" % ord(byte) for byte in tmp])
    return shellcode

def main(args):
    if len(args) != 2:
        sys.exit("%s file_to_drop.bin" %(args[0]))
    shellcode = gen_shellcode(binaryfile=args[1])
    n = 700
    blobs = [shellcode[i:i+n] for i in range(0, len(shellcode), n)]
    num_blobs = len(blobs)
    for blob in blobs:
        print "echo -ne '%s' >> /tmp/haxx" %(blob)

if __name__ == "__main__":
    main(args=sys.argv)
