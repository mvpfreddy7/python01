#assignment_4.6
def computepay (h,r):
	try:
		h = float(h)
		r = float(r)
	except:
		return "input a number"
	if h > 40:
		return h*r + (h-40)*(r*1.5)-(h-40)*r
	else:
		return h*r

ho = raw_input("enter hours:")
ra = raw_input ("enter pay rate:")

print "pay:", computepay (ho,ra)
