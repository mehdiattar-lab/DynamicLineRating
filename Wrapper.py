# Copyright 2025 Tampere University.
# This software was developed within Hedge-IoT project, co-funded by European Union.
# This source code is licensed under the MIT license. See LICENSE in the repository root directory.
# This software can utilize the dynamic line rating of over head lines in power systems either based on IEEE 738 standard or CIGRE 601 standard (similar standards)
# Author: Mehdi Attar <mehdi.attar@tuni.fi>




import __init__
import conductor

import pandas as pd
import matplotlib.pyplot as plt


import csv
import os

##################################################
##################################################
#Implementiation without considering the conductor temperature
#changes from one hour to another. so the conductor temperature is fixed at 80 degree centigrade


# Get the current working directory
current_directory = os.getcwd()
#print(current_directory)

# Join the current directory with the filename using os.path.join
file_path_weather = os.path.join(current_directory, 'weather.csv')
#print(file_path_weather)
file_path_irradiance = os.path.join(current_directory, 'irradiance.csv')#

# Open the CSV file for weather and solar irradiance
weather = pd.read_csv(file_path_weather)#
irradiance = pd.read_csv(file_path_irradiance)
max_allowable_current = []
temperature_plot = []
wind_speed_plot = []
current_difference = []


for i in range (0,8759): # for one year simulation

    ambient_temperature = weather.iloc[i, 0]
    air_temperature = ambient_temperature.split(',')[5]
    wind_speed = ambient_temperature.split(',')[6]
    try:
        air_temperature = air_temperature.strip('"')    # air_temperature
        air_temperature=round(float(air_temperature))
        temperature_plot.append([])
        temperature_plot[i].append(air_temperature)
    except TypeError as e:
        print("value error",e)
    try:
        wind_speed = wind_speed.strip('"')              # wind_speed
        wind_speed = float(wind_speed)/20
        wind_speed = round(float(wind_speed))
        wind_speed_plot.append([])
        wind_speed_plot[i].append(wind_speed/20)
    except TypeError as e:
        print("value error",e)
    
    solar_irradiance = irradiance.iloc[i, 0]

    try:
        solar_irradiance = solar_irradiance.split(',')
        value=solar_irradiance[5]
        value = value.strip('"')
        solar_irradiance = float(value)
    except TypeError as e:
        print("value error",e)    
    angle_of_attack = 45      # input parameter
    conductor_temperature = 75.0   # input parameter
    horizontal_angle = 0   # input parameter
    elevation = 93   # input parameter

    ieee = __init__.thermal_rating(
        air_temperature,
        wind_speed,
        angle_of_attack,
        solar_irradiance,
        conductor.drake_constants_ieee738,
        conductor_temperature,
        horizontal_angle,
        elevation,
        standard="ieee"
    )

    max_allowable_current.append([])
    max_allowable_current[i].append(ieee)
    
    ########################################### for reporting an plotting

    current_difference.append([])
    current_difference[i].append(0)
    current_difference[i] = (int(max_allowable_current[i][0]) - 845)/845  # percentage of current difference


    #print(type(max_allowable_current[0]))
    #print(max_allowable_current[0])    
    
    Jan_Mar = 0
    count_1 = 0

    Apr_Jun = 0
    count_2 = 0

    Jul_Sep = 0
    count_3 = 0

    Oct_Dec = 0
    count_4 = 0

for i in range (0,8759):
    if i < 2190:
        Jan_Mar = current_difference[i] + Jan_Mar
        count_1 = count_1 + 1
    elif 2190 <= i < 4380:
        Apr_Jun = current_difference[i] + Apr_Jun
        count_2 = count_2 + 1
    elif 4380 <= i < 6570:
        Jul_Sep = current_difference[i] + Jul_Sep
        count_3 = count_3 + 1
    else:
        Oct_Dec = current_difference[i] + Oct_Dec
        count_4 = count_4 + 1

Jan_Mar = Jan_Mar/count_1
print(Jan_Mar)
Apr_Jun = Apr_Jun/count_2
print(Apr_Jun)
Jul_Sep = Jul_Sep/count_3
print(Jul_Sep)
Oct_Dec = Oct_Dec/count_4
print(Oct_Dec)

plt.figure(figsize=(8, 4))
plt.plot(max_allowable_current)
plt.xlabel('Hour of the year')
plt.ylabel('Allowable current')
plt.grid(True)


plt.figure(figsize=(8, 4))
plt.plot(temperature_plot)
plt.plot(wind_speed_plot)
plt.plot(temperature_plot, label='Temperature', color='red')
plt.plot(wind_speed_plot, label='Wind speed', color='blue')
plt.xlabel('Hour of the year')
plt.legend()
plt.grid(True)


