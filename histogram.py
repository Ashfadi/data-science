Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> df=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\sampledata.csv',usecols=['Age'])
>>> plt.hist(df,bins=[0,20,40,60,100],ec='black')
(array([ 6., 93., 64., 12.]), array([  0,  20,  40,  60, 100]), <BarContainer object of 4 artists>)
>>> plt.xlabel('Age Group')
Text(0.5, 0, 'Age Group')
>>> plt.ylabel('Number of People')
Text(0, 0.5, 'Number of People')
>>> plt.title('Number of People in different Age Groups')
Text(0.5, 1.0, 'Number of People in different Age Groups')
>>> ticks = [10,30,50,80]
>>> labels = ["<21","21-40","41-60",">60"]
>>> plt.xticks(ticks,labels)
([<matplotlib.axis.XTick object at 0x0000023415CB41C0>, <matplotlib.axis.XTick object at 0x0000023415CB4190>, <matplotlib.axis.XTick object at 0x0000023415C9F7F0>, <matplotlib.axis.XTick object at 0x0000023415D5A550>], [Text(10, 0, '<21'), Text(30, 0, '21-40'), Text(50, 0, '41-60'), Text(80, 0, '>60')])
>>> plt.show()
>>> 