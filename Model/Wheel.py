import numpy as np


class Wheel:
    def __init__(self, canvas, descriptions, root, angle, color):
        """

        :param canvas: Tkinter canvas to draw wheel on
        :param descriptions: String of descriptions to go on the wheel
        :param root: Tkinter root
        :param angle: The angle it should be rotated to during the spin
        """
        self.color = color
        self.angle = angle
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
        radius = 150
        centerX, centerY = 300, 300
        self.canvas.create_oval(x0, y0, x1, y1, fill="white")

        for i, description in enumerate(self.descriptions):
            startAngle = anglePerSection * i - self.angle
            self.canvas.create_arc(x0, y0, x1, y1,
                                   start=startAngle,
                                   extent=anglePerSection,
                                   fill=self.getColorBrightness(self.color, i),
                                   outline="black")
            midpointAngle = (startAngle + (anglePerSection / 2)) % 360
            angle_rad = np.radians(midpointAngle)
            textX = centerX + radius * np.cos(angle_rad)
            textY = centerY - radius * np.sin(angle_rad)
            self.canvas.create_text(textX, textY,
                                    text=description,
                                    font=("Arial", 14),
                                    fill=self.getTextColor(i),
                                    angle=midpointAngle)

        self.canvas.create_oval(centerX - 50, centerY - 50, centerX + 50, centerY + 50, fill="white")

    def getColorBrightness(self, color, sectionNr):
        rgb = self.tkColorToRgb(color)
        totalSections = self.sections - 1
        midSection = (totalSections / 2)
        if sectionNr <= midSection:
            darkestColor = self.getDarkestColor(rgb)
            diff = [o - d for o, d in zip(rgb, darkestColor)]
            scale = (midSection - sectionNr) / midSection
            newRgb = [int(o - d * scale) for o, d in zip(rgb, diff)]

        else:
            scale = (sectionNr - midSection) / midSection
            newRgb = [int(value + (255 - value) * scale) for value in rgb]

        return self.rgbToHex(newRgb)

    def getDarkestColor(self, rgb):
        high = max(range(len(rgb)), key=lambda i: rgb[i])
        darkest_rgb = [0, 0, 0]
        darkest_rgb[high] = 30
        return darkest_rgb

    def tkColorToRgb(self, color):
        rgb = self.root.winfo_rgb(color)
        return [int(x / 256) for x in rgb]

    def rgbToHex(self, rgb):
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

    def getPercentage(self, sectionNr):
        minimumIntensity = 10
        stepChange = (100 - minimumIntensity) / (self.sections - 1)
        return 100 - stepChange * sectionNr

    def getTextColor(self, sectionNr):
        rgb = self.tkColorToRgb(self.getColorBrightness(self.color, sectionNr))
        luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.144 * rgb[2]) / 255
        return "black" if luminance > 0.5 else "white"

    @classmethod
    def genericWheel(cls, canvas):
        x0, y0, x1, y1 = 30, 30, 570, 570
        centerX, centerY = 300, 300
        canvas.create_oval(x0, y0, x1, y1, fill="white")
        canvas.create_text(centerX, centerY, text="Press spin!", fill="black")
        pass
