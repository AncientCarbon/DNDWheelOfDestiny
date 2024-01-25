import numpy as np


class Wheel:
    def __init__(self, canvas, descriptions):
        self.canvas = canvas
        self.sections = len(descriptions)
        self.descriptions = descriptions
        self.drawWheel()

    def drawWheel(self):
        anglePerSection = 360 / self.sections
        x0, y0, x1, y1 = 30, 30, 570, 570
        center = 300
        self.canvas.create_oval(x0, y0, x1, y1, fill="white")
        colors = ["red", "orange red", "dark orange", "orange", "gold", "yellow", "light yellow",
                  "lemon chiffon", "light goldenrod yellow", "papaya whip", "moccasin", "peach puff",
                  "pale goldenrod", "khaki", "dark khaki", "yellow green", "green yellow", "chartreuse",
                  "lawn green", "lime", "lime green", "pale green", "light green", "medium spring green",
                  "spring green", "medium sea green", "sea green", "forest green", "green", "dark green",
                  "medium aquamarine", "aquamarine", "turquoise", "light sea green", "medium turquoise",
                  "dark turquoise", "deep sky blue", "dodger blue", "cornflower blue", "steel blue",
                  "royal blue", "blue", "medium blue", "dark blue", "navy", "midnight blue", "blue violet",
                  "slate blue", "dark slate blue", "medium slate blue"]

        for i in range(self.sections):
            startAngle = anglePerSection * i
            endAngle = anglePerSection * (i + 1)
            self.canvas.create_arc(x0, y0, x1, y1,
                                   start=startAngle,
                                   extent=anglePerSection,
                                   fill=colors[np.random.randint(len(colors))],
                                   outline="black")

        self.canvas.create_oval(center-85, center-85, center+85, center+85, fill="white")