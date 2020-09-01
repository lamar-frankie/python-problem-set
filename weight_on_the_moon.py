#This script is used to calculate your weight on the moon. 

#Create a constant and set it equal to the moon weight differential of 1.622
MOON_WEIGHT_DIFFERENTIAL = 1.22


#Ask the user to enter their weight
user_weight = input("Enter your weight: ")


#Calculate the users weight on the moon (Moon weight = Earth weight * moon weight differential)
def calculate_weight_on_moon(weight):
  moon_weight = weight * MOON_WEIGHT_DIFFERENTIAL
  print(moon_weight)
  
  
