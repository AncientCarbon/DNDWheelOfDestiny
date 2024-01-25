import tkinter as tk

import numpy as np

from Model.Wheel import Wheel


class GUIController:
    def __init__(self, root, wheelData):
        """

        :param root: the Tkinter root.
        :param wheelData: The array of strings used as options on the wheel.
        """
        self.targetAngle = None
        self.decayFactor = 0.99
        self.anglePerFrame = 10
        self.color = None
        self.angleRotated = None
        self.minRotations = None
        self.spinSpeed = None
        self.angle = 0
        self.spinButton = None
        self.wheel = None
        self.canvas = None
        self.characterInfo = None
        self.root = root
        self.root.title("D&D Wheel of Destiny")
        self.wheelData = wheelData
        self.setupWidgets()

    def setupWidgets(self):
        label = tk.Label(self.root, text="Let the wheel decide your destiny!")
        characterDisplay = tk.Label(self.root, textvariable=self.characterInfo)

        label.pack()
        characterDisplay.pack()

        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
        self.color = colors[np.random.randint(len(colors))]
        self.wheel = Wheel(self.canvas, self.wheelData, self.root, self.angle, self.color)
        self.spinButton = tk.Button(self.root, text="Spin", command=self.spinWheel)
        self.spinButton.pack()

    def update(self):
        # TODO: Update
        pass

    def onCreateCharacter(self):
        self.characterInfo.set("Character created. (placeholder)")

    def spinWheel(self):
        self.angleRotated = 0
        self.targetAngle = np.random.randint(360, 5 * 360)
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
