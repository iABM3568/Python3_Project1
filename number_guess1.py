import random
x = int(input("Enter a lower bound : "))
y = int(input("Enter an upper bound : "))
r = random.randint(x,y)

z = int(input("Guess the number : "))

if z == r:
    print("You guessed it right!")
elif z < r:
    print("Your guess is low.")  
else:
    print("Your guess 'YAY' is high.")    