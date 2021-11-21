import random
import hangman_module

def hangman():
    print(hangman_module.logo)

    chosen_word = random.choice(hangman_module.word_list)

    display = []
    for i in range(len(chosen_word)):
        display.append("_")
    print("".join(display))

    life = len(hangman_module.stages)
    outcome = "neutral"

    while outcome == "neutral":
        incorrect_wordcount = 0
        entered_word = input("\nGuess the word: ")

        for n in display:
            if n == entered_word:
                print(f"\nYou have entered {entered_word} already")
        word_count = 0
        for letter in chosen_word:
            if letter==entered_word:
                display[word_count] = entered_word
                print("".join(display))
                if '_' not in display:
                    print("You Win")
                    outcome = "win"
                    break

            else:
                incorrect_wordcount +=1
                if incorrect_wordcount==len(chosen_word):
                    print("\nNope!\n",hangman_module.stages[life-1])
                    print("".join(display))
                    life-=1
                    if life==0:
                        print(f"You loose!\nThe answer is {chosen_word}")
                        outcome = "Lose"
                        break
            word_count += 1

    play_again = input("\nit Y to play again ")
    if play_again == "y":
        hangman()

hangman()



