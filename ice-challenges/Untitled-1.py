rider1_age = int(input("how old is first rider? "))
rider1_height = int(input("How tall is the first rider? "))
rider_query = input("Is there a second rider? Enter yes, or no. ")
second_rider = rider_query.lower()

if second_rider == "yes":
  rider2_height = int(input("How tall is the second rider? "))
  rider2_age = int(input("how old is the second rider? "))
else:
  second_rider = "no"

if second_rider == "no":
    if rider1_height < 36:
        print("You must be 3 feet or over to ride.")
    elif rider1_age >= 18 and rider1_height >=62:
        print ("You may ride the rollercoaster. Have fun, and be safe!")
    else:
        print ("You are either not old enough or tall enough to ride alone.")
elif second_rider == "yes":
   if rider1_age >= 18 or rider2_age >= 18:
      print("Since one of you two are 18 or older, you may ride together. Please be safe and have fun!")
   else:
      print("Your group does not meet our minimum standards if you want to ride together.")
