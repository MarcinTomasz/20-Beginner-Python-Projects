#Replace method used to replace strings.

sentence = '\n Words in my string. \n'

def replace_word():
    
    words_to_replace = input('Enter words to replace: ')
    new_words = input('Enter new words: ')
    print(sentence.replace(words_to_replace, new_words))
    

print(sentence)
replace_word()
