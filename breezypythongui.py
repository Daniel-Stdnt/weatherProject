"""
what we need:
    city at the top, with tempurature below it
    button to toggle light and dark mode
    search box to select city (dropdown if that is too complicated)
    button to switch between fahreinhit and celsius

todo:
    make a new template cause right now its literally just that temperature converter assignment

"""

from breezypythongui import EasyFrame
from tkinter import N, S, W, E
from tkinter.font import Font
import random


class emptyWindow(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Weather App",
                            width = 600, height = 300)
        #light/dark button
        self.darkButton = self.addButton(text="placeholder", row = 0, column= 2, columnspan= 1)
        #top text, could use for displaying the city
        
        weatherFont = Font(family = "Verdana", size = 20)
        self.WeatherLabel = self.addLabel(text = "Weather",
                      row = 1, column = 1, columnspan= 2, sticky= N+W+E+S, font = weatherFont)

        #temperature output
        tempFont = Font(family = "Verdana", size = 30)
        self.WeatherLabel = self.addLabel(text=0,
                      row = 2, column = 1, columnspan= 2, sticky= N+W+E+S, font=tempFont)
        #temp type toggle
        self.tempTypeToggleButton = self.addButton(text = "Switch to Fahrenheit/Celsius", row = 3, column = 1)
        #the search
        self.searchField = self.addTextField(text = "search for city", row = 4, column = 0, columnspan= 2, sticky = W+E)
        self.searchEnterButton = self.addButton(text = "search", row = 4, column = 2)


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
    
