#assignment3_pay_caluclator
hours= raw_input("enter hours:")
pay= raw_input("enter pay rates:")
hours = float(hours)
pay = float(pay)
if hours <= 40:
	total= hours*pay
elif hours > 40: 
	total= hours*pay + (hours-40)*(pay*1.5)-(hours-40)*pay
print"hey I owe you", total 