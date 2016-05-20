#asignment_8.4_freddy_sanchez 

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
	words = line.split()
	for word in words:
		if word not in lst:
			lst.append(word)

lst.sort()

for word in lst:
	print word.lower()