import pandas as pd
import openpyxl
import requests
import csv
import json
import numpy as np
import uuid
import datetime
from datetime import datetime
from datetime import datetime, timedelta
from datetime import datetime, timedelta

string_series = ['01:00', '00:00', '02:00']
float_series = []

for s in string_series:
    hours, minutes = s.split(':')  # split the string into hours and minutes
    total_minutes = int(hours) * 60 + int(minutes)  # convert hours and minutes to total minutes
    total_hours = total_minutes / 60  # convert total minutes to hours
    float_value = float(total_hours)  # convert hours to float
    float_series.append(float_value)

print(float_series)  # output: [1.0, 0.0, 2.0]

# importing geopy library
from geopy.geocoders import Nominatim
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")


#AirPollutant,Concentration,DatetimeBegin,DatetimeEnd

df_O3 = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_7_13174_2020_timeseries.csv')
df_O31=df_O3.fillna(0)
df_O31["DatetimeBegin"] = df_O31["DatetimeBegin"].str.replace("+","").str.removesuffix(' 01:00')
df_O31["DatetimeEnd"] = df_O31["DatetimeEnd"].str.replace("+","").str.removesuffix(' 01:00')
df_O31["SamplingPoint"]=df_O31["SamplingPoint"].str[3:11]
print(df_O31["DatetimeBegin"])
print(df_O31["SamplingPoint"])

df_SO2 = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_1_13647_2020_timeseries.csv')
df_SO21=df_SO2.fillna(0)
df_SO21["DatetimeBegin"] = df_SO21["DatetimeBegin"].str.replace("+","").str.removesuffix(' 01:00')
["DatetimeEnd"] = df_SO21["DatetimeEnd"].str.replace("+","").str.removesuffix(' 01:00')
print(df_SO21["DatetimeBegin"])
print(df_SO21["DatetimeEnd"])


df_CO = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_10_12941_2020_timeseries.csv')
df_CO1=df_CO.fillna(0)
df_CO1["DatetimeBegin"] = df_CO1["DatetimeBegin"].str.replace("+","").str.removesuffix(' 01:00')
df_CO1["DatetimeEnd"] = df_CO1["DatetimeEnd"].str.replace("+","").str.removesuffix(' 01:00')
print(df_CO1["DatetimeBegin"])
print(df_CO1["DatetimeEnd"])


df_PM1 = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_5_11826_2020_timeseries.csv')
df_PM10=df_PM1.fillna(0)
df_PM10["DatetimeBegin"] = df_PM10["DatetimeBegin"].str.replace("+","").str.removesuffix(' 01:00')
df_PM10["DatetimeEnd"] = df_PM10["DatetimeEnd"].str.replace("+","").str.removesuffix(' 01:00')
print(df_PM10["DatetimeBegin"])
print(df_PM10["DatetimeEnd"])


df_C6H6 = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_20_13617_2020_timeseries.csv')
df_C6H61=df_C6H6.fillna(0)
df_C6H61["DatetimeBegin"] = df_C6H61["DatetimeBegin"].str.replace("+","").str.replace(' 01:00', "")
df_C6H61["DatetimeEnd"] = df_C6H61["DatetimeEnd"].str.replace("+","").str.replace(' 01:00', "")
print(df_C6H61["DatetimeBegin"])
print(df_C6H61["DatetimeEnd"])

df_PM2 = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_6001_12435_2020_timeseries.csv')
mdf_PM2= pd.merge(df_O31, df_PM2, on='DatetimeBegin', how='left')
print(mdf_PM2.columns)
df_PM25=mdf_PM2.fillna(0)
df_PM25["DatetimeBegin"] = df_PM25["DatetimeBegin"].str.replace("+","").str.replace(' 01:00', "")
df_PM25["DatetimeEnd"] = df_PM25["DatetimeEnd"].str.replace("+","").str.replace(' 01:00', "")
print(df_PM25["DatetimeBegin"])
print(df_PM25["DatetimeEnd"])

df_NO = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_38_11201_2020_timeseries.csv')
df_NO1=df_NO.fillna(0)
df_NO1["DatetimeBegin"] = df_NO1["DatetimeBegin"].str.replace("+","").str.replace(' 01:00', "")
df_NO1["DatetimeEnd"] = df_NO1["DatetimeEnd"].str.replace("+","").str.replace(' 01:00', "")
print(df_NO1["DatetimeBegin"])
print(df_NO1["DatetimeEnd"])

df_NO2 = pd.read_csv('https://ereporting.blob.core.windows.net/downloadservice/ES/ES_8_12793_2020_timeseries.csv')
df_NO21=df_NO2.fillna(0)
df_NO21["DatetimeBegin"] = df_NO21["DatetimeBegin"].str.replace("+","").str.removesuffix(' 01:00')
df_NO21["DatetimeEnd"] = df_NO21["DatetimeEnd"].str.replace("+","").str.removesuffix(' 01:00')

print(df_NO2["DatetimeBegin"])


