def findUserName(name):
    #given string 'lastname,firstname'
    user_name=name[name.find(',')+1:].strip()[0]+name[0:name.find(',')]
    return user_name

    #index_of_coma= name.find(',')
    # first_name=name[index_of_coma+1:].strip()
   # last_name=name[0:index_of_coma]
   # user_name=first_name[0]+last_name
   # return user_name
