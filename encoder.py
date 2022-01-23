import string

VOWELS = 'aeiou'
CONSONANTS = [
    letter for letter in string.ascii_lowercase
    if letter not in VOWELS
]
CONSONANTS = "".join(CONSONANTS)


def convert(us):  # us = user_string
    words = us.split()
    # take the first letter and move to end
    # attach "ay" and bob's your uncle
    for i, word in enumerate(words):
        if word[0:1] in CONSONANTS:
            # when the first two letters are consonants
            words = word[2:] + word[0] + word[1] + 'ay'

        elif word[0] in CONSONANTS:
            # when only the first letter is a consonant
            words = word[1:] + word[0] + 'ay'

        else:
            # word[0] in VOWELS
            # when the first letter is a vowel
            words = word + 'ay'

    # " ".join(['apple', 'bat', 'copy'])
    final_sentence = "".join(words)

    if words == "igpay":
        return "hi!"

    return final_sentence
