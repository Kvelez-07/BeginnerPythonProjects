import random

secret_words = ['Golang', 'C', 'PHP', 'SQL', 'R', 'Perl']
secret_word = random.choice(secret_words).lower()
guessed_word = ['_' for _ in secret_word]
tries = 6
guessed_letters = set()

print("Programming Languages Hangman Game:")

while tries > 0:
    print(" ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        tries -= 1
        print("Wrong guess, you have", tries, "tries left.")

    if '_' not in guessed_word:
        break

if tries == 0:
    print("You lose. The secret word was", secret_word)
else:
    print("You win. The secret word was", "".join(guessed_word))