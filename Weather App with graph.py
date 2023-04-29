## Weather App using Tkinter
##API Key = 50ce1789429f47d28b0687b3a5b9d874
##API Request link for AQI Data : https://api.weatherbit.io/v2.0/current/airquality?postal_code=580020&country=IN&key=50ce1789429f47d28b0687b3a5b9d874
##API Return Data for AQI:
'''
{"data":[{"mold_level":0,"aqi":18,"pm10":4.84452,"co":206.947,"o3":24.6763,"predominant_pollen_type":"Molds",
            "so2":0.558794,"pollen_level_tree":0,"pollen_level_weed":0,"no2":3.29874,"pm25":4.4459,"pollen_level_grass":0}],
  "city_name":"Dharwad","lon":"75.1338","timezone":"Asia\/Kolkata","lat":"15.3478","country_code":"IN","state_code":"19"}
'''
##API Request Link for Weather Data: https://api.weatherbit.io/v2.0/current?postal_code=580020&country=IN&key=50ce1789429f47d28b0687b3a5b9d874
##API Return Data for Weather:
'''
{"data":[{"rh":93.1875,"pod":"n","lon":75.1338,"pres":932,"timezone":"Asia\/Kolkata","ob_time":"2022-08-08 19:25","country_code":"IN","clouds":77,"ts":1659986731,
    "solar_rad":0,"state_code":"19","city_name":"Hubli","wind_spd":9.6888,"wind_cdir_full":"west-southwest","wind_cdir":"WSW","slp":1002.5,"vis":16,"h_angle":-90,
    "sunset":"13:24","dni":0,"dewpt":20.1,"snow":0,"uv":0,"precip":0,"wind_dir":249,"sunrise":"00:47","ghi":0,"dhi":0,"aqi":14,"lat":15.3478,
"weather":{"icon":"c03n","code":803,"description":"Broken clouds"},"datetime":"2022-08-08:19","temp":21.3,"station":"analysis:meso","elev_angle":-58.78,"app_temp":21.9}],
              "count":1}
'''

from tkinter import *
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("India AQI and Weather App")
root.geometry('350x300')

##Function to fetch and display AQI Data for entered Pin Code
def aqi_data():
    ##Create a new window
    aqi_win = Toplevel()
    aqi_win.title("AQI Data for searched ZipCode")
    aqi_win.geometry('500x500')
    area_zip.get()
    try:
        ##requesting data from API
        aqi_req = requests.get("https://api.weatherbit.io/v2.0/current/airquality?postal_code="+area_zip.get()+"&country=IN&key=50ce1789429f47d28b0687b3a5b9d874")
        ##Store the data
        aqi_data = json.loads(aqi_req.content)
        ##Sort the API data
        aqi_lvl = aqi_data["data"][0]["aqi"]
        aqi_pm10 = aqi_data["data"][0]["pm10"]
        aqi_pm25 = aqi_data["data"][0]["pm25"]
        aqi_co = aqi_data["data"][0]["co"]
        aqi_so2 = aqi_data["data"][0]["so2"]
        aqi_no2 = aqi_data["data"][0]["no2"]
        aqi_pollen = aqi_data["data"][0]["predominant_pollen_type"]
        aqi_city =  aqi_data["city_name"]
        
        ##Background color according to AQI Value
        if aqi_lvl >=0 and aqi_lvl <= 50:
            aqi_color = "#0C0"
            aqi_category = "Good"
        elif aqi_lvl >=51 and aqi_lvl <= 100:
            aqi_color = "#FFFF00"
            aqi_category = "Satisfactory"
        elif aqi_lvl >=101 and aqi_lvl <= 200:
            aqi_color = "#ff9900"
            aqi_category = "Unhealthy For Sensitive Groups"
        elif aqi_lvl >=201 and aqi_lvl <= 300:
            aqi_color = "#FF0000"
            aqi_category = "Unhealthy"
        elif aqi_lvl >=301 and aqi_lvl <= 400:
            aqi_color = "#990066"
            aqi_category = "Very Unhealthy"
        elif aqi_lvl >= 401 and aqi_lvl <= 500:
            aqi_color = "#660000"
            aqi_category = "Hazardous"

        ##Change Root colour to category color
        aqi_win.configure(background=aqi_color)

        ##Create a Label to Print the Data
        myLabel = Label(aqi_win, text="Air Quality Index of " + aqi_city + " :", bg=aqi_color,font='arial 28 italic')
        myLabel.grid(row = 0, column=0,columnspan=2)

        lvl_label = Label(aqi_win, text = "AQI Level = " + str(aqi_lvl) + "     --     Category : " + aqi_category , bg=aqi_color,font='arial 20')
        lvl_label.grid(row=1,column=0,columnspan=1)

        pm10_label = Label(aqi_win, text = "PM-10 Concentration Level = " + str(aqi_pm10),bg=aqi_color,font='arial 20')
        pm10_label.grid(row=2,column=0,columnspan=1)

        pm25_label = Label(aqi_win, text = "PM-25 Concentration Level = " + str(aqi_pm25),bg=aqi_color,font='arial 20')
        pm25_label.grid(row=3,column=0,columnspan=1)

        co_label = Label(aqi_win, text = "CO Concentration Level = " + str(aqi_co),bg=aqi_color,font='arial 20')
        co_label.grid(row=4,column=0,columnspan=1)

        so2_label = Label(aqi_win, text = "SO-2 Concentration Level = " + str(aqi_so2),bg=aqi_color,font='arial 20')
        so2_label.grid(row=5,column=0,columnspan=1)

        no2_label = Label(aqi_win, text = "NO-2 Concentration Level = " + str(aqi_no2),bg=aqi_color,font='arial 20')
        no2_label.grid(row=6,column=0,columnspan=1)

        pollen_label = Label(aqi_win, text = "Primary Pollen Type = " + aqi_pollen, bg=aqi_color,font='arial 20')
        pollen_label.grid(row=7,column=0,columnspan=1)

        ##AQI_Window exit button
        back_Butt = Button(aqi_win, text="Go To Main Menu", command=aqi_win.destroy, fg='red',bg='black',font='arial 20 bold')
        back_Butt.grid(row=8,column=0,columnspan=2,padx=10,pady=10)
        
    except Exception as e:
        api_data = "Error Connecting to API..."


