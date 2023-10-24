from machine import ADC
from time import sleep


class Potentiometer:
    adcpin = None
    updateRate = None
    potValue = None

    def __init__(self, gpio):
        self.adcpin = gpio
        # self.updateRate = updateRate

    def ReadPotentiometer(self):
        pot = ADC(self.adcpin)

        adc_value = pot.read_u16()
        volt = (3.3 / 65535) * adc_value

        percentPot = self.__scale__percent(volt)

        # self.potValue = percentPot
        return percentPot

    def __scale__percent(self, volt):
        percent = (volt / 3.3) * 100
        return int(percent)

    def getPotValue(self):
        return self.ReadPotentiometer()

    # while True:
    #     potvalue = ReadPotentiometer()
    #     print(potvalue)
    #     sleep(1)




