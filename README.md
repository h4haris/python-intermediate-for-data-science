# Python Intermediate 
Advanced python knowledge and experimentation with 'Matplotlib' for ploting graphs and 'Pandas' for tabular data handling for Data Science

## Content
- Visualization
- Data Structure
- Control Structures
- Case Study

### Data Visualization
- very imp in data Analysis
- -> to explore data
- -> report insights

### Matplotlib

```bash
Line Plot
------------------

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
population = [2.5, 3.69, 5.26, 6.97]
plt.plot(year, population) => line chart, first list is mapped to x axis and second to y axis
plt.show()
```

If you pass only one argument in 'plot', Python will know what to do and will use the index of the list to map onto the x axis, and the values in the list onto the y axis.

```bash
Scatter Plot
------------------

plt.scatter(year, population) => scatter chart
plt.show()
```

```bash
Change a scale to logarithmic
------------------
plt.xscale('log')
```

### Histogram
- Explore dataset
- Get idea about distribution

```bash
help(plt.hist)

plt.hist(values, bins=3) => by default bin is 10
plt.show()
```

### Clean a Plot

```bash
plt.clf() => cleans a plot so you can start a fresh
```

### Plot Customization

Many options
- different plot types
- many customizations

Choice depends on
- Data
- Story you want to tell

```bash
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10]) => to start y axis from zero

plt.yticks([0,2,4,6,8,10], ['0','2B','4B','6B','8B','10B']) => to indicate label in billions with corresponding values

plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8) => s for size increase by double, c for color schemes, alpha for opacity between 0-1 

plt.grid(True) => add gridlines on the plot
plt.text(1550, 71, 'India') => add text to point
```

call all these customizations before show()

### Dictionaries

```bash
world = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

Retrieving data
------------------
print(world.keys()) => print keys in dictionary
print(world['norway']) => print value of a key


Changing data
------------------
world["Pakistan"] = 'Karachi' => will add new key/value pair if not present or update existing key

'Pakistan' in world => check if key exist and return True

del(world["Pakistan"]) => to remove a key/value pair from dictionary
```

### Pandas
- high level data manipulation tool
- built on numpy
- store data in dataframe

```bash
import pandas as pd
brics = pd.DataFrame(dict)

brics.index = ['BR', 'RU', 'IN'] => to change index to custom index

brics = pd.read_csv('path/to/brics.csv') => to import from csv file

brics = pd.read_csv('path/to/brics.csv', index_col=0) => to define that first col is index
```

### Pandas Access Methods

```bash
IDEAL METHODS
------------------

- accessing columns 
brics['country'] => will return 2D arrays
brics[ ['country'] ] => use double square brackets to return 1D array
brics[ ['country', 'capital'] ] => will return two columns

- accessing rows 
brics[1:4]

PANDAS METHODS
------------------
loc (label-based)
iloc (integer position-based)

- accessing rows 
brics.loc[ ["RU", "IN"] ] => will return 2 rows with all columns
brics.iloc[ [1,2] ]

- accessing columns 
brics.loc[ :, ["country", "capital"] ] => will return all rows with country and capital columns
brics.iloc[ :, [0,1] ]

- accessing both 
brics.loc[ ["RU", "IN"], ["country", "capital"] ] => will return 2 rows with country and capital columns
brics.iloc[ [1,2], [0,1] ]
```

### Comparison Operators
==, !=, <=, >=, >, <

### Boolean Operators
```bash
and, or, not

for numpy:
-logical_and()
np.logical_and(bmi>21, bmi <22)

logical_or()
logical_not()
```

### if, elif, else

```bash
if z%2 == 0 :
    print('z is divisible by 2')
elif z%3 == 0 :
    print('z is divisible by 3')
else :
    print('z is neither divisible by 2 nor by 3')
```

### Filtering pandas DataFrames

```bash
brics[ brics["area"] > 8 ] => will filter table data where area is greater than 8
brics[ np.logical_and( brics["area"] > 8, brics["area"] < 10) ] => will filter table data where area is between 8 and 10
```

### Loops

```bash
-While

while condition :
    expression

-for loop
work with lists + strings

for var in seq :
    expression

-for loop with index
for index, height in enumerate(seq) :
    expression

-For loop n times [Here n=10]
for x in range(10) :
    expression
```


### Looping Data Structures

```bash
-Looping thru Dictionary
for key, val in dict.items() :
    expression

-Looping thru NumPy array (multi-dimension)
for val in np.nditer(my_array) :
    expression
```

### Looping Panda table

```bash
for val in brics :
    print(val)

Output => each label will be printed
e.g.
country
capital
area
population

For printing each row:
------------------

for label, row in brics.iterrows() :
    print(label)
    print(row)

Output => print label and each row with all columns one by one in separate line

for label, row in brics.iterrows() :
    print(label + ': ' + row['capital'])

Output => print label + capital only from each row

Iterate Dataframe with for loop
For adding a new column with for loop
------------------

for label, row in brics.iterrows() :
    # creating series on every iteration
    brics.loc[ label, "name_length"] = len(row["country"])
print(brics)

Do vectorized operations using Apply [MORE EFFICIENT WAY]
For adding a new column without for loop 
------------------

brics[ "name_length" ] = brics[ "country" ].apply(len)
print(brics)
```

### Random Numbers
How to Solve?
- Analytical
- Simulate the process (Hacker statistics!)

```bash
np.random.rand() => generate random float between 0 and 1
np.random.seed(123) => sets the random seed, so that your results are reproducible between simulations.
np.random.randint(4, 8) => generate random int between 4(inclusive) and 8
```

### Random Walk

```bash
Known in Science
-> Path of molecules
-> Gambler's financial status
```

## Case Study

1. Imagine the following: you're walking up the empire state building to DataCamp HeadQuarters and you're playing a game with a friend.

2. You throw a die one hundred times.

3. If it's 1 or 2 you'll go one step down.

4. If it's 3, 4, or 5, you'll go one step up.

5. If you throw a 6, you'll throw the die again and will walk up the resulting number of steps.

6. Of course, you can not go lower than step number 0. And also, you admit that you're a bit clumsy and have a chance of 0.1% of falling down the stairs when you make a move. Falling down means that you have to start again from step 0. With all of this in mind, you bet with your friend that you'll reach 60 steps high.

7. How to solve? What is the chance that you will win this bet?

### Answer 
- Simulate multiple random walks and plot histogram.

- To calculate the chance that this end point is greater than or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, the total number of simulations.

- Ans : 78.4%