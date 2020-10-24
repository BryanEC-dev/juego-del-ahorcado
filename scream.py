


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
    print('1. Tienes 7 intentos para adivinar la palabra')   
    print('2. Puedes ingresar una letra o una palabra completa')   
    print('3. Si luego de solicitar tres pistas no adivinas la palabra perderas')

    print("\n Suerte....")   


def display_board(hidden_word, tries,IMAGES):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+')

def message(win,word):
    """
    docstring
    """
    if win:
        print('')
        print('¡Felicitaciones! Ganaste!!!! La palabra es: {}'.format(word))
    else:
        print('')
        print('¡ Perdiste!, la palabra correcta era {}'.format(word))
