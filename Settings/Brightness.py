import neopixel


class Brightness:
    np = None
    ledAmount = None

    def __init__(self, np, ledAmount):
        self.np = np
        self.ledAmount = ledAmount
        if np != neopixel.NeoPixel:
            return

    # Set all LEDs to a color scaled by a brightness factor.
    def set_brightness(self, color, brightness_factor):
        scaled_color = self.__scale_color(color, brightness_factor)
        for i in range(self.ledAmount):
            self.np[i] = scaled_color
        self.np.write()

    # Scale a color by a brightness factor.
    def __scale_color(self, color, brightness_factor):
        r, g, b = color
        return (int(r * brightness_factor), int(g * brightness_factor), int(b * brightness_factor))
