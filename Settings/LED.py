import machine
from Settings.Brightness import *
from time import sleep


class LED:
    np = None  # neopixel object
    amount = None  # amount of LED's
    gpio = None  # GPIO of signal wire for LED's

    def __init__(self, gpio, amount):
        self.amount = amount
        self.gpio = gpio
        self.np = neopixel.NeoPixel(machine.Pin(gpio), amount)

    # Flashes LED's x amount of times to look like police sirens. 
    def police(self, amountOfTimes):
        for k in range(amountOfTimes):
            for i in range(self.amount):
                self.changeColor(i, 0, 0, 255)

            sleep(0.05)

            for i in range(self.amount):
                self.changeColor(i, 255, 0, 0)

            sleep(0.05)

    # Turns on all LED at a specific RGB color with a desired brightness 
    def enableAll(self, r, g, b, brightness):
        bp = Brightness(self.np, self.amount)
        for i in range(self.amount):
            self.np[i] = (r, g, b)
            bp.set_brightness((r, g, b), brightness)
        self.np.write()

    # Changes the color of a single LED at a specific index
    def changeColor(self, index, r, g, b):
        self.np[index] = (r, g, b)
        self.np.write()

    # Loops through all spots in the LED and adjust the color to a desired color.
    def changeAllColor(self, r, g, b):
        for i in range(self.amount):
            self.np[i] = (r, g, b)
        self.np.write()

    def getAmount(self):
        return self.amount

    # An alternative way of using the potentiometer to adjust the LED strip
    # but the bottom method is the best way to get more out of the
    # LED spectrum when working with the full range of RGB
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

    # Takes 4 RGB values and allows for adjustment between all four of those values
    # with a corresponding potentiometer value of 0 - 100.
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
