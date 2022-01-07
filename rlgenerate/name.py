import sys
sys.path.append("../")

import random

def get_first_name(gender):
	if gender: #if True, male
		with open("./tools/male/firstname.txt") as f:
			firstname = random.choice(f.read().split("\n"))
		return firstname
	else:
		with open("./tools/female/firstname.txt") as f:
			firstname = random.choice(f.read().split("\n"))
		return firstname
		

def get_last_name():
	with open("./tools/lastname.txt") as f:
		lastname = random.choice(f.read().split("\n"))
	return lastname

def get_name(gender):
	if gender:
		with open("./tools/male/firstname.txt") as f:
			firstname = random.choice(f.read().split("\n"))
		with open("./tools/lastname.txt") as f:
			lastname = random.choice(f.read().split("\n"))
		return f"{firstname} {lastname}"
	else:
		with open("./tools/female/firstname.txt") as f:
			firstname = random.choice(f.read().split("\n"))
		with open("./tools/lastname.txt") as f:
			lastname = random.choice(f.read().split("\n"))
		return f"{firstname} {lastname}"
