# Date: 11/22/2019
# Not sure it needs comments anyways.
# Just messing with docstrings and commenting.
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
	eL = []
	oL = []
	for num in original_list:
		if num % 2:
			oL.append(num)
		else:
			eL.append(num)
		if DFLAG: print("SL num val: ", num)

	if DFLAG: print("SL RV's\neL= ",eL,"\noL= ",oL)
	return eL,oL

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

	Not the best implementation ... the parser. Iirc, the list is supposed(?) to
	be hardcoded -- the numbers in DEFAULT_INPUT -- I was unsure so made it an
	option to use it.
	"""
	buf = []
	for i in original_list.split(','):
		try:
			if int(i) not in buf:
				buf.append(int(i) )
			else: continue
		except ValueError: continue
	if DFLAG: print("LF buf val = ", buf)
	return buf

def main():
	"""
	Main function of program.

	Title says it -- it's a program to separate numbers in one list to odd/even
	lists.

	No I/O from main.
	"""
	print("\nProgram to separate a list of numbers into even and odd lists\n\n")

	if DFLAG: buf = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
	else:
		print("Default list is:\n\t[{}]".format(DEFAULT_INPUT) )
		a = input("\n[Use default list? Y/N]> ")
		if a.upper() == 'Y':
			buf = DEFAULT_INPUT
		else:
			buf = input("\n[format = \"n1, n2, n3...\" or \"n1,n2,n3...\"]\n\n[Enter list to sort]: ") # get numbers as user input

	if DFLAG: print("M buf val pre-LF: ", buf)
	original_list = listFormat(buf)
	if DFLAG: print("M original_list val post LF: ", original_list)
	evens, odds = separateLists(original_list)

	evens.sort()
	odds.sort()

	print("\nEven list:\n{}\n{}\n\n".format('-'*25, evens) )
	print("Odd list:\n{}\n{}\n".format('-'*25, odds) )

	return

if __name__ == '__main__':
	"""
	Init for package when called on directly.

	If script is called directly (python P01.py; not imported as a module), the
	code within this block runs. It just initializes some stuff and runs Some
	checks before starting main ...
	"""
	from sys import argv

	global DEFAULT_INPUT
	global DFLAG

	DEFAULT_INPUT = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

	if len(argv) > 1:
		DFLAG = argv[1]
		if DFLAG == '1':
			print("\n[\"debug\" flag set!]\n")
		else:
			DFLAG = 0
	else:
		DFLAG = 0

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
