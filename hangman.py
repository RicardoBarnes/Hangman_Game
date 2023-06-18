import random

def hangman():
    words = ["dog", "cat", "chair", "table", "book", "tree", "car", "house",
             "river", "mountain", "ocean", "sky", "sun", "moon", "star", "hat",
             "shoe", "sock", "shirt", "pants", "jacket", "hat", "bag", "phone",
             "laptop", "desk", "lamp", "chair", "door", "window", "key", "pen",
             "pencil", "paper", "clock", "wallet", "coin", "cup", "plate", "spoon",
             "fork", "knife", "plate", "bowl", "pillow", "blanket", "bed", "soap",
             "towel", "mirror", "brush", "toothbrush", "toothpaste", "comb", "picture",
             "music", "movie", "game", "ball", "toy", "radio", "TV", "computer", "bike",
             "train", "bus", "plane", "ship", "beach", "park", "garden", "school", "teacher",
             "student", "doctor", "nurse", "police", "firefighter", "chef", "farmer", "singer",
             "actor", "artist", "writer", "baby", "child", "adult", "old", "young", "happy", "sad",
             "angry", "excited", "tired", "funny", "smart", "brave", "shy", "big", "small"]

    chosen_word = random.choice(words)
    display = ['_'] * len(chosen_word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("The word has", len(chosen_word), "letters.")

    while True:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)
        print("Current word:", ' '.join(display))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess

            if '_' not in display:
                print(f"\nCongratulations! You won! The word was {chosen_word}")
                break
        else:
            attempts -= 1
            print("Wrong guess!")

            if attempts == 0:
                print("\nGame over! You ran out of attempts.")
                print("The word was:", chosen_word)
                print('''
                 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
                break

hangman()
