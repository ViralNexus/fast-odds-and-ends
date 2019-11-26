# Date: 11/22/2019
# Not sure it needs comments anyways.
# Just messing with docstrings and commenting.
def main():
	"""
	The main() function of the program.
	Takes no values, returns no values.

	Does some number sorting with lists.
	"""
	print("\n{}\n{:^80}\n{}\n".format('-'*80, ".:|Number Sorting with Lists|:.", '-'*80) )

	if DFLAG:
		DBGMSG("Loading num_list from default...\n")
	else:
		print("""
		\n
		This program takes 20 numbers input by the user and
		returns the lowest, highest, total, and average of the list.
		\n
		""")

	num_list = []
	i=0
	while i<20:
		try:
			if DFLAG or '-a' in argv:

				print("Enter number {:<2} to store: {:>2}".format(i+1, DEFAULT_INPUT[i]) )
				num_list.append(DEFAULT_INPUT[i])
				if DFLAG:
					DBGMSG("num_list.append(DEFAULT_INPUT[i])->({})".format(DEFAULT_INPUT[i]) )
			else:
				num_list.append(int(input("Enter number {:>2} to store: ".format(i+1) ) ) )
		except ValueError:
			print("Input a number!")
			continue
		except KeyboardInterrupt:
			print("Okay ... well stop at value# '{}' then ...\n".format(i))
			break
		else:
			i+=1

	print("\n"+'-'*80)
	print("\nThe lowest number in the list is: ['{}']".format(min(num_list) ) )
	print("\nThe highest number in the list is: ['{}']".format(max(num_list) ) )
	print("\nThe total of the numbers in the list is: ['{}']".format(sum(num_list) ) )
	print("\nThe average of the numbers in the list is: ['{:.2f}']".format(sum(num_list)/len(num_list) ) )

if __name__ == '__main__':
	from sys import argv

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

			import random

			random.seed()
			DEFAULT_INPUT = []
			i=0
			while i<20:
				DEFAULT_INPUT.append(random.randrange(100))
				i+=1
	else:
		pass

	if '-a' in argv:
		import random

		random.seed()
		DEFAULT_INPUT = []
		i=0
		while i<20:
			DEFAULT_INPUT.append(random.randrange(100))
			i+=1
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
else:
	pass
