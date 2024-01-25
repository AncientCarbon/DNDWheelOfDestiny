import numpy as np
import tkinter as tk

class Wheel:
    def __init__(self, canvas, descriptions, root):
        """
        :param canvas: canvas object to draw on.
        :param descriptions: An array of strings containing information about the field.
        """
        self.root = root
        self.canvas = canvas
        self.sections = len(descriptions)
        self.descriptions = descriptions
        self.drawWheel()

    def drawWheel(self):
        """
        Draws the GUI wheel with a random selection of colors. Uses amount of string objects as amount of fields
        """
        anglePerSection = 360 / self.sections
        x0, y0, x1, y1 = 30, 30, 570, 570
        center = 300
        self.canvas.create_oval(x0, y0, x1, y1, fill="white")
        colors = ["red", "blue", "green", "yellow"]

        color = colors[np.random.randint(len(colors))]

        for i in range(self.sections):
            startAngle = anglePerSection * i
            self.canvas.create_arc(x0, y0, x1, y1,
                                   start=startAngle,
                                   extent=anglePerSection,
                                   fill=self.getColorBrightness(color, i),
                                   outline="black")

        self.canvas.create_oval(center - 85, center - 85, center + 85, center + 85, fill="white")

    def getColorBrightness(self, color, sectionNr):
        rgb = self.tkColorToRgb(color)
        totalSections = self.sections - 1
        midSection = (totalSections / 2)
        minRgbValue = 30

        if sectionNr < midSection:
            scale = sectionNr / midSection * 0.9
            newRgb = [max(int(value * scale), minRgbValue) for value in rgb]

        elif sectionNr == midSection:
            newRgb = rgb

        else:
            scale = (sectionNr - midSection) / midSection
            newRgb = [int(value + (255 - value) * scale) for value in rgb]

        return self.rgbToHex(newRgb)

    def tkColorToRgb(self, color):
        rgb = self.root.winfo_rgb(color)
        return [int(x / 256) for x in rgb]

    def rgbToHex(self, rgb):
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

    def getPercentage(self, sectionNr):
        minimumIntensity = 10
        stepChange = (100 - minimumIntensity) / (self.sections - 1)
        return 100 - stepChange * sectionNr
