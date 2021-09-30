"""
 Functions that display information on the screen
"""

from config.configuration import config
from colorama import init, Fore, Back, Style
import time

def welcome():
    print(' '* 14 + '-------------------------------------')
    print(' '* 14 +'|                                   |')
    print(' '* 14 +'|' +Fore.GREEN +' BIENVENIDOS AL JUEGO DEL AHORCADO ' + Fore.RESET + '|')
    print(' '* 14 +'|                                   |')
    print(' '* 14 +'-------------------------------------')
    print('\n')
    

def rules():
    print('---------------------------------------------------------------------')
    print('|' +Fore.GREEN +'                                 REGLAS                             ' + Fore.RESET + '|')
    print('---------------------------------------------------------------------')
    print(Fore.CYAN +'1. ' +Fore.RESET + 'Tienes 7 intentos para adivinar la palabra.')
    print(Fore.CYAN +'2. ' +Fore.RESET + 'Puedes ingresar una letra o la palabra completa.')
    print(Fore.CYAN +'3. ' +Fore.RESET + 'Luego de solicitar todas las pistas tendras una sola vida')

def display_board(hidden_word: str, tries: int, images: list) -> None:
    """
    shows the hidden word and the image of the hanged man
    :param hidden_word:
    :param tries:
    :param images:
    :return:
    """
    
    display_lives(int(config.get('VARIABLES','TRIES')), tries)
    print(images[tries])
    print('')
    print(hidden_word)
    print('----+'* len(hidden_word))


def message(win: bool, word: str) -> None:
    """

    :param win:indicates if the game was won
    :param word: the hidden word
    :return:None
    """
    if win:
        print('')
        print('---------------------------------------------------------------------')
        print('¡Felicitaciones! Ganaste!!!! La palabra es:' +Fore.GREEN + word + Fore.RESET )
        print('---------------------------------------------------------------------')
        #print('¡Felicitaciones! Ganaste!!!! La palabra es: {}'.format(word))
    else:
        print('')
        print('---------------------------------------------------------------------')
        print('Perdiste! , la palabra correcta era: ' +Fore.GREEN + word + Fore.RESET )
        print('---------------------------------------------------------------------')
       


def display_lives(total_lives: int, lost_lives: int) -> None:
    """
    shows the number of lives in the game
    :param lost_lives: lost lives in the game
    :param total_lives: total lives in the game
    :return: None
    """
    pending_lives = total_lives - lost_lives
    lives = (Fore.BLUE +'vidas: ' + Fore.RESET + '' + '\u2661' * lost_lives + '\u2665' * pending_lives)
    print('\n')
    print(lives.ljust(100, ' '))

def help_game():
    print('---------------------------------------------------------------------')
    print('|' +Fore.GREEN +'                                 ayuda                             ' + Fore.RESET + '|')
    print('---------------------------------------------------------------------')
    print(Fore.CYAN +'1. ' +Fore.RESET + 'Solo puedes obtener un total de 3 pistas presionando la opción 1.')
    print(Fore.CYAN +'2. ' +Fore.RESET + 'Puedes ingresar una letra o la palabra completa en  la opción 2.')
    print(Fore.CYAN +'3. ' +Fore.RESET + 'Puesdes revisar el número de letras y pistas que obtuviste en el juego en la opción 3.')
    print(Fore.CYAN +'5. ' +Fore.RESET + 'Puesdes salir del juego en la opción 5.')
    time.sleep(5)
    

def configuration_game():
    print('configuracion:')
    print('Este juego tiene 3 niveles, escoga uno de los niveles')
    level = int(input('Ingrese el nivel que desea'))
    print('Cada nivel tiene 4 palabras')
    print('Sistma de puntaje:')
    print('el puntaje obtenido en cada palabra equivale al número de vidas')
    print('Si pierde en alguna palabra no obtendra puntos y solo se quedara con los puntos de la palabra anterior')
    time.sleep(6)
    

def show_score(scores: list) -> None:
    """

    :param points: list with scores
    :return:None
    """
    print('')
    print('------------------------------------------------')
    print('|'+Fore.CYAN+'Nombre        '+Fore.RESET+'| '+Fore.CYAN+'Puntaje'+Fore.RESET+'|'+Fore.CYAN+'Fecha                 '+Fore.RESET +'|')
    print('------------------------------------------------')
    for score in scores:
        data = list(score)
        print(' {} {}  {}'.format(data[0] + ' '*(14 - len(data[0])), str(data[1]) + ' '*6,str(data[2])))
    print('------------------------------------------------')
    print('\n')
        
    
    