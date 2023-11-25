#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import pandas as pd

def getData():
    return pd.read_csv(input("CSV file name: "))

def getColumnNames():
    return( input("Enter latitude: "), input("Enter longitude: ") ) 

def getLocale():
    return( float(input('Enter current latitude: ')),float(input('Enter current longitude: ')) ) 

def computeDist(x1,y1,x2,y2):
    return( (x1 - x2)**2 + (y1 - y2)**2)

