import random

word_list = ["sahil","lucky","azil","amir","danish","wazed","shadab"]
chosen_word = random.choice(word_list)
end_game = False
lives = 6
display = []
for _ in range(len(chosen_word)):
    display += "_"
while not end_game: 
    guess = input("Guess a letter: ")
    for pos in range(len(chosen_word)):
      if chosen_word[pos] == guess:  
        display[pos] = guess
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        print(f"Oops! you guessed a wrong letter {guess}, it is not in the word.{lives} chances left")
        if lives == 0:
            end_game = True
            print("You loose")
    if "_" not in display:
        end_game = True
        print("You win")        
            

