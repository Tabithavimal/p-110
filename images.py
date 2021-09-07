import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv('images.csv')
data=df["temp"].tolist()
populationmain=statistics.mean(data)
populationstd=statistics.stdev(data)
print(populationmain)
print(populationstd)
def randomsetofmeans(counter):
    dataset=[]
    for index in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def showfigure(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    meanlist=[]
    for index in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanlist.append(setofmeans)

    showfigure(meanlist)
    samplemean=statistics.mean(meanlist)
    samplestd=statistics.stdev(meanlist)
    print(samplemean)
    print(samplestd)

setup()