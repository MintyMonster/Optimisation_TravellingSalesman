import numpy
import pandas as pd
#import itertools

data = pd.read_csv('cities.csv')
cities: list = []
startDistance: float = 10_987_144.136907717
currentDistance: float = startDistance
iterations: int = 10_000
random = numpy.random.randint # "Avoid the dot"

allDistances: list = []

# Get the euclidean distance from 2 cities
def distance(city1: tuple, city2: tuple) -> float:
    return numpy.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) # Distance formula
    #return numpy.linalg.norm(city1, city2)

# # Get the cumulative distance between 2 cities in the list, return cumulative distance as float
def objectiveFunction(cityList: list) -> float:
    cumulativeDistance: float = distance(cityList[0], cityList[-1])
    #cumulativeDistance += [distance(cityList[i], cityList[i + 1]) for i in range(0, len(cityList) - 1)]
    for i in range(0, len(cityList) - 1):
        cumulativeDistance += distance(cityList[i], cityList[i + 1])

    return cumulativeDistance

# Swap two cities in the list, create new list to run calculations on
def citySwap(cityList: list) -> list:
    cityA: int = random(0, len(cityList))
    cityB: int = random(0, len(cityList))

    newCityList = list(cityList)
    newCityList[cityA], newCityList[cityB] = cityList[cityB], cityList[cityA]

    return newCityList

# If the conditions are met, return a true/false statement to allow for swapping or not
def makeSwap(originalScore: float, newScore: float, distance: float) -> bool:
    randomChance: int = random(0, startDistance)
    swap = True

    if originalScore < newScore:
        swap = False
        if randomChance < distance:
            swap = True

    if originalScore > newScore:
        swap = True
        if randomChance < distance:
            swap = False

    return swap

# Maybe we get half decent averages??
# Average out every distance put together
def average(distances: list) -> float:
    distance = 0

    for i in distances:
        distance += i

    print("Total distance:", distance)
    return distance / len(allDistances)

# Main()
def main():
    global currentDistance, cities

    cities += [(j['X'], j['Y']) for i, j in data.head(5001).iterrows()] # Quicker than regular for loop

    #cities.append([(j['X'], j['Y']) for i, j in data.head(5001).iterrows()])

    #for i, j in data.head(5001).iterrows():
    #   cities.append((j['X'], j['Y']))

    #itertools.chain(cities, ((j['X'], j['Y']) for i, j in data.head(5001).iterrows()))

    print(cities)

    # Main logic
    for i in range(0, iterations):
        # Get new city list
        newCities: list = citySwap(cities)
        # Get scores/objectives
        currentScore: float = objectiveFunction(cities)
        newScore: float = objectiveFunction(cities)

        # If the swap is true, swap the values and set old list to new list with swapped value
        if makeSwap(currentScore, newScore, currentDistance):
            cities = newCities

        # Remove some distance
        currentDistance -= 1000
        #print(cities)
        print(i, ": ", objectiveFunction(cities))
        # Add to list for the "average()" function
        allDistances.append(objectiveFunction(cities))

    # User feedback logic
    o1: float = objectiveFunction(cities)
    newcities: list = citySwap(cities)
    o2: float = objectiveFunction(newcities)
    print(makeSwap(o1, o2, currentDistance))

    print("Average", average(allDistances))

# Define main
if __name__ == '__main__':
    main()

# Results

# 1,000,000 iterations(1) -> 11001341.12971

# 100,000 iterations(1) -> 11178934.8743292

# 50,000 iterations(1) -> 10974512.12378819

# 20,000 iterations(1) -> 11070768.911042985
# 20,000 iterations(2) -> 11108708.12710553
# 20,000 iterations(3) -> 11036493.184472352

# 20,000 average ==> 11071990.0742

# 15,000 iterations(1) -> 11095028.292239944
# 15,000 iterations(2) -> 11291439.332093196
# 15,000 iterations(3) -> 11121352.235697258
# 15,000 iterations(4) -> 11013246.381083615
# 15,000 iterations(5) -> 11044441.89298024

# 15,000 average ==> 11113101.6268

# 10,000 iterations(1) -> 11093442.201513553
# 10,000 iterations(2) -> 11055938.024081167
# 10,000 iterations(3) -> 10982057.737973414 ==> WIN!
# 10,000 iterations(4) -> 11048806.619376583
# 10,000 iterations(5) -> 11044827.237103494

# 10,000 average ==> 11045014.364

# 5,000 iterations(1) -> 11047772.268310422
# 5,000 iterations(2) -> 11138903.59188073
# 5,000 iterations(3) -> 11082429.534282451
# 5,000 iterations(4) -> 11196114.514311789
# 5,000 iterations(5) -> 11187077.503559494

# 5,000 average ==> 11130459.4825

# 1,000 iterations() -> 11043870.779970698
# 1,000 iterations() -> 11031215.41168306
# 1,000 iterations() -> 11043355.857864594
# 1,000 iterations() -> 10996629.816949299
# 1,000 iterations() -> 11038306.036355073

# 1,000 average ==> 11030675.5806

# Resources
# https://towardsdatascience.com/optimizing-your-python-code-156d4b8f4a29
