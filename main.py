# Imports
import random
import numpy
import pandas as pd

# Variables
df = pd.read_csv('cities.csv') # Get file to read
cities: list = [] # Instantiate list
startDistance: float = 10987144.136907717 # Get the starting distance
currentDistance: float = startDistance # Set the current distance as the starting distance
iter: int = 5000 # Get the iterable value

def main(): # Define main
    global currentDistance # Access currentDistance
    global cities # Access cities (list)

    for i, j in df.head(5001).iterrows(): # Foreach row in file, in range of 0-5000
        cities.append((j['X'], j['Y'])) # Append into cities list as (X,Y)


    #print(cities)
    random.shuffle(cities) # Shuffle the list
    print(cities) # Print list

    ##################################################################

    for i in range(0, iter): # in range of 5000 (iter)
        #print(i)
        newCities: list = CitySwap(cities) # Create new list with 2 swapped values
        currentObjective: float = Objectivefunction(cities) # Get cumulative distance for currentObjective
        newObjective: float = Objectivefunction(newCities) # Get cumulative distance for newObjective from newly created list

        if MakeSwap(currentObjective, newObjective, currentDistance): # Check if the swap is true or false based on parameters
            cities = newCities # If swap is true, set old list to new list

        currentDistance -= 1 # Decrease currentDistance by 1

        print(Objectivefunction(cities)) # Prints

def MakeSwap(oScore: float, nScore: float, dist: float) -> bool: # Define MakeSwap()
    randomChance: int = random.randrange(0, int(startDistance)) # Get randomChance from 0 to startDistance (defined at the top)
    swap: bool = True # instantiate swap variable

    if oScore < nScore: # Check originalScore is smaller than newScore,
        swap = False # Make Swap false,
        if randomChance < dist: # However, if the randomChance is smaller than the distance,
            swap = True # Make the swap true

    if oScore > nScore: # Check originalScore is bigger than newScore,
        swap = True # Make swap true,
        if randomChance < dist: # However, if randomChance is smaller than the distance,
            swap = False # Make swap false

    return swap # Return the previously assigned boolean value

def CitySwap(citiesList: list) -> list: # Define CitySwap()
    cityA: int = random.randrange(0, len(citiesList)) # Get random cityA from cities (list)
    cityB: int = random.randrange(0, len(citiesList)) # Get ranom cityB from cities (list)

    newCityList: list = list(citiesList) # Instantiate a new list based on old list

    newCityList[cityA], newCityList[cityB] = citiesList[cityB], citiesList[cityA] # Swap A, B in new list, with A, B from old list

    return newCityList # Return newly created list

def Distance(city1: tuple, city2: tuple) -> float: # Define distance()
    return numpy.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) # Euclidean distance function

def Objectivefunction(citiesList: list) -> float: # define ObjectiveFunction()
    cDistance: float = Distance(citiesList[0], citiesList[-1]) # Create cumulative distance between first and last in the list

    for i in range(0, len(citiesList) - 1): # loop list in range of citiesList length
        cDistance: float = cDistance + Distance(citiesList[i], citiesList[i + 1]) # New cumulative distance is previous value + value + distance between i and i + 1

    return cDistance # Return cumulative distance

if __name__ == '__main__': # Main
    main()