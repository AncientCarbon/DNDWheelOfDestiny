import tkinter as tk

import numpy as np

from Model.Wheel import Wheel
from Model.SpinTypesEnum import SpinTypes


def getWheelData(spinType):
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


class GUIController:
    def __init__(self, root):
        """
        The brains of the operation
        :param root: The tk.Tk() root object
        """
        self.spinTypeLabel = None
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
        self.spinTypeLabel = tk.Label(self.root, text=self.getSpinType(), font=('Arial', 14))
        self.spinTypeLabel.pack()
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

        self.wheelData = getWheelData(self.getSpinType())
        self.color = self.colors[np.random.randint(len(self.colors))]
        self.wheel = Wheel(self.canvas, self.wheelData, self.root, self.angle, self.color)

        self.spinButton = tk.Button(self.root, text="Spin", command=self.spinWheel)
        self.spinButton.pack(padx=20, pady=20)
        self.drawArrow()

    def spinWheel(self):
        if not self.spinCount == 0:
            self.color = self.colors[np.random.randint(len(self.colors))]

        self.spinButton.config(state='disabled')
        self.spinTypeLabel.config(text=self.getSpinType())

        self.wheelData = getWheelData(self.getSpinType())

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
        self.spinButton.config(state='normal')

    def getSpinType(self):
        for spinType in SpinTypes:
            if spinType.value == self.spinCount:
                return spinType.name.capitalize()

        # TODO: Make pop-up to show that the character is done
        # TODO: Show the final stats and make them easy to copy
        self.spinCount = 0