##Function to fetch weather info for the entered Pin Code
def weather_data():
    ##Create a new window
    weather_win = Toplevel()
    weather_win.title("Weather Data for searched ZipCode")
    weather_win.geometry('700x500')
    area_zip.get()
    try:
        ##requesting data from API
        weather_req = requests.get("https://api.weatherbit.io/v2.0/current?postal_code="+area_zip.get()+"&country=IN&key=50ce1789429f47d28b0687b3a5b9d874")
        ##Store the data
        weather_data = json.loads(weather_req.content)
        ##Sort the Weather API data                                                ##weather_data["data"][0]
        temp = weather_data["data"][0]["temp"]
        feel_temp = weather_data["data"][0]["app_temp"]
        humidity = weather_data["data"][0]["rh"]
        cloud = weather_data["data"][0]["clouds"]
        time = weather_data["data"][0]["pod"]
        pressure = weather_data["data"][0]["pres"]
        speed  = weather_data["data"][0]["wind_spd"]
        direction = weather_data["data"][0]["wind_dir"]
        sun_up = weather_data["data"][0]["sunrise"]
        sun_down = weather_data["data"][0]["sunset"]
        visibility = weather_data["data"][0]["vis"]
        uv = weather_data["data"][0]["uv"]
        
        city = weather_data["data"][0]["city_name"]



        ## App Color scheme
        if time == "d":
            weather_color = '#7F7FFF'                                                 ## Sky Blue #0000BF or #8787CE
            text_color = 'black'
        else:
            weather_color='#262626'
            text_color= 'white'

        ##Change widow colour to weather color
        weather_win.configure(background=weather_color)
        

        ##Create a Label to Print the Data                            ##fg=text_color, bg=weather_color
        city_Label = Label(weather_win, text="Weather in " + city + " :",fg=text_color, bg=weather_color,font='arial 28 italic')
        city_Label.grid(row = 0, column=0,columnspan=3)

        temp_label = Label(weather_win, text = " Temperature is  " + str(temp) + "° Celcius" ,fg=text_color, bg=weather_color,font='arial 16')
        temp_label.grid(row=1,column=0,columnspan=2)

        feel_label = Label(weather_win, text = " Feels like  " + str(feel_temp) + "° Celcius" ,fg=text_color, bg=weather_color,font='arial 16')
        feel_label.grid(row=2,column=0,columnspan=2)

        humidity_label = Label(weather_win, text = "Relative humidity = " + str(humidity) + "%" ,fg=text_color, bg=weather_color,font='arial 16')
        humidity_label.grid(row=3,column=0,columnspan=2)

        cloud_label = Label(weather_win, text = "Colud Coverage = " + str(cloud) +"%" ,fg=text_color, bg=weather_color,font='arial 16')
        cloud_label.grid(row=4,column=0,columnspan=2)

        pressure_label = Label(weather_win, text = "Pressure (mb) = " + str(pressure) + "%" ,fg=text_color, bg=weather_color,font='arial 16')
        pressure_label.grid(row=5,column=0,columnspan=2)

        speed_label = Label(weather_win, text = "Wind Speed = " + str(speed) + "m/s",fg=text_color, bg=weather_color,font='arial 16')
        speed_label.grid(row=6,column=0,columnspan=1)

        dir_label = Label(weather_win, text = " And Wind Direction = " + str(direction) +"°" ,fg=text_color, bg=weather_color,font='arial 16')
        dir_label.grid(row=6,column=1,columnspan=1)

        vis_label = Label(weather_win, text = "Visibility = " + str(visibility) + " KM" ,fg=text_color, bg=weather_color,font='arial 16')
        vis_label.grid(row=7,column=0,columnspan=2)

        uv_label = Label(weather_win, text = "UV  = " + str(uv) + "     (if ZERO then no data available)" ,fg=text_color, bg=weather_color,font='arial 16')
        uv_label.grid(row=8,column=0,columnspan=2)
       
        ##Weather_Window exit button
        back_Butt = Button(weather_win, text="Go To Main Menu", command=weather_win.destroy, fg='red',bg='black',font='arial 20 bold')
        back_Butt.grid(row=10,column=0,columnspan=3,padx=10,pady=10)
        
    except Exception as e:
        api_data = "Error Connecting to API..."

