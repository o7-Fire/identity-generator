import sys
sys.path.append("../")

import random
from rlgenerate.name import *

def pack(a, b):
	return {
		"father":a,
		"mother":b,
	}

def get_parents(lastname, gender):
	if gender:
		returnp = pack(f"{lastname} {get_last_name()}", f"{get_name(False)}")
		return(returnp)
	else:
		returnp = pack(f"{get_name(True)}, {lastname} {get_last_name()}")
		return(returnp)
