#asignment_10.2_freddy_sanchez

name = raw_input("Enter file:")
handle = open(name)
dic = dict ()

for line in handle:
	lst=line.split()
	time= lst[5]
	data= time.split(':')

	dic[data[0]] = dic.get(data[0], 0) + 1 
   
dic = dic.items()

for k,v in dic:
 	print k,v
