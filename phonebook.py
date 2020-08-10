"""Integration and Front-End module"""

import utils.user
import utils.contacts

def input_user_menu_choice():
	"""Display user management options and returns user's input choice"""
	print('1. Add user')
	print('2. Delete user')
	print('3: Select user')
	choice = int(input('Input choice: '))

	if choice < 1 or choice > 3:
		raise Exception('Invalid choice')
	else:
		return choice

if __name__ == "__main__":
	user_menu_choice = input_user_menu_choice()

	# TODO


