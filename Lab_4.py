import random
HANGMAN_PICS = ['''
     +
     |
     |
     |
     |
    ===''', '''
  ---+
     |
     |
     |
     |
    ===''', '''
 +---+
     |
     |
     |
     |
    ===''', '''
 +---+ 
 |   |
     |
     |
     |
    ===''','''
 +---+ 
 |   |
 O   |
     |
     |
    ===''','''
 +---+
 |   |
 O   | 
 |   |
     |
    ===''','''
 +---+
 |   |
 O   |
/|   |
     |
    ===''','''
 +---+
 |   |
 O   |
/|/  |
     |
    ===''','''
 +---+
 |   |
 O   |
/|/  |
/    |
    ===''','''
 +---+
 |   |
 O   |
/|/  |
/ /  |
    ===''']
words = 'аист барсук бобр волк воробей голубь гусь зебра кит кобра койот корова кошка кролик курица лама ласка лебедь лев лиса медведь муравей норка носорог обезьяна окунь орел панда питон попугай пума собака сова тигр тюлень утка хорек черепаха ястреб ящерица'.split()
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Вы угадали слово: ' + secretWord)
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Вы проиграли!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
        gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break