import pandas as pd

class TableData:
    def __init__(self, fileName):
        # reads the chosen file into a dataframe
        self.data = pd.read_csv(fileName)

    def getData(self):
        # returns dataframe when called
        return self.data

    def getSelectedDateData(self, startDate, endDate):
        # define the date range
        searchStart = pd.to_datetime(startDate, format= '%d/%m/%Y') # format the data into d/m/y because americans
        searchEnd = pd.to_datetime(endDate, format= '%d/%m/%Y')

        # convert to timestamp format
        self.data['ACCIDENT_DATE'] = pd.to_datetime(self.data['ACCIDENT_DATE'], format= '%d/%m/%Y')

        # selected data is between start and end data
        selectedData = self.data[(self.data['ACCIDENT_DATE'] >= searchStart) & (self.data['ACCIDENT_DATE'] <= searchEnd)]

        return selectedData






# create an instance of the TableData
table = TableData('Stats.csv')

# data for selected range -- this data will be received from UI selection
startDate = '3/07/2013'
endDate = '4/07/2013'

# get all the data
print("Table Data: ")
print(table.getSelectedDateData(startDate, endDate))
print()

