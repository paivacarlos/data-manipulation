import re
import time
import sqlite3
import pycountry
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings("ignore")

#connect to database
conn = sqlite3.connect("../../imdb.db")

#What is the most comom movie category in the imdb?

#creating a consult on the database
consult_01 = '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type'''

#extract the result
result_01 = pd.read_sql_query(consult_01, conn)
print(result_01)

#Now we are gonna calculta the percent of the type
result_01['percent'] = (result_01['COUNT'] / result_01['COUNT'].sum()) * 100

print(result_01)

#here, qe ate gonna create a graphic with 4 categorys
#and categorys with more titles and 1 with restant

#creating a dict
others = {}

#filter percet in 5% and sum the total
others['COUNT'] = result_01[result_01['percent'] < 5]['COUNT'].sum()

#recording
others['percent'] = result_01[result_01['percent'] < 5]['percent'].sum()

#adjust the name
others['type'] = 'others'

#view
print(others)

#filter the dataframe of result
result_01 = result_01[result_01['percent'] < 5]

#append teh datafre others categorys
result_01 = result_01.append(others, ignore_index=True)

#organiza the result
result_01 = result_01.sort_values(by='COUNT', ascending=False)

#view
print(result_01.head())

#adjust labels
labels = [str(result_01['type'][i])+' '+'['+str(round(result_01['percent'][i],2))+'%'+']' for i in result_01.index]

#plot
cs = cm.Set3(np.arange(100))

#create the figure
f = plt.figure()

#Pie Plot
plt.pie(result_01['COUNT'], labeldistance= 3, radius= 1, colors= cs, wedgeprops= dict(width = 0.8))
plt.legend(labels = labels, loc = 'right', prop = {'size':6})
plt.title("Title distribution", loc='center', fontdict={'fontsize':20, 'fontweight': 20})
plt.show()










