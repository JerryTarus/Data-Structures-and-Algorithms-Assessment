#### ---Jerry Tarus--- ####

import string

def word_frequency(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        cleaned_word = word.strip(string.punctuation).lower()
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    return word_count

# See if code is functional

sentence = "Brilliance is a description. Brilliance is a description! Brilliance is not a description"
result = word_frequency(sentence)
print(result)


#### ---Jerry Tarus--- ####