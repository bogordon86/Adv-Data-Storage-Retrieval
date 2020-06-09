<!--lint disable no-heading-punctuation-->
<!--lint enable no-heading-punctuation-->

<img src='images/Honolulu-HI.png' />

Planning a long holiday vacation in Honolulu, Hawaii! Created a climate analysis API in order to see trends in HI weather before booking the trip.

## Step 1 - Data Engineering

Used Python and Pandas to inspect the content of weather data CSV files and cleaned the data.

All of this takes place in a Jupyter notebook titled `data_engineering.ipynb`.

---

## Step 2 - Database Engineering

Next, used SQLAlchemy to model the table schemas and created a sqlite database for the tables.

This took place in a Jupyter Notebook called `database_engineering.ipynb`.


---

## Step 3 - Climate Analysis and Exploration

Used Python and SQLAlchemy to do basic climate analysis and data exploration on the weather station tables. You can find this work in the Jupyter Notebook file called `climate_analysis.ipynb`.


---

## Step 4 - Climate App

After completing an initial analysis, I designed a Flask API based on the developed queries

Below are the routes:

### Routes

* `/api/v1.0/precipitation`

  * Query for the dates and temperature observations from the last year.

* `/api/v1.0/stations`

  * Return a json list of stations from the dataset.

* `/api/v1.0/tobs`

  * Return a json list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

 * To view the code in Python that I utilized to plot the charts refer to https://github.com/bogordon86/Hawaii-Climate-Analysis/blob/master/climate-analysis.md.
 
 Here are the results:
 <img src='output_17_0.png' />
 * The average rain per month:
 <img src='output_9_1.png' />
 The average temps from last year during my proposed trip dates by day (May 1-15th).
 <img src='output_22_1.png' />
 Here is the cumulative average temp for the trip date range.
 <img src='output_24_0.png' />
 
 
