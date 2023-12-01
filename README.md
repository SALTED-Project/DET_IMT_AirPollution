# Air Pollution Data Enrichment Toolchain by IMT

## Introduction
This Python script processes air quality data for Madrid obtained from various sources within the SALTED project. It converts the time format, retrieves data from different pollutants, and merges datasets for further analysis. The processed data is then formatted and converted into NGSI-LD format.

#### 📝 Description
-   The script converts time strings to a float representation.
-   Air quality data for O3, SO2, CO, PM1, C6H6, PM2, NO, and NO2 is retrieved from respective URLs (European Open Portal or Madrid open portal).
-   Weather data is obtained from visual crossing in excel format.
-   The processed data is merged and categorized based on air quality levels.
-   The final dataset is saved in `filename.xlsx`
-   This dataset is used to convert the data into NGSI-LD format.

#### :sparkles: Other components
N/A

#### Data File Structure
The Excel file (`filename.xlsx`) utilized in the DET contains a header row with pollutants name and attributes like CO, O3, SO2, PM10, C6H6, PM2.5, NO2, NO, and associated concentration values with units and location of the sensors.

#### 📧 Contact
All code located in this repository has been developed by Institut Mines Telecom (IMT).

## Installation
### Prerequisites
Make sure you have Python installed on your machine. You can install the required libraries using the following command:
pip install pandas 
openpyxl requests geopy

### Usage
Run the Script
python filename.py

## Acknowledgment 
This work was supported by the European Commission CEF Programme by means of the project SALTED ‘‘Situation-Aware Linked heterogeneous Enriched Data’’ under the Action Number 2020-EU-IA-0274.

## License
 N/A



