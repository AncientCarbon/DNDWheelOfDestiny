from Model.GUIController import GUIController
import tkinter as tk


class CharacterCreatorApp:

    def __init__(self):
        self.root = tk.Tk()
        num = input("Nr of sections: ")
        try:
            num = int(num)
        except ValueError:
            print("Not an int")

        numberList = [str(i) for i in range(1, num+1)]
        print(numberList)
        self.gui = GUIController(self.root, numberList)

        pass

    def run(self):
        self.root.mainloop()
