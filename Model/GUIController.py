import tkinter as tk

import numpy as np

from Model.Wheel import Wheel
from Model.SpinTypesEnum import SpinTypes


class GUIController:
    def __init__(self, root):
        """

        :param root: the Tkinter root.
        :param wheelData: The array of strings used as options on the wheel.
        """
        self.colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
        self.spinCount = 0
        self.targetAngle = None
        self.decayFactor = 0.99
        self.anglePerFrame = 10
        self.color = None
        self.angleRotated = None
        self.angle = np.random.randint(0, 359)
        self.spinButton = None
        self.wheel = None
        self.canvas = None
        self.root = root
        self.root.title("D&D Wheel of Destiny")
        self.wheelData = None
        self.setupWidgets()

    def setupWidgets(self):
        label = tk.Label(self.root, text="Let the wheel decide your destiny!", font=('Arial', 18))
        label.pack(padx=20, pady=20)

        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.wheel = Wheel.genericWheel(self.canvas)

        self.spinButton = tk.Button(self.root, text="Spin", command=self.spinWheel)
        self.spinButton.pack(padx=20, pady=20)
        self.drawArrow()

    def spinWheel(self):

        # Picks a random color from the colors list
        self.color = self.colors[np.random.randint(len(self.colors))]

        self.wheelData = self.getWheelData(self.getSpinType())

        self.wheel = Wheel(self.canvas, self.wheelData, self.root, self.angle, self.color)
        # Resets the wheel
        self.angleRotated = 0
        self.anglePerFrame = 10

        # Gets a random amount of rotation between 0 and 5 full spins before initiating slow-down
        self.targetAngle = np.random.randint(0, 5 * 360)
        self.rotateWheel()

    def rotateWheel(self):
        if self.angleRotated > self.targetAngle:
            # deceleration
            self.anglePerFrame *= self.decayFactor

        if self.anglePerFrame > 0.3:
            self.angle += self.anglePerFrame
            self.angle = self.angle % 360

            self.canvas.delete("all")
            self.wheel = Wheel(self.canvas, self.wheelData, self.root, self.angle, self.color)

            self.angleRotated += self.anglePerFrame

            self.root.after(10, self.rotateWheel)
            self.drawArrow()

        else:
            self.calculateResult()

    def drawArrow(self):
        arrowLength = 50
        arrowWidth = 20
        centerX = 300
        centerY = 50
        points = [
            centerX + arrowWidth // 2, centerY - arrowLength,
            centerX - arrowWidth // 2, centerY - arrowLength,
            centerX, centerY
        ]
        self.canvas.create_polygon(points, fill="red", outline="white")

    def calculateResult(self):
        anglePerSection = 360 / len(self.wheelData)
        adjustedAngle = (self.angle + 90) % 360
        sectionIndex = (int(adjustedAngle / anglePerSection)) % len(self.wheelData)
        selectedField = self.wheelData[sectionIndex]
        spinType = self.getSpinType()
        print(spinType, ":", selectedField)
        self.spinCount += 1

    def getSpinType(self):
        for spinType in SpinTypes:
            if spinType.value == self.spinCount:
                return spinType.name.capitalize()

        return ["Error1", "Error2", "Error3"]

    def getWheelData(self, spinType):
        fileName = spinType
        filePath = f"Model/SpinTypes/{fileName}"
        fileData = []
        try:
            with open(filePath) as file:
                for line in file:
                    fileData.append(line.strip())
            return fileData
        except FileNotFoundError:
            print(f"File not found: {filePath}")
        pass

