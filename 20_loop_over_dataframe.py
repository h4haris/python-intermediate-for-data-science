# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for label, row in cars.iterrows() :
    print(label)
    print(row)



# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ': ' + str(row['cars_per_cap']))
