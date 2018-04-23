import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
f=open('mysql.key').readline().split()

cnx = mysql.connector.connect(user=f[0], password=f[1],
                              host='127.0.0.1',
                              database='lo_demand_timeseries')


cursor = cnx.cursor()          

query = ("SELECT * FROM 2018_demand_time")                    
cursor.execute(query)
%matplotlib inline


lo=[]

for i in cursor:
    lo.append(list(i))       

header =['Partno','Proj','Jan','Feb','Mar','Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']
df=pd.DataFrame(lo, columns=header)

df.pivot_table(index='Proj').pl

cnx.close()

