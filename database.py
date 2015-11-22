import sqlite3 as lite
import pandas as pd
#from collections import defaultdict
#Hard link to database
con = lite.connect('C:\Users\lfabrizio\AppData\Local\Continuum\Anaconda\Thinkful\database\getting_started.db')
with con:
	cur = con.cursor()
	cur.execute('drop table if exists weather;')
	cur.execute('drop table if exists cities')
	#cities table
	cur.execute('create table cities (name text, state text)')
	cur.execute("INSERT INTO cities VALUES('New York City', 'NY')") 
	cur.execute("INSERT INTO cities VALUES('Boston', 'MA')")
	cur.execute("INSERT INTO cities VALUES('Chicago', 'IL')")
	cur.execute("INSERT INTO cities VALUES('Miami', 'FL')")
	cur.execute("INSERT INTO cities VALUES('Dallas', 'TX')")
	cur.execute("INSERT INTO cities VALUES('Seattle', 'WA')")
	cur.execute("INSERT INTO cities VALUES('Portland', 'OR')")
	cur.execute("INSERT INTO cities VALUES('San Francisco', 'CA')")
	cur.execute("INSERT INTO cities VALUES('Los Angeles', 'CA')")
	cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
	cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
	#weather table
	cur.execute("create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.execute("INSERT INTO weather VALUES('New York City', 2013, 'July', 'January', 62)")
	cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January', 59)")
	cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January', 59)")
	cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January', 84)")
	cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January', 77)")
	cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January', 61)")
	cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December', 63)")
	cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', 64)")
	cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', 75)")
	cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 1776)")
	cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 100)")
	
cur.execute("select cities.name, cities.state from cities inner join weather on cities.name = weather.city where weather.warm_month like 'July'")
rows = cur.fetchall()
cols=[desc[0] for desc in cur.description]
dfc=pd.DataFrame(rows, columns=cols)
print ('The cities that are warmest in July are:')
#print(dfc)
for dff in dfc:
	print(dfc.name + ", " + dfc.state)

	
