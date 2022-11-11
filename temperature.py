temp_degree = int(input("Enter temperature in degree celcius :"))
if temp_degree < -273.15:
    print("The temperature is invalid because it is below absolute zero.")
elif temp_degree == -273.15:
    print("The temperature is absolute zero.")
elif temp_degree > -273.15 and temp_degree < 0:
    print("The temperature is below freezing.") 
elif temp_degree == 0:
    print("The temperature is at the freezing point.")
elif temp_degree > 0 and temp_degree < 100:
    print("The temperature is in the normal range.")
elif temp_degree == 100:
    print("The temperature is at the boiling point.")
else :
    print("The temperature is above the boiling point.")
    
