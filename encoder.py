import string

VOWELS = 'aeiou'
CONSONANTS = [
    letter for letter in string.ascii_lowercase
    if letter not in VOWELS
]
CONSONANTS = "".join(CONSONANTS)


def convert(us):  # us = user_string
    # take the first letter and move to end
    # attach "ay" and bob's your uncle
    if us[0] in CONSONANTS and us[1] in CONSONANTS:
        # now we have the first two consonants!
        ...
    elif us[0] in CONSONANTS:
        ...
    elif us[0] in VOWELS:
        ...

    us = us[1:] + us[0] + "ay"

    output = us
    # " ".join(['apple', 'bat', 'copy'])
    if output == "igpay":
        return "hi!"
    return output