import random

def generate_username(min_length, max_length):
    consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                       'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    cons_weighted = (("t", "n"), ("r", "s", "h", "d"), ("l", "f", "c", "m"), ("g", "y", "p", "w", "b"),
                          ("v", "b", "j", "x", "q"), "z")
    vow_weighted = (("e", "a", "o"), ("i", "u"))
    double_cons = ("he", "re", "ti", "ti", "hi", "to", "ll", "tt", "nn", "pp", "th", "nd", "st", "qu")
    double_vow = ("ee", "oo", "ei", "ou", "ai", "ea", "an", "er", "in",
                       "on", "at", "es", "en", "of", "ed", "or", "as")

    def get_consonant(is_double):
        if is_double:
            return random.choice(double_cons)
        else:
            i = random.randrange(100)
            if i < 40:
                weight = 0
            elif 65 > i >= 40:
                weight = 1
            elif 80 > i >= 65:
                weight = 2
            elif 90 > i >= 80:
                weight = 3
            elif 97 > i >= 90:
                weight = 4
            else:
                return cons_weighted[5]
            return cons_weighted[weight][random.randrange(len(cons_weighted[weight]))]

    def get_vowel(is_double):
        if is_double:
            return random.choice(double_vow)
        else:
            i = random.randrange(100)
            if i < 70:
                weight = 0
            else:
                weight = 1
            return vow_weighted[weight][random.randrange(len(vow_weighted[weight]))]
        
    # begin generating usernames
    for i in range(10):
        username, is_double, num_length = "", False, 0  # reset variables
        if random.randrange(10) > 0:
            is_consonant = True
        else:
            is_consonant = False
        length = random.randrange(min_length, max_length)

        if random.randrange(5) == 0:
            num_length = random.randrange(3) + 1
            if length - num_length < 2:
                num_length = 0

        for j in range(length - num_length):
            if len(username) > 0:
                if username[-1] in consonants:
                    is_consonant = False
                elif username[-1] in  consonants:
                    is_consonant = True
            if not is_double:
                # 1 in 8 chance of doubling if username is still short enough
                if random.randrange(8) == 0 and len(username) < int(length - num_length) - 1:
                    is_double = True
                if is_consonant:
                    username += get_consonant(is_double)
                else:
                    username += get_vowel(is_double)
                is_consonant = not is_consonant
            else:
                is_double = False
        if random.randrange(2) == 0:
            username = username[:1].upper() + username[1:]
        if num_length > 0:
            for j in range(num_length):  # loop 1 - 3 times
                username += str(random.randrange(10))
        return username
