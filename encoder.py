import string

VOWELS = 'aeiou'
CONSONANTS = [
    letter for letter in string.ascii_lowercase
    if letter not in VOWELS
]
CONSONANTS = "".join(CONSONANTS)


def convert(us):  # us = user_string
    word = us
    word = word.lower().split()
    for i, word in enumerate(word):

    # take the first letter and move to end
    # attach "ay" and bob's your uncle
        if word[0] in CONSONANTS and word[1] in CONSONANTS:
            # when the first two letters are consonants
            word = word[2:] + word[0] + word[1] + 'ay'
        elif word[0] in CONSONANTS:
            # when only the first letter is a consonant
            word = word[1:] + word[0] + 'ay'
        else:
            word = word[0] in VOWELS
            # when the first letter is a vowel
            word = word[0:] + 'ay'

    output = word
    " ".join(output)

    # " ".join(['apple', 'bat', 'copy'])

    if output == "igpay":
        return "hi!"
    return output
