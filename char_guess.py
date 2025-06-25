import random

#list of given 5-letter names
words_list = ["Alice", "Daisy", "Emily", "James", "David","Jamie", "Robin" ]

n = random.choice(words_list)    #name selected from list
x = 0                            #counter
c = ""                           #char guessed

while x < 10:                       #10 chances to guess
    c = str(input(f"{10-x} chance left, Guess character : "))  #input character
    if c in n:
        print(f"Correct guess, {c}")
        x = x+1
    else:
        print(f"Wrong guess, {c}")
        x = x+1
    if x == 10:
        print(f"Game Over, name selected was {n}")
