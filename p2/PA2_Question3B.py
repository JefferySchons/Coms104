from PA2_Question3A import Guess_Win

print '###Menu###'

print 'p) Play the guessing game'

print 'q) Quit'

choise=raw_input("Enter your choise")
while choise!='q':
    Guess_Win()
    print '###Menu###'
    print 'p) Play the guessing game'
    print 'q) Quit'
    choise=raw_input('Enter your choise')
print 'Bye!!'
