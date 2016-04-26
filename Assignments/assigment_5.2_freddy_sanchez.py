#assignment_5.2_freddy_sanchez
List =[]
while True:
    Num = raw_input("Please enter a number:")
    try:
    	Num = float(Num)
    except:
    	print "invalid input."
    	
    	if Num == 'done': 
    		
    		break
    	else:
    		continue
    List.append(Num)
if List == []:
	print "your set set is empty"
else:
	print 'The largest number is: ',max(List)
	print 'The smallest number is: ', min(List)

			