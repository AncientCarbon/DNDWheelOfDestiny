from Model.GUIController import GUIController
import tkinter as tk


class CharacterCreatorApp:

    def __init__(self):
        self.root = tk.Tk()

        self.gui = GUIController(self.root)
        self.root.mainloop()

