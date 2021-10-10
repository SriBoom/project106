import numpy as np
import csv
import plotly_express as px

def dataGraph(data_path):
    with open(data_path) as file:
        df=csv.DictReader(file)
        fig=px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    marks=[]
    days=[]
    with open(data_path) as csv_file:
        reader=csv.DictReader(csv_file)
        for row in reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {'x':marks, 'y':days}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'], datasource['y'])
    print("Correlation between Marks vs Days Present in college :-  \n--->",correlation[0,1])
    
def setup():
    data_path  = "data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    
    dataGraph(data_path)
setup()