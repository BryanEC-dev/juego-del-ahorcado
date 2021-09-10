import time

# it is verified if the word or letter I entered is correct
def enter_letter():
    letter = False
    word = False
    
    letters = input("Ingrese una letra o una palabra: ")
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
            tries += 1
    else:
        for index, x in enumerate(word):
            if x == letter:
                hidden_word[index] = letter
    
    return hidden_word, tries
        
def track(number_help,random_word):
    if number_help == 3:
        print("ya no tienes mas pistas")
        time.sleep(3)
    else:
        # 2 is added by the position of the tracks in the database
        idx = number_help + 1  
        print(f'Pista {idx}: {random_word[idx]}' )
        number_help += 1
        time.sleep(5)
    
    return number_help
        
    
    





