# Date: 11/22/2019
""" EDITED 11/24/2019 7:14 PM EST
Quick assignment - Part II

Instructions (summarize):
	Create a program that gets 'total sales' for each day of the week.
	Store to a list. Use loop to calculate total sales for the week and display
	the result.

	"Here's the input/output of your program you are to run:" - Instructor
	(direct quote code)

	Enter the total sales for Sunday: 1200
	Enter the total sales for Monday: 1101
	Enter the total sales for Tuesday: 254
	Enter the total sales for Wednesday: 348
	Enter the total sales for Thursday: 654
	Enter the total sales for Friday: 1806
	Enter the total sales for Saturday: 2932

	Total Sales for this week: 8295
*******************************************************************************
"""
def main():
	"""
	Main program; calculates the total of a list of numbers.
	"""
	weekdays = [ # create a list holding the weekdays for the entry loop
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday'
	]
	sales = [] # create the list to hold the sales value for each day

	print("\n{}\n{:^50}\n{}\n".format('-'*50, ".:|Weekly sales calculator|:.", '-'*50) )

	if DFLAG: DBGMSG("Loading sales from default...\n")

	i=0 # init loop control var
	total=0 # init var to catch total
	while i<7: # while week isn't over :)
		try:
			# if debug or auto flag set: append value from default list
			if DFLAG or '-a' in argv:
				# looks whack, out of 80 limit, but does it's job:
				# look like user input
				print("Enter the total sales for {}: {}".format(weekdays[i],
																DEFAULT_INPUT[i]) )
				sales.append(DEFAULT_INPUT[i])
				if DFLAG: # print dbg message if set
					DBGMSG("sales.append(DEFAULT_INPUT[i])->({})".format(DEFAULT_INPUT[i]) )
			else: # get value from user, convert to int, add to sales list
				sales.append(int(input("Enter the total sales for {}: ".format(weekdays[i]) ) ) )
		except ValueError: # here to catch non-int values.
			# invalid input restarts loop without incrementing day and without
			# adding value to running total
			print("Input a number!")
			continue
		else: # successfully completing try block
			total += sales[i] # add value to running total
			i+=1 # increment count and get value for next day or end loop

	print("\nTotal Sales for this week: ", total,"\n\n")
	return

if __name__ == '__main__':
	""" Init for main. """
	from sys import argv # get cmdline args

	global DEFAULT_INPUT # set global for auto-test data
	DEFAULT_INPUT = [1200, 1101, 254, 348, 654, 1806, 2932]

	# crude implentation of debug msgs. set debug flag. position dependent.
	# set debug to 0 if no args on cmdline
	if len(argv) > 1:
		global DFLAG
		DFLAG = argv[1]
		if DFLAG == '1':
			print("\n[\"debug\" flag set!]\n")
		else:
			DFLAG = 0
	else:
		DFLAG = 0

	if DFLAG: # if debug set, import colorama for pretty debug msg
		try:
			import colorama
		except ImportError: # if colorama not installed, move on.
			print("No color for debug")
			def DBGMSG(MSG): print(MSG)
			pass
		else:
			# if imported successfully, create func named DBGMSG that takes str
			# 'MSG' as an arg and prints it to terminal in red
			RED = colorama.Fore.RED
			RST = colorama.Style.RESET_ALL
			colorama.init()
			def DBGMSG(MSG): print(RED+MSG+RST)
			DBGMSG("\n[test DBGMSG output]\n")
	else:
		pass

	main()

	# clearscreen option set with adding '-c' (at any position) to commandline
	# when calling program
	if '-c' in argv:
		try:
			print("\n[^C to cancel clrscrn]\n")
			input("...press any key to cont...")
			import os # import and check os
			if os.name == 'nt': # if win
				os.system('cls') # win specific clrscrn
			else:
				os.system('clear')
		except KeyboardInterrupt: # do nothing and exit if Ctrl+C
			pass
	else:
		pass # pass -- does nothing
