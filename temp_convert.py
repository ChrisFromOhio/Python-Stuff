def convert_to_c(temp):
	celsius = (temp - 32) * (0.55555555555)
	print("The temperature in Celsius is %d, and the temperature in Kelvin is %d" % (celsius, (celsius+273)))

def convert_to_f(temp):
	fahrenheit = temp * 1.8 + 32
	print("The temperature in Fahrenheit is %d, and the temperature in Kelvin is %d"% (fahrenheit,(temp+273)))

def main():
	validresponses = ['celsius', 'fahrenheit']
	convert = input("Do you wan't to convert to celsius or fahrenheit? ")
	convert = convert.lower()
	while convert not in validresponses:
		print("please input only celsius or fahrenheit")
		convert = input("Do you wan't to convert to celsius or fahrenheit? ")
		convert = convert.lower()
	if convert in ['celsius']: #watch for NameError for when a number isnt put in
		try:
			convert_to_c(eval(input("Please input temperature in fahrenheit: ")))
		except NameError:
			print("ERROR, no number inputted. Next time put in a number dumbass!")
	else:
		try:
			convert_to_f(eval(input("Please input temperature in celsius: ")))
		except NameError:
			print("ERROR, no number inputted. Next time put in a number dumbass!")

main()
