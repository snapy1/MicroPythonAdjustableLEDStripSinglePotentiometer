import machine
import neopixel
from Settings.Brightness import *
from time import sleep


class LED:
    np = None
    amount = None
    gpio = None

    def __init__(self, gpio, amount):
        self.amount = amount
        self.gpio = gpio
        self.np = neopixel.NeoPixel(machine.Pin(gpio), amount)

    def police(self):
        for k in range(100):
            for i in range(self.amount):
                self.changeColor(i, 0, 0, 255)

            sleep(0.05)

            for i in range(self.amount):
                self.changeColor(i, 255, 0, 0)

            sleep(0.05)

    def enableAll(self, r, g, b, brightness):
        bp = Brightness(self.np)
        for i in range(self.amount):
            self.np[i] = (r, g, b)
            bp.set_brightness((r, g, b), brightness)
        self.np.write()

    def changeColor(self, index, r, g, b):
        self.np[index] = (r, g, b)
        self.np.write()

    def changeAllColor(self, r, g, b):
        for i in range(self.amount):
            self.np[i] = (r, g, b)
        self.np.write()

    def getAmount(self):
        return self.amount

    def setValueWithPercentage(self, percentage):

        if percentage < 0:
            percentage = 0
        if percentage > 100:
            percentage = 100

        t = percentage / 50.0

        if percentage <= 50:
            R = int(255 * (1 - t))
            G = int(255 * t)
            B = 0
        else:
            t -= 1  # Adjust the value of t for the second segment
            R = 0
            G = int(255 * (1 - t))
            B = int(255 * t)

        self.changeAllColor(R, G, B)

    def gradientWithPercentage(self, percentage):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128)]
        # Ensure percentage is between 0 and 100
        percentage = max(0, min(percentage, 100))

        # Calculate how many colors and segments
        num_colors = len(colors)
        segment_length = 100.0 / (num_colors - 1)

        # Find the segment the percentage falls into
        segment_index = int(percentage // segment_length)
        segment_t = (percentage % segment_length) / segment_length

        if segment_index >= len(colors) - 1:
            # Handle the edge case where percentage = 100
            return colors[-1]

        # Linear interpolation for each channel
        start_color = colors[segment_index]
        end_color = colors[segment_index + 1]

        R = int(start_color[0] + segment_t * (end_color[0] - start_color[0]))
        G = int(start_color[1] + segment_t * (end_color[1] - start_color[1]))
        B = int(start_color[2] + segment_t * (end_color[2] - start_color[2]))

        self.changeAllColor(R, G, B)
