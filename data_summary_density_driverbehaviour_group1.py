# Import libraries
from pandas import read_csv
from matplotlib import pyplot

# Load the csv file using read_csv function of pandas library
myFilename = 'DriverBehaviourData.csv'
myNames = ['Occupants', 'Age', 'Sex', 'Aboriginal', 'Day', 'Alcohol', 'Drugs', 'Circumstance', 'RUMDesc', 
            'Pedestrian', 'Cyclist', 'DriverClass']

# Read csv file
myData = read_csv(myFilename, names=myNames)

# print plot
myData.plot(kind='density', subplots=True, layout=(12,1), figsize=(10, 10), sharex=False)
pyplot.show()