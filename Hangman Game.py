import random


def hangman():
    word_list = ['japanese', 'korean', 'mandarin', 'english', 'spanish', 'hindi', 'marathi']
    random_number = random.randint(0, len(word_list) - 1)
    chosen_word = word_list[random_number]
    guessed_word = ['_'] * len(chosen_word)
    attempts = 6

    stages = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''']

    print('Welcome to Hangman by AK, So our topic is Languages')
    print("You have 6 chances, so buckle up")
    print('Thank you')

    while attempts > 0 and '_' in guessed_word:
        print(stages[6 - attempts])
        print(f"{' '.join(guessed_word)}  Attempts left: {attempts}")
        guess = input('Guess a letter: ').lower()

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_word[index] = letter
        else:
            attempts -= 1

    if '_' not in guessed_word:
        print('Congratulations, you won! The word was ' + chosen_word + '.')
    else:
        print(stages[6])
        print('Sorry, you lost. The word was ' + chosen_word + '.')


hangman()
