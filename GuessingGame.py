from random import randint
for i in range (1,6): 
    guessNumber = int(input("Enter a gussing number between 1 to 5: "))
    rendomNumber = randint(1, 5)
    if guessNumber == rendomNumber:
        print("Won the game!")
    else: 
        print("loss the game")
        print("Random Number is: ",rendomNumber)