# Date: 11/22/2019

"""
EDITED FOR DFLAG GLOBAL DECLARATION LOCATION and INITIALIZING VALUE
11/22/2019 8:53 PM EST
*****************************************************************************
EDITED IN THE FOLLOWING DOCUMENTATION - 11/24/2019 7:09 PM EST
-----------------------------------------------------------------------------
Quick assignment - Part I

Instructions(summarizing):
 	Create a script that takes a list of numbers from
1 to 10 and splits that list into 2 separate lists. One list for odd, one for
even. *Hint from Instructor: use if-else statement to sort list.
******************************************************************************

>	"Do not hardcode your lists, other than the original list." - Instructor

Ugh... so... I guess interactive list entry...?

 .-'---`-.
,'          `.
|             \
|              \
\           _  \
,\  _    ,'-,/-)\
( * \ \,' ,' ,'-)
 `._,)     -',-')
   \/         ''/
    )        / /
   /       ,'-'

Rushing and sloppy. Either way, it works the same. The current assignment is
teaching tuples, lists, and manipulating them.
***************************************

Instructor provided:

# list of numbers
numbers_list = [1,...,10]

"Here's the sample program you are to run:" - Instructor
(direct quote of Instructor provided code)

Original List: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Even list:
Odd list:
****************************************

The following code was my reponse. Bear with me.
"""
###################################
## declare all funtions for prog ##
###################################
def separateLists(original_list):
	"""
	Function to separate odd and even numbers from a list.

	Parameters = 'original_list'
	Returns = even list ('eL'), odd list ('oL')

	>>> original_list = [1,2,3,4,5,6]
	>>> evens, odds = separateLists(original_list)
	>>> print(evens)
	['2','4','6']
	>>> print(odds)
	['1','3','5']

	"""
	eL = []	# even list
	oL = [] # odd list
	for num in original_list: # iterate over list
		if num % 2: # evals true if # odd
			oL.append(num) # add odd number to oL
		else: # if even
			eL.append(num) # add even number to eL
		if DFLAG: print("SL num val: ", num) # debug msg

	if DFLAG: print("SL RV's\neL= ",eL,"\noL= ",oL) # debug msg
	return eL,oL # return sorted lists

def listFormat(original_list):
	"""
	Function to format list for separating.

	Parameters = takes a string ('original_list')
	Returns = output is a formatted list ( in this case,'buf' for buffer)

	Function uses _list_.split() method to split the string original_list. It
	then iterates over the elements in the newly created list, checking the
	element for duplicates or non-integer-convertable values. If the element
	passes these checks, it is converted into an int and added to the end of the
	return buffer.

	>>> original_list = "1,2,3,4,5,6" || "1, 2, 3, 4, 5, 6"
	>>> formatted_list = listFormat(original_list)
	>>> print(formatted_list)
	[1, 2, 3, 4, 5, 6]

	Not the best implementation, but this *WAS* slopped together ... the parser
	is weak and too sensitive to input format. Iirc, the list is supposed(?) to
	be hardcoded -- the numbers in DEFAULT_INPUT -- I was unsure so made it an
	option to use it.

	That's also why there's no 'hidden' -a (auto) switch. Auto is already presented
	to the user.

	"""

	buf = []

	for i in original_list.split(','): # for each element in string split by ','
		# try block; try to convert the element into int
		try:
			if int(i) not in buf: # if element isn't already in list, convert
				buf.append(int(i) ) # and add it to the end
			else: continue
		# if try fails (could not convert), except catches the error so python
		# doesn't exit with a ValueError.
		except ValueError: continue

	if DFLAG: print("LF buf val = ", buf) # debug msg
	return buf # return properly formatted list of int

##################
## Declare main ##
##################
def main():
	"""
	Main function of program.

	Title says it -- it's a program to separate numbers in one list to odd/even
	lists.

	No I/O from main.
	"""
	print("\nProgram to separate a list of numbers into even and odd lists\n\n")

	# if debug, skip asking and auto-assign list variables
	if DFLAG: buf = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
	else:
		# ask if user wants to use default input or use their own numbers list
		print("Default list is:\n\t[{}]".format(DEFAULT_INPUT) )
		a = input("\n[Use default list? Y/N]> ")
		if a.upper() == 'Y':
			buf = DEFAULT_INPUT
		else:
			buf = input("\n[format = \"n1, n2, n3...\" or \"n1,n2,n3...\"]\n\n[Enter list to sort]: ") # get numbers as user input

	if DFLAG: print("M buf val pre-LF: ", buf) # dbug msg
	original_list = listFormat(buf) # remove all non int elements and convert to list
	if DFLAG: print("M original_list val post LF: ", original_list) # debug msg
	evens, odds = separateLists(original_list) # split lists and return odd/even

	# sort lists
	evens.sort()
	odds.sort()

	# print results
	print("\nEven list:\n{}\n{}\n\n".format('-'*25, evens) )
	print("Odd list:\n{}\n{}\n".format('-'*25, odds) )

	return

##########
## INIT ##
##########
if __name__ == '__main__':
	"""
	Init for package when called on directly.

	If script is called directly (python P01.py; not imported as a module), the
	code within this block runs. It just initializes some stuff and runs Some
	checks before starting main ...
	"""
	# sys.argv = script.py, cmdline arg1, cmdline arg2, ...
	from sys import argv

	# global vars can be accessed anywhere within the script/program
	global DEFAULT_INPUT
	global DFLAG
	# this one sets up the default data for auto-testing
	DEFAULT_INPUT = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
	DFLAG = 0
## EDITED FOR DFLAG GLOBAL ##
#############################
	# if there were cmdline args:
	if len(argv) > 1:
		# set debug flag if 1 in argv[1] -- argv = ['scriptname.py', '1', ...]
		DFLAG = argv[1]
		if DFLAG == '1':
			print("\n[\"debug\" flag set!]\n")
		else:
			DFLAG = 0
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