def plot_graph():
    plot_win = Toplevel()
    plot_win.title('data veri')
    plot_win.geometry('200x200')
    area1_zip.get()
    area2_zip.get()
    area3_zip.get()
    try:
    ##requesting data from API for city 1
        graph_req1 = requests.get("https://api.weatherbit.io/v2.0/current?postal_code="+area1_zip.get()+"&country=IN&key=50ce1789429f47d28b0687b3a5b9d874")
        graph_data1 = json.loads(graph_req1.content)
        ##AQI data for City 1:
        aqi_lvl1 = graph_data1["data"][0]["aqi"]

        ##requesting data from API for city 2
        graph_req2 = requests.get("https://api.weatherbit.io/v2.0/current?postal_code="+area2_zip.get()+"&country=IN&key=50ce1789429f47d28b0687b3a5b9d874")
        graph_data2 = json.loads(graph_req2.content)
        ##AQI data for City 2:
        aqi_lvl2 = graph_data2["data"][0]["aqi"]

        ##requesting data from API for city3
        graph_req3 = requests.get("https://api.weatherbit.io/v2.0/current?postal_code="+area3_zip.get()+"&country=IN&key=50ce1789429f47d28b0687b3a5b9d874")
        graph_data3 = json.loads(graph_req3.content)
        ##AQI data for City 3:
        aqi_lvl3 = graph_data3["data"][0]["aqi"]

        lab1 = Label(plot_win, text=aqi_lvl1).grid(row=0,column=0)
        lab2 = Label(plot_win, text=aqi_lvl2).grid(row=1,column=0)
        lab3 = Label(plot_win, text=aqi_lvl3).grid(row=2,column=0)
        
        x = np.array(['City 1', 'City 2', 'City 3'])
        y = np.array([api_lvl1,api_lvl2,api_lvl3])
        plt.xlabel('AQI Level')
        plt.ylabel('Cities')
        plt.title('AQI Graph')
        plt.bar(x,y, color='hotpink')
        plt.show()
        
    except Exception as e:
        api_data = "Error Connecting to API..."

def graph_data():
     ##Create a new window
    graph_win = Toplevel()
    graph_win.title("Plot a Graph")
    graph_win.geometry('300x300')

    ##main label
    main_label = Label(graph_win, text="Enter Pincodes for 3 Cities to get AQI graph")
    main_label.grid(row=0,column=0,columnspan=2)

    ##Area 1 pincode:
    global area1_zip
    area1_label = Label(graph_win, text = "City 1 : ", font='arial 20',bg='black',fg='white')
    area1_label.grid(row=1,column=0)
    area1_zip = Entry(graph_win,width=40,relief=SUNKEN)
    area1_zip.grid(row=1,column=1)
    ##Area 2 Pincode:
    global area2_zip
    area2_label = Label(graph_win, text = "City 2 : ", font='arial 20',bg='black',fg='white')
    area2_label.grid(row=2,column=0)
    area2_zip = Entry(graph_win,width=40,relief=SUNKEN)
    area2_zip.grid(row=2,column=1)
    ##Area 3 Pincode:
    global area3_zip
    area3_label = Label(graph_win, text = "City 3 : ", font='arial 20',bg='black',fg='white')
    area3_label.grid(row=3,column=0)
    area3_zip = Entry(graph_win,width=40,relief=SUNKEN)
    area3_zip.grid(row=3,column=1)

    ##Graph Button
    plot_Butt = Button(graph_win, text = "Plot",command=plot_graph , font='arial 20', bg='black', fg='white')
    plot_Butt.grid(row=4,column=0,columnspan=2)

    ##Main Menu Button
    back_Butt = Button(graph_win, text="Go To Main Menu", command=graph_win.destroy, fg='red',bg='black',font='arial 20 bold')
    back_Butt.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

##Root window ZipCode Entry Button
area_zip = Entry(root,width=40,relief=SUNKEN)
area_zip.grid(row=0,column=0,columnspan=2)

##Root window AQI Button Option
aqi_Butt = Button(root, text = "Get AQI",command=aqi_data,font='arial 20',bg='black',fg='white')
aqi_Butt.grid(row=1,column=0,columnspan=1, padx=10,pady=10)

##Root window Weather Button Option
weather_Butt = Button(root, text = "Get Weather",command=weather_data,font='arial 20',bg='black',fg='white')
weather_Butt.grid(row=1,column=1,columnspan=1, padx=10,pady=10)

##Graph Window Button:
grp_Butt = Button(root, text = "Plot a Graph", command=graph_data , font='arial 20', bg='black', fg='white')
grp_Butt.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

##Root Window Exit Button
exit_Butt = Button(root, text="Exit App?", command=quit, fg='red',bg='black',font='arial 20 bold')
exit_Butt.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

root.mainloop()
