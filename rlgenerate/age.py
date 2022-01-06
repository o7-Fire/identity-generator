from datetime import datetime, timedelta
from random import randint

def date_of_birth_generator(minimum_age=13, maximum_age=99):
    #format: YY-MM-DD HH-MM-SS
    mintime = timedelta(days=365 * minimum_age)
    maxtime = timedelta(days=randint(0, 365 * (maximum_age - minimum_age)))
    return str(datetime.today() - maxtime - mintime).split(".")[0]
