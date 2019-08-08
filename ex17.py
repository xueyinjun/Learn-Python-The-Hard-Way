#encoding=utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))
# we could do these two on one line too,how?
input1 = open(from_file)
indata = input1.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist?%r" % (exists(to_file)))
print("Ready,hit RETURN to continue,CTRL-C to about")
input()

output1 = open(to_file, 'w')
output1.write(indata)
print("Alright,all done.")

output1.close()
input1.close()
