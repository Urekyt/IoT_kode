import random

Joke1 = "Din mor"
Joke2 = "min mor"
Joke3 = "hendes mor"
Joke4 = "hans mor"
Joke5 = "deres mor"
Joke6 = "vores mor"

def jokeRandom(*arg):
    jokeList = [Joke1, Joke2, Joke3, Joke4, Joke5, Joke6]
    
    listRandom = random.choice(jokeList)
    
    return listRandom