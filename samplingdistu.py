import csv
import pandas as pd
import random 
import statistics
df = pd.read_csv("data.csv")
average = df["average"].to_list()

def take100samples():
    samples=[]
    for m in range(0,100):
      v=random.randint(1,len(average))
      samples.append(float (average[v]))
    samplesmean=statistics.mean(samples)
    return(samplesmean)
    


def meanofmeans():
  allsampleaverages=[]
  for x in range(1,1000):
      average1=take100samples()
      print(average1)
      allsampleaverages.append(average1)
  print(allsampleaverages)
  #meanofmeans1=statistics.mean(allsampleaverages)
  #print(meanofmeans1)

meanofmeans()