# Input libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

# Load the csv file using read_csv function of pandas library
myFilename = 'RoadCrashData.csv'
myNames = ['Month', 'WeekDay','DaySpan', 'Light', 'Weather', 'Traffic', 'Surface', 'Division', 'TowFactor',
            'HeavyVehicle', 'LGA/Area', 'Rural/Urban', 'SpeedRelated', 'RoadClass']

# Read csv file
myData = read_csv(myFilename, names=myNames)

# Print scatter plot
scatter_matrix(myData)
pyplot.show()