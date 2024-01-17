import tkinter as tk


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

class Character:
    def __init__(self):
        # TODO: Code layout
        pass

    def assignAttribute(self):
        # TODO: make the logic
        pass

    def updateAttribute(self, attribute, value):
        # TODO: updates
        pass


class WheelSpinner:
    def __init__(self):
        # Initialize attributes
        pass

    def spin(self):
        # logic
        pass


class GUIController:
    def __init__(self, master):
        # TODO: Setup layout (buttons, labels, canvas etc)
        pass

    def update(self):
        # TODO: Update
        pass


class CharacterCreatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.character = Character()
        self.wheelSpinner = WheelSpinner()
        self.gui = GUIController(self.root)

        # Setup interactions
        pass

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = CharacterCreatorApp
    app.run()
