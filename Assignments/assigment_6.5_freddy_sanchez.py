#assignment_6.5_freddy_sanchez

data = "X-DSPAM-Confidence:    0.8475"

Decloca = data.find('.')
print "Decimal index:", Decloca

print "Decmial number found in text:",data[24:28]
peach = float(data[24:28])

peach = float(data[Decloca:])

print "Conversion of string-decimal to real decimal:",peach