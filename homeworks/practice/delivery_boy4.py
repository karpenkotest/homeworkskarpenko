max_floor=int(input("Enter the max floor number: "))
number_of_flats_per_floor=int(input("Enter the number of flats per floor: "))
searched_number=int(input("Enter the number you want to search: "))
number_of_flats_in_one_entrance=max_floor*number_of_flats_per_floor
#print(f'The number of flats in one entrance is {number_of_flats_in_one_entrance}')
enrtance_number=0
if searched_number%number_of_flats_in_one_entrance:
    entrance_number=searched_number//number_of_flats_in_one_entrance+1
    print("Entrance number:",entrance_number)
else:
  entrance_number=searched_number//number_of_flats_in_one_entrance
  print("Entrance number:",entrance_number)
normalized_numbers=searched_number%number_of_flats_in_one_entrance
#print(normalized_numbers)
if not normalized_numbers:
  print("Floor number:",max_floor)
if normalized_numbers:
     if normalized_numbers%number_of_flats_per_floor:
         floor=normalized_numbers//number_of_flats_per_floor+1
         print("Floor number:",floor)
     else:
         floor=normalized_numbers//number_of_flats_per_floor
         print("Floor number:",floor)
