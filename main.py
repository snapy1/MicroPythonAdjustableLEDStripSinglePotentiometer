from Settings.LED import *
from Settings.Potentiometer import *

l = LED(15, 60)
p = Potentiometer(26)

currentPotValue = p.getPotValue()


while True:
    if p.getPotValue() != currentPotValue:  # if the updated value is different than the old one
        # then updating currentPotValue
        currentPotValue = p.getPotValue()
        l.gradientWithPercentage(currentPotValue)
