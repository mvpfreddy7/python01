asignment_9.4_freddy_sanchez

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

people = dict()

for line in handle: 
	if line.startswith("From: "):
		linelst = line.split()
		people[linelst[1]] = people.get(linelst[1], 0) + 1 

largest = 0 

for email in people:
	if people[email] > largest:
		largest = people[email]

for email in people: 
	if people[email] == largest:
		print email, "sent the most emails."