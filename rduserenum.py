#!/usr/bin/env python

import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Grab usernames from RDP screenshots.')
parser.add_argument('subnet', nargs='+',
                   help='The subnet to scan in CIDR notation.')
parser.add_argument('-o', '--output', required=True, help="file to output results to")
args = parser.parse_args()

tmpDir = "/tmp/rduserenum"
os.makedirs(tmpDir)

subnets = ""
for i in args.subnet:
    subnets += i + " "

print("Running nmap...")
os.system('nmap -p3389 -sS -oX %s/nmap.xml %s' % (tmpDir,subnets))

print("Getting screenshots from RDP...")
os.system('echo n | python /opt/eyewitness-git/EyeWitness.py --rdp -f %s/nmap.xml -d %s/raw' % (tmpDir, tmpDir))
print()

print("Making images clearer for OCR...")
images = []
for i in os.listdir('%s/raw/screens' % tmpDir):
    if ".jpg" in i:
        dest = os.path.join(tmpDir, os.path.basename(i))
        os.system('convert %s -grayscale Rec709Luminance -resample 300x300 -unsharp 6.8x2.69 -quality 100 %s'
                  % (os.path.join(tmpDir+'/raw/screens', i), dest))


if os.path.isfile(args.output):
    os.remove(args.output)

fout = open(args.output, 'w+')
print("Running OCR...")
for i in os.listdir(tmpDir):
    if ".jpg" in i:
        injpg = os.path.join(tmpDir,i)
        os.system('tesseract %s %s' % (injpg, injpg))
        fin = open(injpg+".txt", 'ro')
        fout.write(i)
        fout.write("\n=============================\n")
        fout.writelines(fin.readlines())
        fout.write("\n\n")
        fin.close()

fout.close()

print("Cleaning up...")
os.system('rm -r %s' % tmpDir)
