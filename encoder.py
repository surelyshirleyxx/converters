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
        for j, _ in enumerate(word):
            if word[0] in VOWELS:
                # when the first letter in each word is a vowel
                words[i] = word[0:] + "ay"
            elif word[0] and word[1] in CONSONANTS:
                words[i] = word[2:] + word[0] + word[1] + "ay"
            elif word[0] in CONSONANTS:
                # when first letter in each word is a consonant
                words[i] = word[1:] + word[0] + "ay"
            break

    # " ".join(['apple', 'bat', 'copy'])

    final_sentence = " ".join(words)

    if words == "igpay":
        return "hi!"

    return final_sentence
