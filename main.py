"""
For a user selected period, display the information of all accidents that happened in that period.

For a user selected period, produce a chart to show the number of accidents in each hour of the day (on average).

For a user selected period, retrieve all accidents caused by an accident type that contains a keyword (user entered)
e.g. collision, pedestrian, etc.

Allow the user to analyze the impact of alcohol in accidents - ie: trends over time, accident types involving alcohol.

One other "Insight" of your choice.
"""

import pandas as pd
import matplotlib.pyplot as plt


class TableData:
    def __init__(self, fileName):
        # reads the chosen file into a dataframe
        self.data = pd.read_csv(fileName)

    def getData(self):
        # returns dataframe when called
        return self.data

    def getSelectedDateData(self, startDate, endDate):
        # --- for a user selected period, display the information of all accidents that happened in the period ---

        # define the date range
        searchStart = pd.to_datetime(startDate, format='%d/%m/%Y')  # format the data into d/m/y because americans
        searchEnd = pd.to_datetime(endDate, format='%d/%m/%Y')

        # convert to timestamp format
        self.data['ACCIDENT_DATE'] = pd.to_datetime(self.data['ACCIDENT_DATE'], format='%d/%m/%Y')

        # selected data is between start and end data
        selectedData = self.data[
            (self.data['ACCIDENT_DATE'] >= searchStart) & (self.data['ACCIDENT_DATE'] <= searchEnd)]

        return selectedData

    def getAccidentPerHour(self):
        # --- For a user selected period, produce a chart to show the number of accidents in each hour of the day ---

        self.data = self.getSelectedDateData(startDate, endDate)  # dataframe is the filtered time period

        hourCount = {}  # create a dictionary for the counted accidents

        for accidentTime in self.data['ACCIDENT_TIME']:
            hour = accidentTime.split('.')[0]  # data formatted as HH.MM.SS so split at '.'

            print(hour)

            if hour in hourCount:
                hourCount[hour] += 1  # if the current hour is in the dictionary, add 1 to it
            else:
                hourCount[hour] = 1  # otherwise give it a value of 1

        return hourCount

    def getSelectedType(self, accidentType):
        # --- for a user selected period, retrieve all accidents caused by a type containing a keyword ---

        # make the searched data the filtered time dataframe
        self.data = self.getSelectedDateData(startDate, endDate)

        # selected data looks for 'Yes' or 'No' in any casings
        searchType = self.data[self.data['ACCIDENT_TYPE'].str.lower().str.contains(accidentType.lower())]

        return searchType

    def getAlcoholInvolved(self, hasAlcohol):  # get data where alcohol was involved in the accident
        searchAlcohol = self.data[self.data['ALCOHOLTIME'].str.lower().str.contains(hasAlcohol.lower())]

        return searchAlcohol


# create an instance of the TableData
table = TableData('WorkableStats.csv')

# data for selected range -- this data will be received from UI selection
startDate = '1/07/2013'
endDate = '7/07/2013'

# data for selected accident type -- this will be user entered from UI
accidentType = 'Struck Pedestrian'
hasAlcohol = 'Yes'

print("Table Data: ")
# print(table.getSelectedType(accidentType))
# print(table.getAlcoholInvolved(hasAlcohol))
table.getAccidentPerHour()
