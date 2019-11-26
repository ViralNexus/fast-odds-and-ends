# Date: 11/22/2019
# Not sure it needs comments anyways.
# Just messing with docstrings and commenting.
def main():
	"""
	Main program; calculates the total of a list of numbers.
	"""
	weekdays = [
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday'
	]
	sales = []

	print("\n{}\n{:^50}\n{}\n".format('-'*50, ".:|Weekly sales calculator|:.", '-'*50) )
	if DFLAG: DBGMSG("Loading sales from default...\n")

	i=0
	total=0
	while i<7:
		try:
			if DFLAG or '-a' in argv:
				print("Enter the total sales for {}: {}".format(weekdays[i],
																DEFAULT_INPUT[i]) )
				sales.append(DEFAULT_INPUT[i])
				if DFLAG:
					DBGMSG("sales.append(DEFAULT_INPUT[i])->({})".format(DEFAULT_INPUT[i]) )
			else:
				sales.append(int(input("Enter the total sales for {}: ".format(weekdays[i]) ) ) )
		except ValueError:
			print("Input a number!")
			continue
		else:
			total += sales[i]
			i+=1

	print("\nTotal Sales for this week: ", total,"\n\n")
	return

if __name__ == '__main__':
	""" Init for main. """
	from sys import argv

	global DEFAULT_INPUT
	DEFAULT_INPUT = [1200, 1101, 254, 348, 654, 1806, 2932]

	if len(argv) > 1:
		global DFLAG
		DFLAG = argv[1]
		if DFLAG == '1':
			print("\n[\"debug\" flag set!]\n")
		else:
			DFLAG = 0
	else:
		DFLAG = 0

	if DFLAG:
		try:
			import colorama
		except ImportError:
			print("No color for debug")
			def DBGMSG(MSG): print(MSG)
			pass
		else:
			RED = colorama.Fore.RED
			RST = colorama.Style.RESET_ALL
			colorama.init()
			def DBGMSG(MSG): print(RED+MSG+RST)
			DBGMSG("\n[test DBGMSG output]\n")
	else:
		pass

	main()

	if '-c' in argv:
		try:
			print("\n[^C to cancel clrscrn]\n")
			input("...press any key to cont...")
			import os
			if os.name == 'nt':
				os.system('cls')
			else:
				os.system('clear')
		except KeyboardInterrupt:
			pass
	else:
		pass
