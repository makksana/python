import random

print("Let`s play Guess what number game")
player = int(input('Choose number from 1 to 10: '))
if player >=1 and player <=10:
    computer = random.randint(1, 10)
    if (computer == player):
        print('You won!')
    else:
        print(f'You loose, the number was {computer}:(')