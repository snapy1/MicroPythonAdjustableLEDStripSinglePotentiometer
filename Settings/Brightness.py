import neopixel


class Brightness:
    np = None

    def __init__(self, np):
        self.np = np
        if np != neopixel.NeoPixel:
            return

    # Set all LEDs to a color scaled by a brightness factor.
    def set_brightness(self, color, brightness_factor):
        scaled_color = self.__scale_color(color, brightness_factor)
        for i in range(60):
            self.np[i] = scaled_color
        self.np.write()

    # Scale a color by a brightness factor.
    def __scale_color(self, color, brightness_factor):
        r, g, b = color
        return (int(r * brightness_factor), int(g * brightness_factor), int(b * brightness_factor))
