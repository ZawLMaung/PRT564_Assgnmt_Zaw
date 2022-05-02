# Input libraries
from matplotlib import pyplot
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'DriverBehaviourData.csv'
myNames = ['Occupants', 'Age', 'Sex', 'Aboriginal', 'Day', 'Alcohol', 'Drugs', 'Circumstance', 'RUMDesc', 
            'Pedestrian', 'Cyclist', 'DriverClass']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Plot the summary box
myData.plot(kind='box', subplots=True, figsize = (10,10), layout=(13,1), sharex=False, sharey=False)
pyplot.show()