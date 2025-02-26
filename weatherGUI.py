"""
what we need:
    first page:
    button to toggle light and dark mode
    search box to find cities and drop down to narrow search
    button to switch between fahreinhit and celsius

    second page:
    city name at the top with big font size
    temperature on the left with temperature type included
    image on right showing the weather state (sunny, rainy, ect.)

todo:
    fix up the alginment errors a little on the first
    maybe increase the size of some labels/buttons?


requirements (run these commands in the terminal before running the first time or there will be errors):
pip install requests
pip install pillow


"""
key = "4343dea060574bf3803185626252502"
import tkinter as tk
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
        self.master.title("Weather App (In Progress)")
        self.master.geometry("600x300")
        self.urlList = []

        self.new_window_button = tk.Button(self.master,text="2",command=self.open_new_window)
        self.new_window_button.place(x=0, y=0)

        self.tempTypeToggleButton = tk.Button(self.master,text="Celsius", command=self.switchTemp)
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
        numSelect = self.cityCombo.current()
        CurrentCity = self.urlList[numSelect]
        new_window = tk.Toplevel(self.master)
        new_window.title("Weather App (In Progress)")
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

            image_path = info['current']['condition']['icon']
            new_window.weatherImage = tk.Label(new_window, text=image_path).grid(row=1,column=2)

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
            self.searchLabel['text'] = "No results"
        else:
            self.searchLabel['text'] = "Choose your City"
            """get the urls from the cities and put them in a list"""
            self.tempList = [f"{city['url']}" for city in cities]
            self.urlList = self.tempList[:]

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
        numSelected = self.cityCombo.current()
        if numSelected <= -1:
            """error"""
        else:
            currentCity = self.urlList[numSelected]
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


    
