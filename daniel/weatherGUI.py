"""
what we need:
    city at the top, with tempurature below it
    button to toggle light and dark mode
    search box to select city (dropdown if that is too complicated)
    button to switch between fahreinhit and celsius

todo:
    make a new template cause right now its literally just that temperature converter assignment

"""


"""
requirements (run these commands before running or there will be errors):
pip install requests
pip install pillow
"""
key = "4343dea060574bf3803185626252502"
import tkinter as tk
"""from breezypythongui import EasyFrame"""
from tkinter import N, S, W, E
from tkinter.font import Font
from tkinter import ttk
from PIL import Image, ImageTk #type: ignore
import requests #type: ignore


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
        self.useCel = True
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("600x300")

        self.new_window_button = tk.Button(self.master,text="placeholder",command=self.open_new_window)
        self.new_window_button.grid(row=0, column =2, columnspan=1, sticky =N+E+S+W)

        """self.cityLabel = tk.Label(self.master,text="Weather")
        self.cityLabel.grid(row=1, column=1, columnspan= 1)

        self.tempLabel = tk.Label(self.master,text=0)
        self.tempLabel.grid(row=2,column=1,columnspan=2)"""

        self.tempTypeToggleButton = tk.Button(self.master,text="switch to ferenihnt/celsus", command=self.switchTemp)
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
            
            new_window.cityName = tk.Label(new_window,text=info['location']["name"] + ", " + info['location']['region']).grid(row=0, column= 1)
            if self.useCel:
                new_window.tempLabel = tk.Label(new_window,text=info['current']['temp_c']).grid(row=1,column=0)
            else:
                new_window.tempLabel = tk.Label(new_window,text=info['current']['temp_f']).grid(row=1,column=0)


            """find a way to get URL images to work"""

            """image_path = info['current']['condition']['icon']"""
            image_path = "he2.png"
            image = Image.open(image_path)
            new_window.weatherImage = tk.PhotoImage(new_window, image).grid(row=1,column=2)

            """the info"""
            print(info["current"]["temp_c"])

    def switchTemp(self):
        self.useCel = not self.useCel
        if self.useCel:
            self.tempTypeToggleButton['text'] = "Celsius"
        else:
            self.tempTypeToggleButton['text'] = "Fahrenhiet"
        print(self.useCel)

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


    
