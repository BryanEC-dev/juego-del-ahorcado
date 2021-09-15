import time
from colorama import init, Fore, Back, Style
# it is verified if the word or letter I entered is correct
def enter_letter():
    letter = False
    word = False
    
    letters = input(Fore.CYAN +"Ingrese una letra o una palabra: " +Fore.RESET)
    letters = letters.lower()
    
    if len(letters) > 1:
        word= True
    else:
        letter = True
    
    response = {'letter' : letter, 'word': word, 'letters' : letters }
    return response


def verify_word(letters,word):
    if letters == word:
        return True
    else:
        return False


def verify_letter(letter,word,letters_entered):
    
    repeated_letter = False
    # check if the letter has already been entered
    if len(letters_entered) == 0:
        letters_entered.append(letter)
    else:
        if letter in letters_entered:
            print("La letra ya fue ingresada.")
            repeated_letter = True
        else:
            letters_entered.append(letter)
    return {'repeat_letter': repeated_letter, 'letters' : letters_entered}


def replace_letter(letter,word,hidden_word, tries):

    if (not letter in word):
            print('La letra "{}" no se encuentra en la palabra. '.format(letter))
            time.sleep(2)
            tries += 1
    else:
        for index, x in enumerate(word):
            if x == letter:
                hidden_word[index] = letter
        print('La letra "{}" si se encuentra en la palabra. '.format(letter))
        time.sleep(2)
    return hidden_word, tries
        
def track(number_help,random_word):
    if number_help == 3:
        print(Fore.RED + "ya no tienes mas pistas" + Fore.RESET)
        time.sleep(3)
    else:
        # 2 is added by the position of the tracks in the database
        idx = number_help + 1 
        track = f'Pista {idx}: '
        print(Fore.CYAN + track + Fore.RESET +  random_word[idx])
        number_help += 1
        time.sleep(5)
    
    return number_help

def review_track(word, track):
    print('\n-----------------------------------------------------------')
    print('Palabra de {} letras'.format(len(word[0])))
    print('\nPistas reveladas:')
    if track >= 1 : print(Fore.CYAN + 'Pista 1:' + Fore.RESET +  word[1])
    if track >= 2 : print(Fore.CYAN + 'Pista 2:'+ Fore.RESET +  word[2])
    if track >= 3 : print(Fore.CYAN + 'Pista 3:' + Fore.RESET +  word[3])
    print('-----------------------------------------------------------\n')
    
        
    
    





