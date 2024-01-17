import tkinter as tk


class GUIController:
    def __init__(self):
        self.characterInfo = None
        self.root = tk.Tk()
        self.root.title("D&D Wheel of Destiny")

        self.setupWidgets()

    def setupWidgets(self):
        label = tk.Label(self.root, text="Let the wheel decide your destiny!")
        createButton = tk.Button(self.root, text="Spin", command=self.onCreateCharacter)
        characterDisplay = tk.Label(self.root, textvariable=self.characterInfo)

        label.pack()
        createButton.pack()
        characterDisplay.pack()

    def update(self):
        # TODO: Update
        pass

    def onCreateCharacter(self):
        self.characterInfo.set("Character created. (placeholder)")
