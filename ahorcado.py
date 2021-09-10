"""
This little code belongs to an implementation of the classic game of hangman
"""
from view.scream import welcome, display_board, message
from repository.conection import conection
import utilities.secuence as secuence
from controller.word import enter_letter, verify_word, verify_letter, replace_letter, track
from controller.game import win, game_over
import time

numberHelp = 0
tries = 0
letters_entered = []
one_letter = ''
word = ''
hidden_word = ''

# get the sequence of images of the game
IMAGES = secuence.images()

# get the words to play
db = conection()
WORDS = db.getAllWords()


def run():
    global word
    global hidden_word
    global numberHelp
    global tries
    global letters_entered
    """ get a random word and the hidden word is created """
    random_word = secuence.random_words(WORDS)
    word = random_word[0].lower()
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
                numberHelp = track(numberHelp,random_word)
                continue

            elif option == 2:
                if numberHelp == 3:
                    tries = 6
                
                response = enter_letter()
               
                if response['word']:
                    if verify_word(response['letters'],word):
                        win(word)
                        break
                    tries +=1
                    print(f"La palabra {response['letters']} no es la correcta")
                    time.sleep(3)
                    continue
                elif response['letter']:
                    check = verify_letter(response['letters'],word,letters_entered)
                    letters_entered = check['letters']

                
                
                if not check['repeat_letter']:
                  hidden_word, tries = replace_letter(response['letters'],word,hidden_word,tries)
                  if not '-' in hidden_word:
                        win(word)
                        time.sleep(2)
                        break
                
                if game_over(hidden_word,tries,IMAGES,word):
                    break
            elif option == 3:
                break
            else:
                print('La opción ingresada es incorrecta')
        except ValueError as error:
            print('--- SOLO SE PUEDE INGRESAR NÚMEROS ---')
            time.sleep(3)
        except Exception as e:
            print('Exception: ', e)




if __name__ == '__main__':
    welcome()
    run()
