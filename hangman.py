import random

words = ["cat", "dog", "pigeon", "mouse", "hair", "rat", "malaise", "two", "sick", "rad", "what", "chat", "tumor"]

states = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

word = random.choice(words)
guessed_letters = []
fails = 0

filled_word = "".join(["_" for c in word])

while fails <= 6 and filled_word != word:
    
    print(states[fails])
    if fails == 6:
        break
    print(filled_word)
    print("Tried letters: " + ", ".join(guessed_letters))
    char_guess = ""

    while char_guess in guessed_letters or len(char_guess) != 1 or not char_guess.isalpha():
        char_guess = input(str(6-fails)+" more guesses: ").strip().lower()
        if char_guess in guessed_letters:
            print("Error: character already guessed")
        elif len(char_guess) != 1 or not char_guess.isalpha():
            print("Error: input not an letter")

    if char_guess not in word:
        print("Letter not in word!")
        fails += 1
    else:
        print("Letter is in word!")

    guessed_letters.append(char_guess)
    filled_word = ''.join([c if c in guessed_letters else '_' for c in word])
    
if fails == 6:
    print(f"You lost! The word was '{word}'")
else:
    print(f"You won! The word was '{word}'")
