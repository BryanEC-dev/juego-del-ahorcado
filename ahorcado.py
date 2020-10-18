import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+')


def random_word():
    length = len(WORDS) - 1
    idx = random.randint(0, length)
    return WORDS[idx]


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    letters = []
    repeated_letter = False 
    one_letter =''

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Ingresa una letra: '))

        """ validar si ingreso la palabra correcta """
        if len(current_letter) > 1:
            print('ingresaste la palabra: {}'.format(current_letter))
            if current_letter == word:
               print('')
               print('Felicidades')
               print('¡Felicitaciones! ganaste, la palabra es: {}'.format(word))
               break
            else:
                """  """
                tries += 1

                if tries == 7:
                    display_board(hidden_word, tries)
                    print('')
                    print('¡ Perdiste!, la palabra correcta era {}'.format(word))
                    break
        else:
            one_letter = current_letter[0]

        print(one_letter)
        """ one_letter = current_letter[0] """
        """ Validar si la letra ya ha sido ingreada """
        for l in letters:
            print('{} no es igual a {}'.format(one_letter, letters))
            if one_letter == l:
               print("Esta letra ya ha sido ingresada, ingrese una nueva letra")
               repeated_letter = True
               break

        if repeated_letter == True :
            repeated_letter = False
            continue

        print('continue con el flujo')  
        letter_indexes = []
        for idx  in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries +=1

            if tries == 7:
                display_board(hidden_word,tries)
                print('')
                print('¡ Perdiste!, la palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter    
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades')
            print('¡Felicitaciones! ganaste, la palabra es: {}'.format(word))
            break
        
        letters.append(one_letter)

def iterable():
    lista = ['a', 'b' , 'c' , 'd']

    for iter in lista:
        print(iter)

if __name__ == '__main__':
    print('BIENVENIDOS AL JUEGO DEL AHORCADO')
    run()
   



