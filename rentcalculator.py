
total_food=int(input("Enter food charges per month :"))
total_electricity=int(input("Enter total electricity charge per month :"))
total_roomrent=int(input("Enter total room rent in permonth :"))
total_water=int(input("Enter water charges in per month :"))
total_person=int(input("Enter the person living in room :"))

total_amount=(total_food+total_electricity
              +total_roomrent+total_water)

print("Total Amount of Room in per month : ",total_amount)
per_person_rent=total_amount/total_person

print("Per Person Rent in per month = ",per_person_rent)



