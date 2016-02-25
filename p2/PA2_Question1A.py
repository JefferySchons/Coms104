from datetime import date

def display_birthday_wishes(name, month, year):
    print "Hi,"+name
    the_age = date.today().year
    if int(month)<date.today().month:
        the_age = the_age -1
    print "You are "+str(the_age)+" year old this year!" #why is year singular in requirements

    if int(month) == 1:
        flower_name= 'carnations'
    elif int(month) ==2:
        flower_name= 'Primrose'
    elif int(month) == 3:
        flower_name= 'Daffodils'
    elif int(month) == 4:
        flower_name= 'Sweet peas'
    elif int(month) == 5:
        flower_name= 'Hawthorn flowers'
    elif int(month) == 6:
        flower_name= 'Roses'
    elif int(month) == 7:
        flower_name= 'Water lilies'
    elif int(month) == 8:
        flower_name= 'Poppies'
    elif int(month) == 9:
        flower_name= 'Asters'
    elif int(month) == 10:
        flower_name= 'Calendulas'
    elif int(month) == 11:
        flower_name= 'Chrysanthemums'
    else:
        flower_name= 'Holly flowers'
        
    print "Here's a bouquet of "+ flower_name+ " for you!"

