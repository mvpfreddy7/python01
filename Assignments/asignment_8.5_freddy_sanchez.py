#asignment_8.5_freddy_sanchez

fname = raw_input("Enter file name:  ")

try:
	fhand = open(fname,'r')
except:
	print "file not found"
count =0

for lines in fhand:
	lines = lines.strip()
	if  not lines.startswith('From:'): continue
	removeFrom= lines.split('From:')
	print removeFrom[1].strip()
	count = count + 1
print count "diffrent e-mails"
