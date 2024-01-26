from Model.GUIController import GUIController
import tkinter as tk


class CharacterCreatorApp:

    def __init__(self):
        self.data = []
        self.root = tk.Tk()
        with open("Model/Strength.txt") as doc:
            for line in doc:
                self.data.append(line)

        self.gui = GUIController(self.root, self.data)
        self.root.mainloop()

