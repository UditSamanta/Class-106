import plotly.express as px
import csv
import pandas as pd
import numpy as np 

def plotGraph(data_path):
    with open(data_path) as csv_file:
        dataFrame = pd.read_csv(csv_file)
        print(dataFrame)
        figure = px.scatter(dataFrame, x = 'Marks In Percentage', y = 'Days Present')
        figure.show()

def setup():
    data_path = './Student Marks vs Days Present.csv'
    data_source = getdatasource(data_path)
    findCorrelation(data_source)
    plotGraph(data_path)

def getdatasource(data_path):
    Student_marks = []
    DaysPresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Student_marks.append(float(row['Marks In Percentage']))
            DaysPresent.append(float(row['Days Present']))
    return {'x':Student_marks, 'y':DaysPresent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print('correlation b/w no. of days present vs marks obtained : ', correlation[0,1])

setup()

