import random
import string

def gen_pass(length):
    characters = string.printable
    password = "".join(random.choice(characters)for i in range(length))
    return password
  