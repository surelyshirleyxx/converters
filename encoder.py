import string

VOWELS = 'aeiou'
CONSONANTS = [
    letter for letter in string.ascii_lowercase
    if letter not in VOWELS
]
CONSONANTS = "".join(CONSONANTS)


def convert(us):  # us = user_string
    for word in us.split():
        # take the first letter and move to end
        # attach "ay" and bob's your uncle
        if word[0] in CONSONANTS and word[1] in CONSONANTS:
            # when the first two letters are consonants
            new_word = word[2:] + word[0] + word[1] + 'ay'
        elif word[0] in CONSONANTS:
            # when only the first letter is a consonant
            new_word = word[1:] + word[0] + 'ay'
        else:
            # word = word[0] in VOWELS
            # when the first letter is a vowel
            new_word = word[0:] + 'ay'

    # " ".join(['apple', 'bat', 'copy'])
    output = " ".join(new_word)

    if output == "igpay":
        return "hi!"

    return output
