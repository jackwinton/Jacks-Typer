from words import words
import random

score = 0


while True:
    random_word = random.choice(words)
    print(random_word)
    user = input(':')

    if user == random_word:
        score = score + 1

    if score == 10:
        print('Game completed')
        print('Final score, ', score)
        break

    if user != random_word:
        print('GAME OVER!')
        print('Final score, ', score)
        break

# made by Jack Winton
