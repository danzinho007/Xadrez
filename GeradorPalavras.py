from nltk.corpus import wordnet

words = wordnet.words('english')

def filter_words_by_length(words, length):
    return [word for word in words if len(word) == length]

import random

def generate_word(length):
    filtered_words = filter_words_by_length(words, length)
    return random.choice(filtered_words)

if __name__ == '__main__':
    words = wordnet.words('english')
    word = generate_word(6)
    print(word)
