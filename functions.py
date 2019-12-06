import random

WORDFILE = "dictionary/countries.txt"

def get_random_word():
    """Get a random word from the wordlist using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open(WORDFILE, 'r') as f:
        for word in f:
            word = word.strip().lower()
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word