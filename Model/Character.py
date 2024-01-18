from Model.WheelSpinner import WheelSpinner


class Character:
    wheel = WheelSpinner

    def __init__(self):
        race = self.wheel.spin()
        pass

    def assignAttribute(self):
        # TODO: make the logic
        pass

    def updateAttribute(self, attribute, value):
        # TODO: updates
        pass
