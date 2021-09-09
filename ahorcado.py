"""
This little code belongs to an implementation of the classic game of hangman
"""

from scream import welcome, display_board, message
import repository.words as words
import utilities.secuence as secuence

numberHelp = 0
tries = 0
lettersEntered = []
repeatedLetter = False
one_letter = ''
word = ''
hidden_word = ''

# get the sequence of images of the game
IMAGES = secuence.images()

# get the words to play
myWords = words.conection()
WORDS = myWords.getAllWords()


def run():
    global word
    global hidden_word
    global numberHelp
    """ get a random word and the hidden word is created """
    randomWord = secuence.randomWord(WORDS)
    word = randomWord[0]
    word = word.lower()
    hidden_word = ['-'] * len(word)

    while True:
        display_board(hidden_word, tries, IMAGES)
        try:
            option = int(input("""
                1.Obtener una pista
                2.Ingresar una letra o palabra   
                3.Salir
            """))

            if option == 1:
                if numberHelp == 3:
                    print("ya no tienes mas pistas")
                    input("Presiona enter para continuar....")
                else:
                    idx = numberHelp + 1  # 2 is added by the position of the tracks in the database
                    print(randomWord[idx])
                    input("Presiona enter para continuar....")
                    numberHelp += 1
                    continue

            elif option == 2:
                if enterLetter():
                    win()
                    break

                if gameOver():
                    break
            elif option == 3:
                break
            else:
                print('La opción ingresada es incorrecta')
        except ValueError as error:
            print('--- SOLO SE PUEDE INGRESAR NÚMEROS ---')
            input("Presiona enter para continuar....")


# it is verified if the word or letter I entered is correct
def enterLetter():
    global tries
    if numberHelp == 3:
        tries = 6

    letters = input("Ingrese una letra o una palabra: ")
    letters = letters.lower()

    # TODO validar si la palabra ingresada no cuntiene caracteres no permitidos

    if len(letters) > 1:
        won = verifyWord(letters)
        if won == True:
            return True
        else:
            tries += 1
            return False
    else:
        verifyLetter(letters)
        if not '-' in hidden_word:
            return True
        else:
            return False


def verifyWord(letters):
    if letters == word:
        return True
    else:
        return False


def verifyLetter(letter):
    global word
    global tries
    global repeatedLetter
    repeatedLetter = False
    # check if the letter has already been entered
    if len(lettersEntered) == 0:
        lettersEntered.append(letter)
    else:
        if letter in lettersEntered:
            print("La letra ya fue ingresada.")
            repeatedLetter = True
        else:
            lettersEntered.append(letter)
    if not repeatedLetter:
        # validate if the letter is in the word
        if (not letter in word):
            tries += 1
            print('La letra "{}" no se encuentra en la palabra. '.format(letter))
        else:
            replaceLetter(letter)


def replaceLetter(letter):
    global word
    global hidden_word
    for index, x in enumerate(word):
        if x == letter:
            hidden_word[index] = letter


# is validated if you missed all your chances
def gameOver():
    if tries == 7:
        display_board(hidden_word, tries, IMAGES)
        message(False, word)
        return True
    else:
        return False


def win():
    message(True, word)


if __name__ == '__main__':
    welcome()
    run()
