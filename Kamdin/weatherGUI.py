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
from tkinter.font import Font
from tkinter import ttk
import requests # type: ignore

def get_cities():
        api_url = "https://api.weatherapi.com/v1/search.json?q=fishers&key=4343dea060574bf3803185626252502"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []

class emptyWindow:
    """find a way to have a urlList variable"""
    def __init__(self,master):
        self.master = master
        self.master.title("Weather App (In Progress)")
        self.master.geometry("600x300")

        self.new_window_button = tk.Button(self.master,text="2",command=self.open_new_window)
        self.new_window_button.place(x=0, y=0)

        self.tempTypeToggleButton = tk.Button(self.master,text="Fahrenheit")
        self.tempTypeToggleButton.place(x=270, y=275)

        self.searchInput = tk.Entry(self.master,text="Search for City")
        self.searchInput.place(x=245, y=225)
        self.searchEnterButton = tk.Button(self.master,text="Search", command=self.populate_listbox)
        self.searchEnterButton.place(x=280, y=150)


        self.searchLabel = tk.Label(self.master,text="Search ^ Select ⇩")
        self.searchLabel.place(x=260, y=180)
        self.cityCombo = ttk.Combobox(self.master)
        self.cityCombo.place(x=235, y=200)

        self.getWeatherButton = tk.Button(self.master,text="Show Weather", command=self.get_weather_data)
        self.getWeatherButton.place(x=260, y=250)
        
    def open_new_window(self):
        CurrentCity = "noblesville-indiana-united-states-of-america"
        new_window = tk.Toplevel(self.master)
        new_window.title("Weather App (In Progress)")
        new_window.geometry("600x300")
        info = self.get_info()
        if len(info) == 0:
            print("👎")
        else:
            print("👍")
            new_window.cityName = tk.Label(new_window,text="Weather App (In Progress)").pack(pady = 20)
            print(info["current"]["temp_c"])

    def populate_listbox(self):
        cities = self.get_cities()
        """build string for combo box"""
        if len(cities) == 0:
            self.searchLabel['text'] = "No Results"
        else:
            self.searchLabel['text'] = "Choose your City"
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

    
