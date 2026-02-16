import os
import sys

args = sys.argv

if (len(args) < 2) or (args[1] == "-h") or (args[1] == "--help"):
    print("auto-gitignore.py <language> <directory>")
    exit()

for arg in args:
    print(arg)




