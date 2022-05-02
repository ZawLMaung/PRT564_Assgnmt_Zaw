# Input libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

# Load the csv file using read_csv function of pandas library
myFilename = 'DriverBehaviourData.csv'
myNames = ['Occupants', 'Age', 'Sex', 'Aboriginal', 'Day', 'Alcohol', 'Drugs', 'Circumstance', 'RUMDesc', 
            'Pedestrian', 'Cyclist', 'DriverClass']

# Read csv file
myData = read_csv(myFilename, names=myNames)

# Print scatter plot
scatter_matrix(myData)
pyplot.show()