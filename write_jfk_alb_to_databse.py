# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:13:29 2015

@author: Nick
"""

import sqlite3 
import pandas as pd

#!---------------------------------!#
#!------ Write Albany data --------!#
#!---------------------------------!#

# Load in the .csv files into a pandas datafraem
df = pd.read_csv('alb_data.csv',index_col = 0,
                 parse_dates = 0)
                 
# Convert column names with spaces to underscores
cols = df.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, (str, unicode)) else x)
df.columns = cols

# now remove leading _ 
cols = df.columns
cols = cols.map(lambda x: x.lstrip('_'))
df.columns = cols

# Create a SQL Databse connection
conn = sqlite3.Connection('extended_weather_db.db')

# We need to create a cursor -- an instance that can access the databse
cursor = conn.cursor()

# Write the pandas data to data base
df.to_sql('ALB',conn,index = True)

#!---------------------------------!#
#!------- Write KJFK data ---------!#
#!---------------------------------!#
# Load in the .csv files into a pandas datafraem
df = pd.read_csv('jfk_data.csv',index_col = 0,
                 parse_dates = 0)
                 
# Convert column names with spaces to underscores
cols = df.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, (str, unicode)) else x)
df.columns = cols

# now remove leading _ 
cols = df.columns
cols = cols.map(lambda x: x.lstrip('_'))
df.columns = cols

# Create a SQL Databse connection
conn = sqlite3.Connection('extended_weather_db.db')

# We need to create a cursor -- an instance that can access the databse
cursor = conn.cursor()

# Write the pandas data to data base
df.to_sql('JFK',conn,index = True)

conn.commit()
conn.close()