def switcherro():

    word = raw_input('enter word to swap:')
    new_word=word[len(word)-1]+word[1:len(word)-1]+word[0]
    return new_word
