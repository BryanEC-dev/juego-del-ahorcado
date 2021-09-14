"""
 Functions that display information on the screen
"""

from config.configuration import config
from colorama import init, Fore, Back, Style

def welcome():
    print('-------------------------------------')
    print('|                                   |')
    print('|' +Fore.GREEN +' BIENVENIDOS AL JUEGO DEL AHORCADO ' + Fore.RESET + '|')
    print('|                                   |')
    print('-------------------------------------')
    print('\n')
    print('---------------------------------------------------------------------')
    print('|' +Fore.GREEN +'                                 REGLAS                             ' + Fore.RESET + '|')
    print('---------------------------------------------------------------------')
    print(Fore.CYAN +'1. ' +Fore.RESET + 'Tienes 7 intentos para adivinar la palabra.')
    print(Fore.CYAN +'2. ' +Fore.RESET + 'Puedes ingresar una letra o la palabra completa.')
    print(Fore.CYAN +'3. ' +Fore.RESET + 'Si luego de solicitar tres pistas no adivinas la palabra perderás.')



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
        print('¡Felicitaciones! Ganaste!!!! La palabra es: {}'.format(word))
    else:
        print('')
        print('¡ Perdiste!, la palabra correcta era {}'.format(word))


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
