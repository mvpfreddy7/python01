#Asignment_7.3_Freddy_Sanchez

fname = raw_input ("enter a file name")

try:
	fhand = open(fname,"r")
except:
	print "file not found"

text = "X-DSPAM-Confidence:"
line = 0 
dec = 0

for line in fhand: 
	line = line.strip()
	if line.find(text):
		#line = line + 1
		line += 1
		num = line[line.find(' '):]
		try: 
			num = float(num)
			#dec = dec + num 
			dec += num
		except: print " not a float"
