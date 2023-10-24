from machine import ADC


class Potentiometer:
    adcpin = None
    updateRate = None
    potValue = None

    def __init__(self, gpio):
        self.adcpin = gpio

    def ReadPotentiometer(self):
        pot = ADC(self.adcpin)

        adc_value = pot.read_u16()
        volt = (3.3 / 65535) * adc_value

        percentPot = self.__scale__percent(volt)

        return percentPot

    def __scale__percent(self, volt):
        percent = (volt / 3.3) * 100
        return int(percent)

    def getPotValue(self):
        return self.ReadPotentiometer()

