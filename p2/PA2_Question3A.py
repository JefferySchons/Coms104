from random import randint

def Guess_Win():
    print 'try to guess a number between 1 and 10'
    correct=0
    guess1=input('Whats  your first guess?')
    random_number=randint(1,10)
    if guess1 != random_number:
        if guess1 > random_number:
            print 'Too high!'
        else:
            print 'Too low!'
        while correct==0:
            guess2=input('Whats  your next guess?')
            if guess2==random_number:
                print 'Thats it!'
                correct=1
            elif guess2 > random_number:
                print 'Too high!'
            else:
                print 'Too low!'
