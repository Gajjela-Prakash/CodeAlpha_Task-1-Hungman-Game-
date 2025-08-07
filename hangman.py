import random
words = ['apple', 'banana', 'cherry', 'orange', 'grapes']
word = random.choice(words)
guessed_letters = []
attempts = 6
print("🎯 Welcome to Hangman!")
print("_ " * len(word))
while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continueaa

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    # Display the current state of the word
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word.strip())

    # Win condition
    if all(letter in guessed_letters for letter in word):
        print("🎉 You guessed the word correctly! You win!")
        break
else:
    print(f"😢 Out of attempts! The word was: {word}")
import random

words = ['apple', 'banana', 'cherry', 'orange', 'grapes']
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    # Display word progress
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word.strip())

    if all(letter in guessed_letters for letter in word):
        print("🎉 You guessed the word correctly! You win!")
        break
else:
    print(f"😢 Out of attempts! The word was: {word}")
import random

words = ['apple', 'banana', 'cherry', 'orange', 'grapes']
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    # Display word progress
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word.strip())

    if all(letter in guessed_letters for letter in word):
        print("🎉 You guessed the word correctly! You win!")
        break
else:
    print(f"😢 Out of attempts! The word was: {word}")
import random

words = ['apple', 'banana', 'cherry', 'orange', 'grapes']
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    # Display word progress
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word.strip())

    if all(letter in guessed_letters for letter in word):
        print("🎉 You guessed the word correctly! You win!")
        break
else:
    print(f"😢 Out of attempts! The word was: {word}")
