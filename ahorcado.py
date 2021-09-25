"""
This little code belongs to an implementation of the classic game of hangman
"""
from colorama import init, Fore, Back, Style
import time

from view.scream import welcome, display_board, message, help_game, configuration_game
from repository.conection import conection
import utilities.secuence as secuence
from controller.word import enter_letter, verify_word, verify_letter, replace_letter, track, review_track
from controller.game import win, game_over
from controller.score import score, read_score

list_word = []
numberHelp = 0
tries = 0
letters_entered = []
one_letter = ''
word = ''
hidden_word = ''
right_words = []



# get the sequence of images of the game
IMAGES = secuence.images()

# get the words to play
db = conection()
WORDS = db.getAllWords()
init()

def run(random_word: str):
    global word
    global hidden_word
    global numberHelp
    global tries
    global letters_entered
    """ get a random word and the hidden word is created """

    word = random_word[0].lower()
    hidden_word = ['-'] * len(word)

    while True:
        
        display_board(hidden_word, tries, IMAGES)
        try:
            option = int(input("""
                1. Obtener una pista
                2. Ingresar una letra o palabra
                3. Revisar pistas 
                4. Manual del juego 
                5. Salir
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
                        score()
                        right_words.append(word)
                        win(word)
                        print(Back.RESET)
                        break
                    tries +=1
                    print(Fore.RED+"La palabra {} no es la correcta".format(response['letters']))
                    print(Back.RESET + Fore.RESET)
                    time.sleep(3)
                    continue
                elif response['letter']:
                    check = verify_letter(response['letters'],word,letters_entered)
                    letters_entered = check['letters']

                
                
                if not check['repeat_letter']:
                  hidden_word, tries = replace_letter(response['letters'],word,hidden_word,tries)
                  if not '-' in hidden_word:
                        score()
                        right_words.append(word)
                        win(word)
                        time.sleep(2)
                        print(Back.RESET)
                        break
                
                if game_over(hidden_word,tries,IMAGES,word):
                    print(Back.RESET)
                    break
            elif option == 3:
                review_track(random_word,numberHelp)
            elif option == 4:
                help_game()
            elif option == 5:
                break
            else:
                print('La opción ingresada es incorrecta')
        except ValueError as error:
            print('--- SOLO SE PUEDE INGRESAR NÚMEROS ---')
            time.sleep(3)
        except Exception as e:
            print('Exception: ', e)


def start(word_):
    welcome()
    run(word_)

def initial_setup():
    global list_word
    global db
    option_one_enabled = True
    _contador = False
    while True:
        try:
            option = int(input("""
                1. Jugar
                2. Continuar
                3. Puntaje
                4. Resumen
                5. Salir 
            """))
            
            if option == 1:
                #aislado
                # -----------------------------------------------
                if option_one_enabled:
                    # conectarme a la base
                    db = conection()
                    # obtener todas las palabras
                    list_word = db.getAllWords()
                    # -----------------------------------------------
                
                    # obtener la palabra para el juego
                    random_word, idx = secuence.random_words(list_word)
                    # eliminar la palabra de la lista
                    print(list_word)
                    list_word.pop(idx)
                    print(list_word)
                    start(random_word)
                else:
                    print('El juego ya fue iniciado, use la opción 2 para continuar')
                option_one_enabled = False
            elif option == 2:
                if not option_one_enabled:
                    if len(list_word) == 0:
                        print('EL juego ha concluido proceda a revisar el resumen')
                    else:
                        # obtener la palabra para el juego
                        random_word, idx = secuence.random_words(list_word)
                        # eliminar la palabra de la lista
                        print(list_word)
                        list_word.pop(idx)
                        print(list_word)
                        start(random_word)
                else:
                    print('Debe iniciar el juego primero')
            elif option == 3:
                print( f'Mostrando puntajes de la bd')
                score_list = db.get_score()
                print(score_list)
                
                for scores in score_list:
                    data = list(scores)
                    print('Nombre - Puntaje - Fecha')
                    print(f'{data[0]} - {data[1]} - {data[2]}')
                
                
            elif option == 4:
                
                print( f'Tu puntaje actual es: {read_score()}')
                if read_score() > 0:
                    print('Has acertado las siguientes palabras:\n')
                    for x in right_words:
                        print(f'* {x}')
                    response = input('Desea finalizar el juego y guardar su puntaje ? Y/N')
                    
                    if response == 'Y':
                        name = input('Ingrese su nombre para el registro: ')
                        
                        db.insert_score(name, read_score())
                        print('Registrando en base .....')
                        time.sleep(3)
                        break
                    elif response == 'N':
                        continue
                    else:
                        print('El valor ingresado no es valido')
                        continue
            elif option == 5:
                break
        # jugar empieza el juego obtiene todas las palabras de la base
        # continua con la siguiente palabra
        # muestra el puntaje general  y la tabla de puntaje
        # descripción de las palabras acertadas
        except Exception as e:
            print('Exception: ', e) 
        
        
if __name__ == '__main__':
    initial_setup()
    
