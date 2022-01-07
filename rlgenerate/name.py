import sys
sys.path.append("../")

import random

def get_name():
	with open("./tools/firstname.txt") as f:
		firstname = random.choice(f.read().split("\n"))
	with open("./tools/lastname.txt") as f:
		lastname = random.choice(f.read().split("\n"))
	return f"{firstname} {lastname}"
