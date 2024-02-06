import random
import sys
from pathlib import Path



def pick_n_draw():
    word_list_file = '../files/mit-wordlist'

    word_list =None 
    with open(Path(word_list_file),'r') as f_handler:
        words = f_handler.read()
        word_list = words.split('\n')

    pos = random.randint(1,len(word_list))
    picked_word = word_list[pos-1]
    word_len = len(picked_word)

    draw_st = picked_word[random.randint(0,len(picked_word)-1)]

    dash_dash = '_ '*word_len


    n = 0
    m = 0
    c_word = ['_' for ch in picked_word ]
    print('------------------------------------')
    print(f'''Let's play a game.I am thinking of a word and you have to make a guess.\
            Here is the hint:\nIts a {word_len} letter word. Can you make a guess?\n\n {c_word}''')
    print('------------------------------------')
    while n < word_len+2:
        guess = input('Type a letter(character) and Hit Enter: ')
        n +=1
        if guess in picked_word:
            m += 1
            if m == word_len:
                print(f'Congratulation! you won.')
                print('-------------------------')
                sys.exit()
            print(f'Congratulation! {m} letter right. :)')
            find_word_pos = picked_word.find(guess)
            c_word[find_word_pos] = guess
            print(c_word)
            guess = ''
        else:
            continue
        if n > (len(c_word)):
            print('-----------------------------------------')
            print(f'Ok! You have exceeded the number of tries allowed for this word. The word was {picked_word}')
            print('-----------------------------------------')
            sys.exit()
        
def main():
    pick_n_draw()
if __name__=="__main__":
    main()
    #n_i_c_e_
    #r_e_d_
