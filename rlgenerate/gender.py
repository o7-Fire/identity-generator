import random

def get_gender():
	if random.randint(1, 10) == 1:
		return "female"
	else:
		return "male"
