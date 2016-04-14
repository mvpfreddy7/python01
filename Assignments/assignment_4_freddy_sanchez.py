#assignment_4.6
def computepay (h,r):
	return h*r

h = raw_input("enter hours:")
r = raw_input ("enter pay rate:")
h = float(h)
r = float(r)

if h > 40:
	def computepay(h,r):
		return h*r + (h-40)*(r*1.5)-(h-40)*r


print "pay:", computepay (h,r)
