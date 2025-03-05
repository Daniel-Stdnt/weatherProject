"""
what we need:
    first page:
    button to toggle light and dark mode --maybe? idk anymore
    search box to find cities and drop down to narrow search
    button to switch between fahreinhit and celsius
    temprature in both celsius and fahreinhit

    second page:

todo:
    larger font
    UI cleanup
    second page
    thats basically it


requirements (run these commands in the terminal before running the first time or there will be errors):
pip install requests
pip install pillow


"""
key = "d3c1372de5b34b7b917181234250303"
import tkinter as tk
from tkinter import N, S, W, E
from tkinter.font import Font
from tkinter import ttk
from PIL import Image, ImageTk #type: ignore
import requests #type: ignore
from io import BytesIO




class emptyWindow:
    
    def __init__(self,master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("600x500")

        # Configure column weights ensure equal distribution of cells in each row
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        image = Image.open("whatsmyweatherlogo.png")

        #resize the image
        max_size = (600, 600)  # Maximum width and height
        image.thumbnail(max_size)
        logo = ImageTk.PhotoImage(image)

        # create a label to display the image
        logo_label = tk.Label(self.master, image=logo)
        logo_label.grid(row=0, column=0, columnspan=3)
        #keep a reference to avoid garbage collection
        logo_label.image = logo
        
        #Row 1
        self.cityLabel = tk.Label(self.master,text="Enter your City or Zip Code")
        self.cityLabel.grid(row=1, column=0, columnspan= 1, padx=0, pady=0, sticky="e")

        self.searchInput = tk.Entry(self.master,text="search for city")
        self.searchInput.grid(row=1,column=1,columnspan=1, padx=0, pady=0)

        self.searchEnterButton = tk.Button(self.master,text="Search City/Zip", command=self.populate_listbox) #change to call GetInfo() getting weather data
        self.searchEnterButton.grid(row=1,column=2,columnspan=1,padx=0, pady=0, sticky="w")

        #Row 2 - might remove - or you can use this to show messages for validation errors or instructions
        self.tempLabel = tk.Label(self.master,text="")
        self.tempLabel.grid(row=2,column=0,columnspan=3)

        #Row 3
        self.second_window_button = tk.Button(self.master,text="Weather App Guide", command=self.open_new_window)
        self.second_window_button.grid(row=3, column=0)

        self.cityCombo = ttk.Combobox(self.master)
        self.cityCombo.grid(row=3, column=1)

        self.show_weather_button = tk.Button(self.master,text="Show The Weather", command=self.show_weather_section)
        self.show_weather_button.grid(row=3, column =2, columnspan=1, sticky="w")
        

    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        newWindow(new_window)
        """numSelect = self.cityCombo.current()
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


            #find a way to get URL images to work

            image_path = "http:" + info['current']['condition']['icon']
            new_window.weatherImage = tk.Label(new_window, text=image_path).grid(row=1,column=2)

            response = requests.get(image_path)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                photo = ImageTk.PhotoImage(image)
              #  new_window.weatherImage.config(image = photo)
              #  new_window.weatherImage.image = photo #keep a reference to avoid garbage collection

            #self.show_image(image_path)
            #the info
            print(info["current"]["temp_c"])"""

    def switchTemp(self):
        self.useCel = not self.useCel
        if self.useCel:
            self.tempTypeToggleButton['text'] = "Celsius"
        else:
            self.tempTypeToggleButton['text'] = "Fahrenhiet"
        print(self.useCel)

    def populate_listbox(self):
        self.cityCombo.set('')
        self.cityCombo['values'] = ()
        cities = self.get_cities()
        """build string for combo box"""
        if len(cities) == 0:
            self.tempLabel['text'] = "No results"
        else:
            self.tempLabel['text'] = "Choose your City"
            """get the urls from the cities and put them in a list"""
            self.tempList = [f"{city['url']}" for city in cities]
            self.urlList = self.tempList[:]

            city_list = [f"{city['id']} - {city['name']}" for city in cities]
            """populate the combo box"""
            self.cityCombo["values"] = city_list

    def show_weather_section(self):
        numSelected = self.cityCombo.current()
        
        if numSelected > -1:
            info = self.get_info()
            # Create new widgets for the weather section
            weather_label = tk.Label(self.master, text="Weather Information")
            weather_label.grid(row=4, column=0, columnspan=3, pady=10)

            weather_info = tk.Label(self.master, text="Temperature: " + str(info['current']['temp_c']) + "°C/" + str(info['current']['temp_f']) +"°F\nHumidity: " + str(info['current']['humidity']) + "%\nCondition: " + str(info['current']['condition']['text']))
            weather_info.grid(row=5, column=0, columnspan=3, pady=10)
                    
            self.image_label = tk.Label(self.master)
            self.image_label.grid(row=6, column=0, columnspan=1, sticky="w")

            # Add an image from a web URL
            image_url = "http:" + info['current']['condition']['icon']  # Replace with your image URL
            self.show_image(image_url)
        else:
            self.tempLabel['text'] = "please select a new city from the dropdown"
    
    def dark_mode(self):
        currentId = self.cityCombo.current()
        if currentId < 0:
            print("please select a city")
        else:
            print(self.cityCombo.get())


    def show_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.grid(row=6, column=1, columnspan=1, sticky="n")
            self.image_label.image = photo  # Keep a reference to avoid garbage collection



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

class newWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Weather App Guide")
        self.master.geometry("600x300")
        tk.Label(self.master, text = "Hello! And welcome to the Weather App Guide!").pack(pady=20)
        tk.Label(self.master, text = "Enter your city into the search box right below the title in the middle.").pack(pady=5)
        tk.Label(self.master, text = "Click the Search City/Zip button to list the cities in the drop down below.").pack(pady=5)
        tk.Label(self.master, text = "Select the city you want to view with the drop down.").pack(pady=5)
        tk.Label(self.master, text = "Once selected, click the Show The Weather button to view that city's weather").pack(pady=5)
        self.exit_button = tk.Button(self.master, text="Exit Guide", command=self.exitWindow).pack(pady=40)

    def exitWindow(self):
        self.master.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = emptyWindow(root)
    root.mainloop()


    
