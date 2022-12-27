import re
import time
import sqlite3
import pycountry
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Tools.scripts.dutree import display
from matplotlib import cm
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings("ignore")
#sns.set_theme("whitegrid")

#connect to database
conn = sqlite3.connect("../../imdb.db")

#extract the table list
tables = pd.read_sql_query("SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table'", conn)
print(type(tables))

#view the result
print(tables.head())

#convert dataframe to list
tables = tables["Table_Name"].values.tolist()

#running the table list and extract the squema of wich one
for table in tables:
    consult = "PRAGMA TABLE_INFO({})".format(table)
    result = pd.read_sql_query(consult, conn)
    print("Schema of the table:", table)
    print(result)
    print("_"*100)
    print("\n")

