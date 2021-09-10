from view.scream import welcome, display_board, message
def game_over(hidden_word, tries, images,word):
    if tries == 7:
        display_board(hidden_word, tries, images)
        message(False, word)
        return True
    else:
        return False


def win(word):
    message(True, word)
