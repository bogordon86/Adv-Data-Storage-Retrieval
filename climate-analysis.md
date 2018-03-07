

```python
# Now I used Python and SQLAlchemy to do basic climate analysis and data exploration on your new weather station tables. 
# All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

# Create a Jupyter Notebook file called climate_analysis.ipynb and use it to complete your climate analysis and data exporation.

# Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

# Use SQLAlchemy create_engine to connect to your sqlite database.

# Use SQLAlchemy automap_base() to reflect your tables into classes.
#Save a reference to those classes called Station and Measurement.
```


```python
#Dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, create_session
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, inspect, func
import datetime as dt
import numpy as np
# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float, Date

import matplotlib.pyplot as plt
import seaborn as sns
```


```python
#Use SQLAlchemy create_engine to connect to your sqlite database.
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)
conn = engine.connect()

```


```python
#Use SQLALchemy automap_base() to reflect your tables into classes.

Base = automap_base()
Base.prepare(engine, reflect = True)
Base.classes.keys()

```




    ['hawaii_measurement', 'hawaii_station']




```python
#Save a reference to those classes called Station and Measurement.
Station = Base.classes.hawaii_station
Measurement = Base.classes.hawaii_measurement
```


```python
#Start your engines! Instantiate a session.
session = Session(engine)
```


```python
#use tab when you put your cursor after the period to be able to see the columns for each class.
Measurement.
Station.
```


      File "<ipython-input-7-cff47c6b6fc6>", line 2
        Measurement.
                    ^
    SyntaxError: invalid syntax
    



```python
#Design a query to retrieve the last 12 months of precipitation data
#Select only the date and prcp values

qry1 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date <= '2017-12-31').\
        filter(Measurement.date >= '2017-01-01').all()
plot1_pd = pd.DataFrame(data=qry1, columns=["date", "prcp"])
plot1_pd = plot1_pd.set_index('date', drop=True)
plot1_pd.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create variables to use in our data plot
prcp1 = plot1_pd['prcp']
date1 = plot1_pd.index.values
#date1
#prcp1
```


```python
# Create the plot
sns.set()
plt.clf()
plt.figure(figsize=[12.8, 8])
labels = 'precipitation'
x_axis = date1
y_axis = prcp1
plt.xlabel("Date", fontsize=18)
plt.ylabel("Precipitation", fontsize=18)
plt.tick_params(axis='y', labelsize=16)
plt.tick_params(axis='x', labelsize=16, rotation=45)

# Have to plot our chart once again as it doesn't stick after being shown
plot1 = plt.plot(x_axis, y_axis, color='steelblue', linewidth=5)
plt.legend(labels=labels, loc='upper right', fontsize='large', frameon=True, edgecolor='black')
plt.show()
```


    <matplotlib.figure.Figure at 0x2126db5a278>



![png](output_9_1.png)



```python
#Use pandas to print the summary statistics for the precipitation data
plot1_pd.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1397.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.165436</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.432264</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.010000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.160644</td>
    </tr>
    <tr>
      <th>max</th>
      <td>6.250000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Design a query to calculate the total number of stations
qry2 = session.query(Station.station).count()
#qry2
```


```python
#Design a query to find the most active stations
#Do this by listing the stations and observation counts in descending order
qry3 = session.query(Measurement.station, func.count(Measurement.tobs)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.tobs).desc())
qry3.all()
```




    [('USC00519281', 2772),
     ('USC00519397', 2724),
     ('USC00513117', 2709),
     ('USC00519523', 2669),
     ('USC00516128', 2612),
     ('USC00514830', 2202),
     ('USC00511918', 1979),
     ('USC00517948', 1372),
     ('USC00518838', 511)]




```python
#Which station has the highest number of observation counts?  
qry3.limit(1).all()

```




    [('USC00519281', 2772)]




```python
#Design a query to retrieve the last twelve months of temperature observation data (tobs)
qry4 = session.query(Measurement.date, Measurement.tobs).group_by(Measurement.date).\
    filter(Measurement.date <= '2017-12-31').filter(Measurement.date >= '2017-01-01').all()
#qry4
```


```python
#Use the same query but also filter by station with highest number of temperature observation counts
qry5 = session.query(Measurement.station, Measurement.date, Measurement.tobs).group_by(Measurement.date).\
    filter(Measurement.date <= '2017-12-31').filter(Measurement.date >= '2017-01-01').\
    filter(Measurement.station=="USC00519281").all()
#qry5
```


