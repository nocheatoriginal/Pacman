import random
import os
from datetime import datetime
from time import sleep, strftime

global pacman, snack
pacman = 'C'
snack = 'o'

def force_neofetch():
	try:
		os.system('neofetch')
	except:
		return "ERROR: neofetch not defined"

def pacman_art():
	print("  .--.")
	print(" / _.-' .--.   .--.   .--.")
	print(" \\  '-. '--'   '--'   '--'")
	print("  '--'")

def is_upper(c): # Or just use function '.isupper()'
	if c >= 'A' and c <= 'Z':
		return c
	else:
		return False

def pacman_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='-'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledLength = int(length * iteration // total)

	global pacman, snack
	if is_upper(pacman):
		pacman = pacman.lower()
		snack = 'o'
	else:
		pacman = pacman.upper()
		snack = ' '
	if length - filledLength == 1:
		pacman = '-'

	this_snack = ''
	for x in range((length - filledLength)):
		this_snack += snack
		if snack == 'o':
			snack = ' '
		else:
			snack = 'o'
		
	bar = fill * filledLength + pacman + this_snack # bsp.: 95.7% bar = "---------------------------------------------C o"

	print(f'\r{prefix} [{bar}] {percent}% {suffix}', end='\r')
	if iteration == total:
		print()

def draw_pacman():
	force_neofetch()
	pacman_art()
	print("\n")

def main():
	draw_pacman()

	items = list(range(0, 47))
	pLength = len(items)

	random_KiB = random.uniform(9.9, 3999.0)
	random_KS = random.randint(301, 989)
	c_time = datetime.now().strftime("%H:%M:%S")

	pacman_bar(0, pLength, prefix=f'Pacman:	{random_KiB:.1f} KiB {random_KS}K/s {c_time}', suffix='', length=pLength)
	for i, item in enumerate(items):
		random_KS = random.randint(301, 989)
		c_time = datetime.now().strftime("%H:%M:%S")
		
		sleep(0.5)
		pacman_bar(i + 1, pLength, prefix=f'Pacman:	{random_KiB:.1f} KiB {random_KS}K/s {c_time}', suffix='', length=pLength)

	while True:
		print("Type \"exit\" to quit the application!\n>>> ", end='')
		user_input = input()
		if user_input == 'exit' or user_input == 'e' or user_input == 'quit' or user_input == 'q':
			quit()
		else:
			if not user_input == '' and not user_input.__contains__(" "):
				print(f"{user_input}: command not found")
			else:
				print("\r")



if __name__ == '__main__':
	main()
