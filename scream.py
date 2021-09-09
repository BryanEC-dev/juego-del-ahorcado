"""
 Functions that display information on the screen
"""


def welcome():
    print('-------------------------------------')
    print('|                                   |')
    print('| BIENVENIDOS AL JUEGO DEL AHORCADO |')
    print('|                                   |')
    print('-------------------------------------')
    print('\n')
    print('-------------------------------------')
    print('|            REGLAS                  |')
    print('-------------------------------------')
    print('1. Tienes 7 intentos para adivinar la palabra.')
    print('2. Puedes ingresar una letra o la palabra completa')
    print('3. Si luego de solicitar tres pistas no adivinas la palabra perderás')

    print("\n Suerte....")


def display_board(hidden_word: str, tries: int, images: list) -> None:
    """
    shows the hidden word and the image of the hanged man
    :param hidden_word:
    :param tries:
    :param images:
    :return:
    """
    print('')
    display_lives(7, tries)
    print(images[tries])
    print('')
    print(hidden_word)
    print('----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+')


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
    lives = ('vidas: ' + '\u2661' * lost_lives + '\u2665' * pending_lives)
    print(lives.ljust(100, ' '))
