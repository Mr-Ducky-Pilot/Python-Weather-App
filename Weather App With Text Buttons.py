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

root = Tk()
root.title("India AQI and Weather App")
root.geometry('350x200')

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

        ##icon and description
        code = weather_data["data"][0]["weather"]["code"]
        desc = weather_data["data"][0]["weather"]["description"]
        
        ##Weather Icon
##        if code==200 or code==201 or code==202:
##            ##add img t01d, to1n
##
##        if code==230 or code==231 or code==232 or code==233:
##            ##add img t04d,to4n
##
##        if code==300 or code==301 or code==302:
##            ##add img d01d, d01n
##
##        if code==500 or code==501:
##            ##add img r01d,r02n
##
##        if code==502:
##            ##add img r03d,r03n
##
##        if code==

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

##        sunup_label = Label(weather_win, text="Sun Rise Time : " + str(sun_up) ,fg=text_color, bg=weather_color,font='arial 16')
##        sunup_label.grid(row=9, column=0,columnspan=1)
##
##        sundown_label = Label(weather_win, text="||    Sun Set Time : " + str(sun_down) ,fg=text_color, bg=weather_color,font='arial 16')
##        sundown_label.grid(row=9, column=1,columnspan=1)
       

        ##Weather_Window exit button
        back_Butt = Button(weather_win, text="Go To Main Menu", command=weather_win.destroy, fg='red',bg='black',font='arial 20 bold')
        back_Butt.grid(row=10,column=0,columnspan=3,padx=10,pady=10)
        
    except Exception as e:
        api_data = "Error Connecting to API..."

##Root window ZipCode Entry Button
area_zip = Entry(root,width=40,relief=SUNKEN)
area_zip.grid(row=0,column=0,columnspan=2)

##Root window AQI Button Option
aqi_Butt = Button(root, text = "Get AQI",command=aqi_data,font='arial 20',bg='black',fg='white')
aqi_Butt.grid(row=1,column=0,columnspan=1, padx=10,pady=10)

##Root window Weather Button Option
weather_Butt = Button(root, text = "Get Weather",command=weather_data,font='arial 20',bg='black',fg='white')
weather_Butt.grid(row=1,column=1,columnspan=1,padx=10,pady=10)

##Root Window Exit Button
exit_Butt = Button(root, text="Exit App?", command=quit, fg='red',bg='black',font='arial 20 bold')
exit_Butt.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

root.mainloop()
