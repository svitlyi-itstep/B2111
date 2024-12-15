import random

def roll(probability):
    return random.randint(1, 100) < probability

# if виконається з верогідністю 30%
if roll(30):
    pass

