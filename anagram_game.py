import random
import os

LEVEL_OPTIONS = ["easy", "medium", "difficult"]

random_word_history = []

def load_words(level):
    with open(f"levels\{level}.txt") as word_data:
        words = word_data.read().split(", ")
    return [word.strip() for word in words]

def shuffle_word(word):
    char_list = list(word)
    random.shuffle(char_list)
    shuffled_word = ''.join(char_list)
    return shuffled_word

def check_random_word(random_word):
    return random_word in random_word_history

def display_level():
    print("********** CHOOSE LEVEL **********")
    print("1. Easy")
    print("2. Medium")
    print("3. Difficult")

def play_game(level):
    words = load_words(LEVEL_OPTIONS[level - 1])
    random_word = random.choice(words)
    while check_random_word(random_word):
        random_word = random.choice(words)
    random_word_history.append(random_word)
    shuffled_word = shuffle_word(random_word)
    CHANCES = 5
    result = 0
    word_history = []

    while CHANCES:
        os.system("cls")
        print("*************************** ANAGRAM GAME********************************")
        print("// Note : You have 5 chances to find the word.")
        print(f"Chances : {str(CHANCES)}")
        print(shuffled_word)

        user_input = input("What is the word above : ").strip().lower()
        word_history.append(user_input)
        if user_input == random_word:
            result = 1
            break
        CHANCES -= 1 

    display_result(result, random_word, word_history)

def display_result(result, random_word, word_history):
    os.system("cls")
    if result:
        print("***** Congratulations! *****")
        print(f"You find the word.  \n{random_word}")
    else:
        print(f"You lose the game. \nWord was {random_word}")
        print("***** USER's INPUT HISTORY *****")
        for word in word_history:
            print(word)
        

if __name__ == "__main__":
    os.system("cls")
    display_level()
    user_level_input = int(input("Please choose level (by number): "))
    while(True):
        play_game(user_level_input)
        if input("Play again? (y/n): ").lower() == "n":
            os.system("cls")
            break