plt.figure(figsize=(8, 4))
plt.plot(current_difference)
x_values = range(8760)
plt.plot(x_values[0:2190],[Jan_Mar]*2190, label=f'Jan-Mar {Jan_Mar*100:.2f}%')
plt.plot(x_values[2190:4380],[Apr_Jun]*2190, label=f'Apr-Jun {Apr_Jun*100:.2f}%')
plt.plot(x_values[4380:6570],[Jul_Sep]*2190, label=f'Jul-Sep {Jul_Sep*100:.2f}%')
plt.plot(x_values[6570:],[Oct_Dec]*2190, label=f'Oct-Dec {Oct_Dec*100:.2f}%')
plt.xlabel('Hour of the year')
plt.legend()
plt.ylabel('Capacity of the line %')
plt.grid(True)
plt.title('wind speed 0')

plt.show()
#print(max_allowable_current)


############################################################
############################################################
# # Implementiation with considering the conductor temperature
# # changes from one hour to another. so the conductor temperature at he first hour is 80 degree centigrade
# # and then it changes depnding on its carrying current and ambient teperature, and wind speed

# # Get the current working directory
# current_directory = os.getcwd()

# # Join the current directory with the filename using os.path.join
# file_path_weather = os.path.join(current_directory, 'weather.csv')
# file_path_irradiance = os.path.join(current_directory, 'irradiance.csv')

# # Open the CSV file
# weather = pd.read_csv(file_path_weather)
# irradiance = pd.read_csv(file_path_irradiance)
# max_allowable_current = []
# temperature_plot = []
# wind_speed_plot = []
# load_current = []
# for i in range (0,8760):
#     load_current.append([])
#     load_current[i].append(500)

# print(load_current)


# #print(weather)
# #print(irradiance)

# #solar_irradiance = irradiance.iloc[12, 5]
# #print(solar_irradiance)


# for i in range (0,8759):

#     #print(i)
#     ambient_temperature = weather.iloc[i, 0]
#     air_temperature = ambient_temperature.split(',')[5]
#     wind_speed = ambient_temperature.split(',')[6]
#     try:
#         air_temperature = air_temperature.strip('"')    # air_temperature
#         air_temperature=round(float(air_temperature))
#         temperature_plot.append([])
#         temperature_plot[i].append(air_temperature)
#     except TypeError as e:
#         print("value error",e)
#     try:
#         wind_speed = wind_speed.strip('"')              # wind_speed
#         wind_speed = round(float(wind_speed))
#         wind_speed_plot.append([])
#         wind_speed_plot[i].append(wind_speed)
#     except TypeError as e:
#         print("value error",e)
    
#     solar_irradiance = irradiance.iloc[i, 0]

#     try:
#         solar_irradiance = solar_irradiance.split(',')
#         value=solar_irradiance[5]
#         value = value.strip('"')
#         solar_irradiance = float(value)
# #        print(solar_irradiance)
#     except TypeError as e:
#         print("value error",e)    


# #    ambient_temperature = 40.0
# #    wind_speed = 0.61
#     angle_of_attack = 45
# #    solar_irradiation = 1000
#     conductor_temperature = 85.0
#     horizontal_angle = 0
#     elevation = 93

# #    print(air_temperature)
# #    print(wind_speed)
# #    print(solar_irradiance)


#     ieee = __init__.thermal_rating(
#         air_temperature,
#         wind_speed,
#         angle_of_attack,
#         solar_irradiance,
#         conductor.drake_constants,
#         conductor_temperature,
#         horizontal_angle,
#         elevation,load_current,
#         standard="ieee")

#     #print(ieee)
#     max_allowable_current.append([])
#     max_allowable_current[i].append(ieee)

#     #print(type(max_allowable_current[0]))
#     #print(max_allowable_current[0])    
    
    
    
    
    
    
    
    
    
    
    
#     #print ("2")

#     # cigre = __init__.thermal_rating(
#     #     ambient_temperature,
#     #     wind_speed,
#     #     angle_of_attack,
#     #     solar_irradiation,
#     #     conductor.drake_constants,
#     #     conductor_temperature,
#     #     horizontal_angle,
#     #     elevation=elevation,
#     #     standard="cigre"
#     # )

# plt.figure(figsize=(8, 4))
# plt.plot(max_allowable_current)
# plt.xlabel('hour of the year')
# plt.ylabel('allowable current')
# plt.grid(True)


# plt.figure(figsize=(8, 4))
# plt.plot(temperature_plot)
# plt.plot(wind_speed_plot)

# # Plot the first graph (y = x^2)
# plt.plot(temperature_plot, label='Temperature', color='red')

# # Plot the second graph (y = x^3)
# plt.plot(wind_speed_plot, label='Wind speed', color='blue')

# plt.xlabel('hour of the year')
# plt.legend()
# plt.grid(True)


# plt.show()
