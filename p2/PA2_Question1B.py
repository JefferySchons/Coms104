from PA2_Question1A import display_birthday_wishes

name = raw_input("Enter name:")
dob = raw_input("Enter dob (mm/dd/yyyy)")

month = dob[0:2]
day = dob[3:5]
year = dob[6: ]
display_birthday_wishes(name,year,month)
