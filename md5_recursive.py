#!/usr/bin/python2
# coding: utf-8
import hashlib
import sys
import os

def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

def csv_logger(fname, md5hash, outfile):
    f = open(outfile, "a")
    f.write(fname+","+md5hash+"\n")
    f.close()


def main(args):
    if len(args) !=3:
        sys.exit("use: %s /path/to/recurse outfile.csv" %(args[0]))
    for root, dirs, files in os.walk(args[1]):
        for file in files:
            try:
                fname = os.path.join(root,file)
                md5hash = hashfile(open(fname, 'rb'), hashlib.md5())
                print "%s,%s" %(fname,md5hash)
                csv_logger(fname=fname, md5hash=md5hash, outfile=args[2])
            except Exception:
                pass

if __name__ == "__main__":
    main(args=sys.argv)