df_weather = pd.read_excel('madrid18w.xlsx')
#df_weather["name"]=(df_weather["name"]).str.split(",")[1]
print(df_weather.columns)
#temp,humidity,windspeed

#areas=list()

df_Data_File = pd.read_excel('test1.xlsx')
#print(df_Data_File.columns)
count=1
print(df_NO2.shape[0])
print(df_Data_File)


for i, val in enumerate(df_PM10["Concentration"]):
    if val >= 0.0 and val <= 12.0:
        df_Data_File.loc[i, "airQualityLevel__value_"] = "Good"
    elif val >= 12.1 and val <= 35.4:
        df_Data_File.loc[i, "airQualityLevel__value_"] = "Moderate"
    elif val >= 35.5 and val <= 55.4:
        df_Data_File.loc[i, "airQualityLevel__value_"] = "Bad"   
    else:
        df_Data_File.loc[i, "airQualityLevel__value_"] = ""

import random
data_id=((["urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-"]*df_NO21.shape[0])+df_O31["SamplingPoint"]+"-"+df_O31["DatetimeBegin"])
df_Data_File["id_"]=data_id
df_Data_File["type_"]=["AirQualityObserved"]*df_NO21.shape[0]
df_Data_File["dateObserved__type_"]="Property"
df_Data_File["dateObserved__value_"]=df_NO21["DatetimeBegin"]+'/'+df_NO21["DatetimeEnd"]
df_Data_File["airQualityLevel__type_"]="Property"
df_Data_File["CO__type_"]="Property"
df_Data_File["CO__value_"]=df_CO1["Concentration"]
df_Data_File["CO__unitCode_"]="GP"
df_Data_File["O3__type_"]="Property"
df_Data_File["O3__value_"]=df_O31["Concentration"]
df_Data_File["O3__unitCode_"]="GQ"
df_Data_File["temp__type_"]="Property"
df_Data_File["temp__value_"]=df_weather["temp"]
df_Data_File["PM10__type_"]="Property"
df_Data_File["PM10__value_"]=df_PM10["Concentration"]
df_Data_File["PM10__unitCode_"]="GQ"

df_Data_File["PM2.5__type_"]="Property"
df_Data_File["PM2.5__value_"]=df_PM25["Concentration"]
df_Data_File["PM2.5__unitCode_"]="GQ"

df_Data_File["C6H6__type_"]="Property"
df_Data_File["C6H6__value_"]=df_C6H61["Concentration"]
df_Data_File["C6H6__unitCode_"]="GQ"

df_Data_File["NO2__type_"]="Property"
df_Data_File["NO2__value_"]=df_NO21["Concentration"]
df_Data_File["NO2__unitCode_"]="GQ"

df_Data_File["NO__type_"]="Property"
df_Data_File["NO__value_"]=df_NO1["Concentration"]
df_Data_File["NO__unitCode_"]="GQ"

df_Data_File["SO2__type_"]="Property"
df_Data_File["SO2__value_"]=df_SO21["Concentration"]
df_Data_File["SO2__unitCode_"]="GQ"

df_Data_File["refPointOfInterest__type_"]="Relationship"
df_Data_File["refPointOfInterest__object_"]="urn:ngsi-ld:PointOfInterest:"+df_O31["SamplingPoint"]+"-"+df_weather["Area"]
df_Data_File["windDirection__type_"]="Property"
df_Data_File["windDirection__value_"]=df_weather["winddir"]
df_Data_File["windSpeed__type_"]="Property"
df_Data_File["windSpeed__value_"]=df_weather["windspeed"]

df_Data_File["source__type_"]="Property"
df_Data_File["source__value_"]="https://aqportal.discomap.eea.europa.eu"

df_Data_File["location__type_"]="GeoProperty"
df_Data_File["location__value__type_"]="Point"
df_Data_File["location__value__coordinates__0_"]="40.4168"
df_Data_File["location__value__coordinates__1_"]="3.7038"

df_Data_File["address__type_"]="Property"
df_Data_File["address__value__addressCountry_"]=df_weather["Country"]
df_Data_File["address__value__addressLocality_"]=df_weather["City"]
df_Data_File["address__value__streetAddress_"]=df_weather["name"]
df_Data_File["address__value__type_"]="PostalAddress"

df_Data_File["relativeHumidity__type_"]="Property"
df_Data_File["relativeHumidity__value_"]=df_weather["humidity"]


df_Data_File["@context__0_"]="https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
df_Data_File["@context__1_"]="https://schema.lab.fiware.org/ld/context"



import pandas as pd
from openpyxl import load_workbook

# Load the Excel file into a workbook object
book = load_workbook('test1.xlsx')

# Select the sheet you want to add the data to
writer = pd.ExcelWriter('test1.xlsx') 
writer.book = book
writer.sheets.update(dict((ws.title, ws) for ws in book.worksheets))
sheet_name = 'Sheet1'

# Write the dataframe to the sheet
df_Data_File.to_excel(writer, sheet_name=sheet_name, startrow=1, startcol=0, index=False, header=False)

# Save the changes to the Excel file
writer.save()

from jsonlds1 import *
convertToJsonldFunction()










