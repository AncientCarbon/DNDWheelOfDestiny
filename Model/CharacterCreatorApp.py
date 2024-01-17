from Model.Character import Character
from Model.GUIController import GUIController
from Model.WheelSpinner import WheelSpinner
import tkinter as tk


class CharacterCreatorApp:

    def __init__(self):
        index = 0
        self.root = tk.Tk()
        self.character = Character()
        self.wheelSpinner = WheelSpinner()
        self.gui = GUIController(self.root)
        # self.character.updateAttribute(self, index, self.wheelSpinner.spin())

        pass

    def run(self):
        self.root.mainloop()


