import csv
import json
import pandas as pd

def convertToJsonldFunction():

    # Read Excel file into pandas DataFrame
    df = pd.read_excel('test1.xlsx')

    # Convert DataFrame to CSV file
    df.to_csv('test1.csv', index=False)

    # Define the CSV file name
    filename ="test1.csv"

    # Define the field names
    fieldnames = [
        "id_",
        "type_",
        "dateObserved__type_",
        "dateObserved__value_",
        "airQualityLevel__type_",
        "airQualityLevel__value_",
        "CO__type_",
        "CO__value_",
        "CO__unitCode_",
        "O3__type_",
        "O3__value_",
        "O3__unitCode_",
        "temp__type_",
        "temp__value_",
        "PM10__type_",
        "PM10__value_",
        "PM10__unitCode_",
        "PM2.5__type_",
        "PM2.5__value_",
     "PM2.5__unitCode_",
        "C6H6__type_",
        "C6H6__value_",
        "C6H6__unitCode_",
        "NO2__type_",
        "NO2__value_",
        "NO2__unitCode_",
        "NO__type_",
        "NO__value_",
        "NO__unitCode_",
        "SO2__type_",
        "SO2__value_",
        "SO2__unitCode_",
        "refPointOfInterest__type_",
        "refPointOfInterest__object_",
        "windDirection__type_",
        "windDirection__value_",
        "windSpeed__type_",
        "windSpeed__value_",
        "source__type_",
        "source__value_",
        "location__type_",
        "location__value__type_",
        "location__value__coordinates__0_",
        "location__value__coordinates__1_",
        "address__type_",
        "address__value__addressCountry_",
        "address__value__addressLocality_",
        "address__value__streetAddress_",
        "address__value__type_",
        "relativeHumidity__type_",
        "relativeHumidity__value_",
        "@context__0_",
        "@context__1_"
    ]

    # Define an empty list to hold the JSON objects
    json_list = []
    # Open the CSV file and read its contents
    with open('test1.csv', 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    headers = data[0]
    count=0
    # Read the CSV file and create a list of dictionaries
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            
            if count==0: 
            
                count+=1 
                continue
            else:
                # Convert each row to a nested dictionary
                json_dict = {
                    "id": row["id_"],
                    "type": row["type_"],
                    "dateObserved": {
                        "type": row["dateObserved__type_"],
                        "value": row["dateObserved__value_"]
                    },
                    "airQualityLevel": {
                        "type": row["airQualityLevel__type_"],
                        "value": row["airQualityLevel__value_"]
                        
                
                    },
                    "CO": {
                        "type": row["CO__type_"],
                        "value": float(row["CO__value_"]),
                        "unitCode": row["CO__unitCode_"]
                
                    },
                    "O3": {
                        "type": row["O3__type_"],
                        "value": float(row["O3__value_"]),
                        "unitCode": row["O3__unitCode_"]
                
                    },
                    "temperature": {
                        "type": row["temp__type_"],
                        "value": float(row["temp__value_"])
                        
            
                    },
                    "PM10": {
                        "type": row["PM10__type_"],
                        "value": float(row["PM10__value_"]),
                        "unitCode": row["PM10__unitCode_"]
                
                    },
                    "C6H6": {
                        "type": row["C6H6__type_"],
                        "value": float(row["C6H6__value_"]),
                        "unitCode": row["C6H6__unitCode_"]
                
                    },
                    "NO2": {
                        "type": row["NO2__type_"],
                        "value": float(row["NO2__value_"]),
                        "unitCode": row["NO2__unitCode_"]
                
                    },
                    "NO": {
                        "type": row["NO__type_"],
                        "value": float(row["NO__value_"]),
                        "unitCode": row["NO__unitCode_"]
                
                    },
                    "SO2": {
                        "type": row["SO2__type_"],
                        "value": float(row["SO2__value_"]),
                        "unitCode": row["SO2__unitCode_"]
                
                    },
                    "refPointOfInterest":{
                        "type": row["refPointOfInterest__type_"],
                        "object": row["refPointOfInterest__object_"]
                    },
                    "windDirection":{
                        "type": row["windDirection__type_"],
                        "value": float(row["windDirection__value_"])
                    },
                    "windSpeed":{
                        "type": row["windSpeed__type_"],
                        "value": float(row["windSpeed__value_"])
                    },
                    "source":{
                        "type": row["source__type_"],
                        "value": row["source__value_"]
                    },
                    "location":{
                        "type": row["location__type_"],
                        "value": {
                            "type": row["location__value__type_"],
                            "coordinates":
                                (float(row["location__value__coordinates__0_"]),float(row["location__value__coordinates__1_"])),
                            }
                    },
                    "address": {
                        "type": row["address__type_"],
                        "value": {
                            "addressCountry": row["address__value__addressCountry_"],
                            "addressLocality": row["address__value__addressLocality_"],
                            "streetAddress": row["address__value__streetAddress_"],
                            "type": row["address__value__type_"]
                        }
                    },
                    "relativeHumidity":{
                        "type": row["relativeHumidity__type_"],
                        "value": float(row["relativeHumidity__value_"])
                    },
                    "@context":
                    [
                        row["@context__0_"],
                        row["@context__1_"],
                    ]
                }
                json_list.append(json_dict)
    
    json_object = json.dumps(json_list, indent=4)
    
    # Writing to sample.json
    with open("sample4.json", "w") as outfile:
        outfile.write(json_object)
    # with open('json_data2.json', 'w') as outfile:
    #     json.dump(json_data.replace(" ",""), outfile)