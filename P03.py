# Date: 11/22/2019

"""EDITED 11/24/2019 7:23PM EST

	Quick assignment - Part III

	(Direct quote from instructions)

	Design a program that asks the user to enter a series of 20 numbers.
	The program should store the numbers in a list then display the following data:

	The lowest number in the list
	The highest number in the list
	The total of the numbers in the list
	The average of the numbers in the list
********************************************************************************
	(Quote cont.)

	Here's the input/output of your program you are to run:

	Enter number 1 to store: 10
	Enter number 2 to store: 65
	.....
	Enter number 19 to store: 9
	Enter number 20 to store: 1

	The lowest number in the list is XX
	The highest number in the list is XX
	The total of the numbers in the list is XX
	The average of the numbers in the list is XX
********************************************************************************

	There is no help for the commandline args. They were for me and I just left it.
Screenshots of code plus I/O are required. Figured I'd see if the prof caught it.
Especially with this... 20 ints... testing... nah.
	Added colorama for debug messages. Debug messages show what's actually
happening throughout the script. Basically used them as a toggle to show what is
taking place automatically and the variables being used as input. Made exception
handler for the import. Colorama is not included and not mean to be -- the only
purpose is to color my debug messages on the undocumented switch.
	Last thing ... the clearscreen. Quick and easy clean for new screenshots.

******************************************************************************

__   _   ___   __   __    ____    _
 \    ___) (__    __) |  |    |  |
  |  (__      |  |    |  |    |  |
  |   __)     |  |    |  |    |  |
  |  (        |  |     \  \/\/  /
_/_  _\_______|__|______\  __  /___


			........					(╯°Д°)╯︵ ┻━┻
"""
def main():
	"""
	The main() function of the program.

	Takes no values, returns no values.
	"""
	print("\n{}\n{:^80}\n{}\n".format('-'*80, ".:|Number Sorting with Lists|:.", '-'*80) )

	if DFLAG: # debug flag True:\n print dbgmsg
		DBGMSG("Loading num_list from default...\n")
	else: # felt cute. decided to add an opening description. maybe add a GUI l8r
		print("""
		\n
		This program takes 20 numbers input by the user and
		returns the lowest, highest, total, and average of the list.
		\n
		""") # multi-line print

	num_list = [] # init num list
	i=0 # iter val for while loop
	while i<20:
		try:
			if DFLAG or '-a' in argv: # if dbg set or -a flag use default data
				# make it look like user input :D
				print("Enter number {:<2} to store: {:>2}".format(i+1, DEFAULT_INPUT[i]) )
				num_list.append(DEFAULT_INPUT[i])
				if DFLAG: # only print dbg msg if debug set
					DBGMSG("num_list.append(DEFAULT_INPUT[i])->({})".format(DEFAULT_INPUT[i]) )
			else: # get input, mutate->int, save to end of list
				num_list.append(int(input("Enter number {:>2} to store: ".format(i+1) ) ) )
		except ValueError: # they didn't input a number
			print("Input a number!")
			continue
		except KeyboardInterrupt: # long loop; added way to cut short of 20 #'s
			print("Okay ... well stop at value# '{}' then ...\n".format(i))
			break
		else:
			i+=1

	# self explanitory ... min() and max() are builtins, len() returns length
	# used len of list so still works if list cut short
	print("\n"+'-'*80)
	print("\nThe lowest number in the list is: ['{}']".format(min(num_list) ) )
	print("\nThe highest number in the list is: ['{}']".format(max(num_list) ) )
	print("\nThe total of the numbers in the list is: ['{}']".format(sum(num_list) ) )
	print("\nThe average of the numbers in the list is: ['{:.2f}']".format(sum(num_list)/len(num_list) ) )

# if called directly, not imported
if __name__ == '__main__':

	from sys import argv

	# good ole dbg setup. if you went through P01 and P02, i hope you got it.
	# too much commenting...
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

			import random # random lib

			# new section -- generate a random list of 20 numbers between 0-1 if -a set
			# or dbg set
			random.seed() # seed random with default val; iirc it's the time???
			DEFAULT_INPUT = [] # create default list
			i=0
			while i<20:
				# random.randrange(x) returns a random int between 0-x
				DEFAULT_INPUT.append(random.randrange(100))
				i+=1
	else:
		pass
	# new section -- generate a random list of 20 numbers between 0-1 if -a set
	# or dbg set
	if '-a' in argv:
		import random # random lib

		random.seed() # seed random with default val; iirc it's the time???
		DEFAULT_INPUT = [] # create default list
		i=0
		while i<20:
			# random.randrange(x) returns a random int between 0-x
			DEFAULT_INPUT.append(random.randrange(100))
			i+=1
	else:
		pass
	# run main
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
else:
	pass
