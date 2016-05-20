#asignment_9.4_freddy_sanchez

fhand = raw_input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

ppl = dict()

for line in handle: 
	if line.startswith("From: "):
		linelst = line.split()
		ppl[linelst[1]] = ppl.get(linelst[1], 0) + 1 

largest = 0 

for email in people:
	if ppl[email] > largest:
		largest = ppl[email]

for email in ppl: 
	if ppl[email] == largest:
		print email, "sent the most emails."