```python
#Put queried data into dataframe so it can be plotted as histogram
plot2_pd = pd.DataFrame(data=qry5, columns=["station", "date", "tobs"])
plot2_pd = plot2_pd.set_index('date', drop=True)
plot2_pd = plot2_pd.drop(columns="station", axis=1)
plot2_pd.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tobs</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>72</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>70</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>64</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>63</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>63</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.set()
#Plot the results as a histogram with bins=12
x = plot2_pd['tobs']
num_bins = 12
# the histogram of the data
#n, bins, patches = 
plt.figure(figsize=[12.8, 8])
temp_plot = plt.hist(x, num_bins, facecolor='steelblue', label='tobs', alpha=0.9)

plt.xlabel('Temperature Observation', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.title('Temperatures Over Last Twelve Months', fontsize=18)
plt.tick_params(axis='y', labelsize=16)
plt.tick_params(axis='x', labelsize=16)
legend = plt.legend(frameon=True, edgecolor='black', fontsize='large')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
```


![png](output_17_0.png)



```python
#Write a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d 
#and return the minimum, average, and maximum temperatures for that range of dates.
def calc_temps(start_date, end_date):
    select = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    return session.query(*select).group_by(Measurement.date).filter(func.strftime("%Y-%m-%d", Measurement.date) >=start_date).\
    filter(func.strftime("%Y-%m-%d", Measurement.date) <=end_date).all()
```


```python
#Calculate the temps for my trip by running calc_temps function using matching dates from last year
data = calc_temps("2017-05-01", "2017-05-15")
```


```python
#Put the results into a dataframe so that it can be plotted
plot3_pd = pd.DataFrame(data=data, columns=["date", "tmin", "tavg", "tmax"])
plot3_pd = plot3_pd.set_index('date', drop=True)
#plot2_pd = plot2_pd.drop(columns="station", axis=1)
plot3_pd.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tmin</th>
      <th>tavg</th>
      <th>tmax</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-05-01</th>
      <td>65</td>
      <td>72.000000</td>
      <td>78</td>
    </tr>
    <tr>
      <th>2017-05-02</th>
      <td>73</td>
      <td>76.500000</td>
      <td>79</td>
    </tr>
    <tr>
      <th>2017-05-03</th>
      <td>70</td>
      <td>75.600000</td>
      <td>78</td>
    </tr>
    <tr>
      <th>2017-05-04</th>
      <td>74</td>
      <td>76.333333</td>
      <td>78</td>
    </tr>
    <tr>
      <th>2017-05-05</th>
      <td>70</td>
      <td>76.333333</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create variables for my plot
p3_date = plot3_pd.index.values
p3_tmin = plot3_pd['tmin']
p3_tavg = plot3_pd['tavg']
p3_tmax = plot3_pd['tmax']
#p3_tavg
```


```python
plt.clf()
plt.figure(figsize=[10, 6])
#Plot the min, avg, and max temperature from your previous query as a bar chart.
#Use the average temperature as the bar height.

#pmin = plt.bar(p3_date, p3_tmin, width, yerr=15)
pavg = plt.bar(p3_date, p3_tavg, yerr=15, label='Error bar is Min to Max Temp')
#pmax = plt.bar(p3_date, p3_tmax)
plt.ylabel('Temp (F)')
plt.xlabel('Trip Dates')
plt.title('Trip Avg Temp by Dates')
plt.xticks(rotation=45)
plt.legend()

plt.show()
```


    <matplotlib.figure.Figure at 0x2126e0f0780>



![png](output_22_1.png)



```python
#Calculate the total Avg Temp for my trip
totalavg = plot3_pd['tavg'].mean()
totalavg
```




    75.23111111111112




```python
#Plot the total Avg Temp for My Trip
plt.figure(figsize=[3, 6])

totalavg_plt = plt.bar('2017-05', totalavg, yerr=15, color='sandybrown', alpha=.5, label='Error bar is Min to Max Temp')
#pmax = plt.bar(p3_date, p3_tmax)

plt.ylabel('Temp (F)', fontsize=12)
plt.xlabel('1st - 15th')
plt.title('Trip Avg Temp', fontsize=14)
plt.legend()
plt.xticks(fontsize=13)
plt.yticks(np.arange(0, 120, 20), fontsize=12)

plt.show()
```


![png](output_24_0.png)



```python
#Optional Analysis
#Calculate the rainfall per weather station using the previous year's matching dates

```


```python
# Calculate the daily normals. Normals are the averages for min, avg, and max temperatures.

# Create a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic tobs that match that date string.
# Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.
# Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
# Use Pandas to plot an area plot (stacked=False) for the daily normals.
```


```python
# Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.

# Use FLASK to create your routes.

```
