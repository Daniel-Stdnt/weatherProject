"""
what we need:
    city at the top, with tempurature below it
    button to toggle light and dark mode
    search box to select city (dropdown if that is too complicated)
    button to switch between fahreinhit and celsius

todo:
    make a new template cause right now its literally just that temperature converter assignment

"""
key = "4343dea060574bf3803185626252502"
import tkinter as tk
"""from breezypythongui import EasyFrame"""
from tkinter import N, S, W, E
from tkinter.font import Font
from tkinter import ttk
import requests


"""def get_cities():
        api_url = "https://api.weatherapi.com/v1/search.json?q=fishers&key=4343dea060574bf3803185626252502"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []"""

class emptyWindow:
    """find a way to have a urlList variable"""
    def __init__(self,master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("600x300")

        self.new_window_button = tk.Button(self.master,text="placeholder",command=self.open_new_window)
        self.new_window_button.grid(row=0, column =2, columnspan=1, sticky =N+E+S+W)

        """self.cityLabel = tk.Label(self.master,text="Weather")
        self.cityLabel.grid(row=1, column=1, columnspan= 1)

        self.tempLabel = tk.Label(self.master,text=0)
        self.tempLabel.grid(row=2,column=1,columnspan=2)"""

        self.tempTypeToggleButton = tk.Button(self.master,text="switch to ferenihnt/celsus")
        self.tempTypeToggleButton.grid(row=3,column=1,columnspan=1)

        self.searchInput = tk.Entry(self.master,text="search for city")
        self.searchInput.grid(row=4,column=0,columnspan=2)
        self.searchEnterButton = tk.Button(self.master,text="Search", command=self.populate_listbox)
        self.searchEnterButton.grid(row=4,column=2,columnspan=1)


        self.searchLabel = tk.Label(self.master,text="Search with the above input and narrow down search with the dropdown below")
        self.searchLabel.grid(row=6,column=1)
        self.cityCombo = ttk.Combobox(self.master)
        self.cityCombo.grid(row=7, column=1)

        self.getWeatherButton = tk.Button(self.master,text="Show Weather", command=self.get_weather_data)
        self.getWeatherButton.grid(row=7,column=2,columnspan=1)
        

    def open_new_window(self):
        CurrentCity = "noblesville-indiana-united-states-of-america"
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")
        new_window.geometry("600x300")
        info = self.get_info()
        if len(info) == 0:
            print("something went wrong")
        else:
            print("something went right")
            new_window.cityName = tk.Label(new_window,text="Placeholder").pack(pady = 20)
            print(info["current"]["temp_c"])


    def populate_listbox(self):
        cities = self.get_cities()
        """build string for combo box"""
        if len(cities) == 0:
            self.searchLabel['text'] = "we couldnt get any results, please try again"
        else:
            self.searchLabel['text'] = "choose your city with the dropdown below"
            """get the urls from the cities and put them in a list"""
            self.urlList = [f"{city['url']}" for city in cities]

            city_list = [f"{city['id']} - {city['name']}" for city in cities]
            """populate the combo box"""
            self.cityCombo["values"] = city_list
    
    def get_weather_data(self):
        currentId = self.cityCombo.current()
        if currentId < 0:
            print("please select a city")
        else:
            print(self.cityCombo.get())



    def get_cities(self):
        
        citySearched = self.searchInput.get()
        api_url = "https://api.weatherapi.com/v1/search.json?q="+citySearched+"&key="+key
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return[]
        
    def get_info(self):
        """figure out how to put the city URL here"""
        currentCity = "noblesville-indiana-united-states-of-america"
        api_url = "https://api.weatherapi.com/v1/current.json?q="+currentCity+"&key="+key
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return[]





if __name__ == "__main__":
    root = tk.Tk()
    app = emptyWindow(root)
    root.mainloop()


"""class emptyWindow(EasyFrame):

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


emptyWindow().mainloop()"""
    
