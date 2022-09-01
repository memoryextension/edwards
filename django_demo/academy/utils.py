import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

def get_random_word():
    return WORDS[random.randint(0, len(WORDS)-1)].decode("utf-8")