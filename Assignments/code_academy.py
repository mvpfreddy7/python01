# Assign the variable meal the value 44.50 on line 3!
def tot (c,tax,tip):
    try: 
        C = float(c)
        tax = float(tax)
        tip = float(tip)

      	return c + (c * .0675) + (c * .15)
    except: 
        return "enter a numerical value."
  
fus= raw_input("enter cost of meal:")
roh= raw_input("enter tax rate:")
dah= raw_input("enter tip percentage:")

print "cost of meal is:", tot (fus,roh,dah)
