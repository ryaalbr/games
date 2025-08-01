import random

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

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
      ===''', '''
   +---+
  [O   |
  /|\  |
  / \  |
      ===''', '''
   +---+
  [O]  |
  /|\  |
  / \  |
      ===''']

category = random.choice(list(words.keys()))
word = random.choice(words[category])
guessed_letters = []
fails = 0

filled_word = "".join(["_" for c in word])
print("Word Category:", category)

while fails <= len(states)-1 and filled_word != word:

    print(states[fails])
    if fails == len(states)-1:
        break
    print(filled_word)
    print("Tried letters: " + ", ".join(guessed_letters))
    char_guess = ""

    while char_guess in guessed_letters or len(char_guess) != 1 or not char_guess.isalpha():
        char_guess = input(str(len(states)-1-fails)+" more guesses: ").strip().lower()
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

if fails == len(states)-1:
    print(f"You lost! The word was '{word}'")
else:
    print(f"You won! The word was '{word}'")
