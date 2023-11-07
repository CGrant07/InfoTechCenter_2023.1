"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""

#Import Libraries Here
import time
import sys
import random
from time import sleep

timeToSleep = 2

print("\n\nWelcome - InfoTech Center 2023\n\n")
time.sleep(timeToSleep)

#Add code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so message is printed on top of previous line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Retina Scanned - Access Granted")



print("\n\n********************************************************************\n\n")
print("Checking current gas levels\n")
sleep(1.5)


# Function that lists Gas Stations, randomly choosing one, and Return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shell", "Speedway","Exon", "Meijer", "Cosco", "Marathon", "BP", "Circle K", "Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

# Function will call gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank has a Quarter Tank of gasoline left, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(), "which is", milesToGasStationsQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank has half of a tank which is plenty to get to your destinations.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank left!")
    else:
        print("You have a full tank of gas!")


gasLevelAlert()

print("\n********************************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunny","Cloudy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

# VRS() function will allow my vehicle to respond based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has engaged, only allowing you to drive 50 MPH.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated your alarm by 45 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has engaged, only allowing you to drive 30 MPH.")
    elif weatherAlert == "Rain":
        print("\nNational Weather Service has updated your alarm by 10 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has engaged, only allowing you to drive 60 MPH.")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated your alarm by 25 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has engaged, only allowing you to drive 45 MPH.")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated your alarm by 5 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has engaged, only allowing you to drive 65 MPH.")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated your alarm by 60 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has engaged, only allowing you to drive 25 MPH.")
    elif weatherAlert == "Sunny":
        print("\nThe weather forcast is calling for a", weatherAlert, "day, enjoy your drive!")
    else:
        print("\nThe weather forcast is calling for a", weatherAlert, "day, enjoy your drive!")

vehicleResponseSystem()

