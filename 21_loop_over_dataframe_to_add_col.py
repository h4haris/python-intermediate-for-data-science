# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)


# Code for loop that adds COUNTRY column
for label, row in cars.iterrows() :
    # creating series on every iteration
    cars.loc[ label, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)




# Use .apply(str.upper)
cars[ "COUNTRY" ] = cars[ "country" ].apply(str.upper)
print(cars)