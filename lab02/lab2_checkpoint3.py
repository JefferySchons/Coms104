

customer_name = raw_input("customer name?")
nights_number= input("number of nights?")

room_service_charge = input("room service amount?")
telephone_charge=input("telephone charge?")
                     
total_room_charge=(nights_number*55.0)
entertainment_tax=total_room_charge*.1

total_bill=total_room_charge+room_service_charge+telephone_charge+entertainment_tax
                       
print "river bend hotel bill (customer: "+customer_name+")"
print "total room charge($): ",total_room_charge
print "entertainment tax($):",entertainment_tax
print  "total bill($): ", total_bill
