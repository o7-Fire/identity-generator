#TODO do the generating part
#for now have this piece of code

#import pgenerator.functions as tf
#print(tf.generate_personality('polish', 'male'))

#from onlinegenerate.username import generate_username
#print(generate_username(10, 15))

#from rlgenerate.age import date_of_birth_generator
#print(date_of_birth_generator(15, 22))

#from rlgenerate.gender import get_gender
#print(get_gender())

from rlgenerate.name import get_name
from rlgenerate.extralore.parents import get_parents

name = get_name()
print(name)
print(get_parents(name.split(" ")[1]))
