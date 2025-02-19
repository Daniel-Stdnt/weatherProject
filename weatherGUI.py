"""
what we need:


todo:
    make a new template cause right now its literally just that temperature converter assignment

"""

from breezypythongui import EasyFrame
from tkinter import N, S, W, E
import random


class emptyWindow(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Temperature Calculator",
                            width = 300, height = 150)
        self.addLabel(text = "Temperature Calculator",
                      row = 0, column = 0, columnspan= 2, sticky= N+W+E)
        #temperature input
        self.addLabel(text = "Temperature", row = 1, column= 0)
        self.temperatureInput = self.addFloatField(value=0.0, row = 1, column = 1)
        #the buttons
        self.fahrenheitButton = self.addButton(text = "Convert To Fahrenheit", row = 2, column = 0, command=self.fahrCalc)
        self.celsiusButton = self.addButton(text = "Convert to Celsius", row = 2, column = 1, command=self.celsCalc)
        #temperature output
        self.addLabel(text = "Output", row = 3, column= 0)
        self.temperatureOutput = self.addFloatField(value=0.0, row = 3, column = 1)


    def fahrCalc(self):
        cels = self.temperatureInput.getNumber()
        fahr = (cels * (9/5)) + 32
        self.temperatureOutput.setNumber(fahr)
        self.setBackground("grey")
        self.temperatureInput["foreground"] = "white"

    def celsCalc(self):
        fahr = self.temperatureInput.getNumber()
        cels = (5/9) * (fahr-32)
        self.temperatureOutput.setNumber(cels)


emptyWindow().mainloop()
    