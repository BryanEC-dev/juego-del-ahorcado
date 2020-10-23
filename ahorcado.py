
import welcome
import repository.words as words
import utilities.secuence as secuence


numberHelp = 0
tries = 0
lettersEntered = []
repeated_letter = False
one_letter = ''
word = ''
hidden_word = ''
# get the sequence of images of the game
IMAGES = secuence.images()

# get the words to play
myWords = words.conection()
WORDS = myWords.getAllWords()

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+ ----+')



def run():
    global word
    global hidden_word
    """ get a random word """
    randomWord = secuence.randomWord(WORDS)
    word = randomWord[1]
    hidden_word = ['-'] * len(word)


    while True:
        display_board(hidden_word, tries)
        try:
            option = int(input("""
                1.Obtener una pista
                2.Ingresar una letra o palabra   
            """))

            if option == 1:

                global numberHelp
                if numberHelp == 3:
                    print("ya no tienes mas pistas")
                    enter = input("Presiona enter para continuar....")
                else:
                    idx = numberHelp + 2  # 2 is added by the position of the tracks in the database
                    print(randomWord[idx])
                    enter = input("Presiona enter para continuar....")
                    numberHelp += 1
                    continue

            elif option == 2:
                enterLetter()
                gameOver()
            else:
                print('La opción ingresada es incorrecta')
        except ValueError as error:
            print('--- SOLO SE PUEDE INGRESAR NÚMEROS ---')
            enter = input("Presiona enter para continuar....")
       

        
def enterLetter():
    global tries
    if numberHelp == 3:
        tries = 6
    
    letters = input("Ingrese una letra o una palabra: ")

    #TODO validar si la palabra ingresada no cuntiene caracteres no permitidos 

    if len(letters) > 1:
        won = verifyWord(letters)
        if won == True:
            pass
            # finde del juego
        else:
            tries += 1
            #aumenta el contador de errores
    else:
        verifyLetter(letters)
        pass



def verifyWord(letters):
    if letters == words:
        return True
    else:
        return False


def verifyLetter(letter):
    global word
    global tries
    # check if the letter has already been entered
    if len(lettersEntered) == 0:
        lettersEntered.append(letter)
    else:
        if letter in lettersEntered:
            print("La letra ya fue ingresada.")
            # debería detenerse el flujo
        else:
            lettersEntered.append(letter)
    # validate if the letter is in the word
    print('la palabara es',word)
    if (not letter in word ):        
        tries +=1
    else:
        replaceLetter(letter)
        pass


def replaceLetter(letter):
    print('enntrando a función')
    global word
    global hidden_word
    wordTemporal = []

    for x in word:
        if x == letter:
            wordTemporal.append(letter)
        else:
            wordTemporal.append('-')
    
    hidden_word = wordTemporal
            


def gameOver():
    if tries == 7:
         display_board(hidden_word, tries)
         print('')
         print('¡ Perdiste!, la palabra correcta era {}'.format(word))
         

               

def iterable():
    lista = ['a', 'b' , 'c' , 'd']

    for iter in lista:
        print(iter)


def core():
    """ current_letter = str(input('Ingresa una letra: '))

        # comentario validar si ingreso la palabra correcta
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
        # comentario  one_letter = current_letter[0]
         # comentario Validar si la letra ya ha sido ingreada
        for l in letters:
            print('{} no es igual a {}'.format(one_letter, letters))
            if one_letter == l:
               print("Esta letra ya ha sido ingresada, ingrese una nueva letra")
               repeated_letter = True
               break

        if repeated_letter == True:
            repeated_letter = False
            continue

        print('continue con el flujo')
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
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

        letters.append(one_letter) """

if __name__ == '__main__':
    welcome.welcome()
    run()
    


    
   



