# Write a Python program that does the following:
# 1. Take three inputs from the user:
# • Distance they need to travel (in kilometers),
# • Speed they plan to travel at (in kilometers per hour),
# • Break time in minutes (how long they plan to rest during the journey).
# 2. The program should calculate:
# • The total travel time (distance divided by speed),
# • The total break time (convert break time into hours and add it to the total travel
# time).
# 3. Finally, print the result in this format:
# "The total journey will take [total journey time] hours including breaks."

# Default Values -
# Distance: 120 km
# Speed: 60 hr
# Break Time: 30 mins

#################
# Take inputs from the user
distance = float(input("Enter the distance to travel in kilometers: "))
speed = float(input("Enter the speed in kilometers per hour: "))
break_time = float(input("Enter break time in minutes: "))

# Calculate travel time
travel_time = distance / speed 

# Convert break time from minutes to hours
break_time_in_hours = break_time / 60

# Calculate total journey time
total_journey_time = travel_time + break_time_in_hours

print(f"The total journey will take {total_journey_time} hours including breaks.")
