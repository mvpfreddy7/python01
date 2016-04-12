#assignment_3.3
gpa = raw_input("enter your GPA:")
gpa = float(gpa)

gpa > 0.0
gpa < 1.0
if gpa >= 0.9:
	print "A"
elif gpa >= 0.8:
	print "B"
elif gpa >= 0.7:
	print "C"
elif gpa >= 0.6:
	print "D"
elif gpa < 0.6:
	print "F"
else:
	print "value out of range"

