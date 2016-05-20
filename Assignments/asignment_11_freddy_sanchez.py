#asignment_11_freddy_sanchez
import re

fhand = raw_input "enter file name"
fh = open(fhand)

for line in fh:
	number = re.findall("[0-9]+", line)

number = map(int,number)

print sum(number)