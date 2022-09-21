# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
    print(area)



# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))




# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for h in house :
    print("the " + str(h[0]) + " is " + str(h[1]) + " sqm")