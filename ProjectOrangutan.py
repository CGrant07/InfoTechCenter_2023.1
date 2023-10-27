print("*******************************************************")
print("Gasoline Branch\n\n")

#Import Libraries here
import random
from time import sleep

def gasLevelGuage():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel



