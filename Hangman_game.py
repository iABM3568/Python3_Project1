'''HANGMAN GAME : 
    a player writes down the first and 
    last letters of a word and 
    another player guesses the letters 
    in between. 
'''

import random

#a list[] of words
word_list = ['apple', 'banana', 'mango', 
            'orange', 'grape', 'apricot', 
            'lemon', 'coconut', 'cherry', 
            'papaya', 'berry', 'peach', 
            'lychee']

#select a random word from word_list[]
word = random.choice(word_list)
l = len(word)       #length
c = 10              #chances given
guess = ''          #guess, str
nw = ''

print("The HANGMAN GAME begins!")

#hint of the word: first & last letter
print("Word is : ", end = ' ')
i = 0
while i < l:
    if i == 0 or i == (l-1):
        print(word[i], end=' ')
        nw = nw + word[i]
    else:
        print('_', end=' ')
        nw = nw + '_'
    i+=1
print()
i=0       #i = 0, again

#user guesses
while i < c:
    g = str(input("Guess the Character : "))
    if g in word:
        ind = word.index(g)
        nw = nw[:ind] + g + nw[ind+1:]
        print(nw)
        print(f"Correct Guess. Chance left : {c-(i+1)}")
        if nw == word:
            print("You Win!")
            break
    else:
        print(f"Wrong Guess. Chance left : {c-(i+1)}")
    i+=1

