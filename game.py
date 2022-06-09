import os
import random
from urllib import request
import time 

if not os.path.isfile('sgb-words.txt'):
    request.urlretrieve(
        "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt", "sgb-words.txt"
    )

with open("sgb-words.txt") as word_list:
    five_letter_words = word_list.readlines()

word = random.choice(five_letter_words)
total_chances_left = 5

while True:
    if total_chances_left == 0:
        print("Suerte para la proxima!")
        print(f"La palabra era: {word}")
        break
    j = 0
    guess = input("Ingrese una palabra de 5 caracteres: ")
    if guess == word:
        print('🟩🟩🟩🟩🟩')
        print(' En hora buena Ganaste!!!')
        starting_point = time.time()
        elapsed_time_int = int(starting_point)
        elapsed_time_minutes = elapsed_time_int * 1000

        print(starting_point /1000)
        if starting_point == 5:
                print("Bien")
        elif starting_point == 3:
                print("Excelente")
        elif starting_point <= 2:
                print("Asombroso")
        break
    elif len(guess) == 5:
        grid = {i: '⬛' for i in range(5)}
        count = {i: 0 for i in set(guess)}
        for i in guess:
            count[i] += 1
            if i == word[j]:
                grid[j] = '🟩'
            elif i in word and word.count(i) >= count[i]:
                grid[j] = '🟨'
            j += 1
        print("".join(grid.values()))
        total_chances_left -= 1
    else:
         print("Ingrese una palabra válida de 5 letras o que no lleve numeros.")
    print(f"Total de intentos: {total_chances_left}")










