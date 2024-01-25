import tkinter as tk
from Model.Wheel import Wheel


class GUIController:
    def __init__(self, root, wheelData):
        """

        :param root: the Tkinter root image.
        :param wheelData: The array of strings used as options on the wheel.
        """
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
        self.wheel = Wheel(self.canvas, self.wheelData, self.root)
        self.spinButton = tk.Button(self.root, text="Spin", command=self.spinWheel)
        self.spinButton.pack()

    def update(self):
        # TODO: Update
        pass

    def onCreateCharacter(self):
        self.characterInfo.set("Character created. (placeholder)")

    def spinWheel(self):
        # TODO: make spin func
        pass
