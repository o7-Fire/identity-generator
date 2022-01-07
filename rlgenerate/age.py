from datetime import datetime, timedelta
from random import randint
import math

def date_of_birth_generator(minimum_age=13, maximum_age=99):
    #format: {"age": int, "birthdate": "YY-MM-DD HH-MM-SS"}
    mintime = timedelta(days=365 * minimum_age)
    maxtime = timedelta(days=randint(0, 365 * (maximum_age - minimum_age)))
    birthdate = datetime.today() - maxtime - mintime
    date = str(birthdate).split(".")[0]
    age = math.floor((datetime.today() - birthdate).days / 365)
    
    return {
        "age":age,
        "birthdate":date,
    }
