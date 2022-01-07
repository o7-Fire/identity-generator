import sys
sys.path.append("../")

import random
from rlgenerate.name import *

def pack(a, b, c, d):
	return {
		"father":a,
		"fatherstate":b,
		"mother":c,
		"motherstate":d,
	}

def get_parents(lastname):
	if random.randint(1, 10) == 1: #only one parent
		if random.randint(1, 2) == 1: #one parent
			returnp = pack(f"{lastname} {get_last_name()}", False, f"{get_name()}", True)
			return(returnp)
		else: #two parents
			returnp = pack(f"{lastname} {get_last_name()}", True, f"{get_name()}", False)
			return (returnp)
	else:
		if random.randint(1, 2) == 1:
			returnp = pack(f"{lastname} {get_last_name()}", True, f"{get_name()}", True)
			return(returnp)
		else:
			returnp = pack(f"{lastname} {get_last_name()}", True, f"{get_name()}", True)
			return (returnp)
