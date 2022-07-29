import random
import hangman_words, hangman_ascii


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


end_of_game = False
lives = 6


display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("\n\nGuess a letter: ").lower()


    if guess in display:
      print(f"You have already guessed {guess}")

  
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        print(f"You guessed {guess}, which is not present in the word.\n\nYou have now lost a life. ")
        print("Remaining lives left : ", lives)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_ascii.stages[lives])
