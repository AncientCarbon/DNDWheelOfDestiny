from Model.GUIController import GUIController
import tkinter as tk


class CharacterCreatorApp:

    def __init__(self):
        self.root = tk.Tk()
        self.gui = GUIController(self.root,
                                 {"red", "orange red", "dark orange", "orange", "gold", "yellow", "light yellow",
                                  "lemon chiffon", "light goldenrod yellow", "papaya whip", "moccasin", "peach puff",
                                  "pale goldenrod", "khaki", "dark khaki", "yellow green", "green yellow", "chartreuse",
                                  "lawn green", "lime", "lime green", "pale green", "light green",
                                  "medium spring green",
                                  "spring green", "medium sea green", "sea green", "forest green", "green",
                                  "dark green",
                                  "medium aquamarine", "aquamarine", "turquoise", "light sea green", "medium turquoise",
                                  "dark turquoise", "deep sky blue", "dodger blue", "cornflower blue", "steel blue",
                                  "royal blue", "blue", "medium blue", "dark blue", "navy", "midnight blue",
                                  "blue violet",
                                  "slate blue", "dark slate blue", "medium slate blue"})

        pass

    def run(self):
        self.root.mainloop()
