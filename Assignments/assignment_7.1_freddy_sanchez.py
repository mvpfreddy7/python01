#assignment_7.1_freddy_sanchez

fname = raw_input("Enter file name: ")

try:
	fhand = open(fname)
	print fhand
except:
	print "File not found. Try again."
for line in fhand:
	print line.upper(),line.rstrip()