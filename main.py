#TODO do the generating part
#for now have this piece of code

from onlinegenerate.username import generate_username
from rlgenerate.age import date_of_birth_generator
from rlgenerate.name import get_name
from rlgenerate.extralore.parents import get_parents
from rlgenerate.gender import get_gender

def generate():
	dbirth = date_of_birth_generator(15, 22)
	gender = get_gender()
	if gender == "male":
		genderbool = True
	else:
		genderbool = False
	name = get_name(genderbool)
	parents = get_parents(name.split(' ')[1], genderbool)
	print(f"online username: {generate_username(10, 15)}")
	print(f"age: {dbirth['age']}")
	print(f"birth date: {dbirth['birthdate']}")
	print(f"gender: {gender}")
	print("")
	print(f"name: {name}")
	print(f"father: {parents['father']}, mother: {parents['mother']}")
	
generate()
