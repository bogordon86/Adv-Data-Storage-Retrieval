#Dependencies
# Import Dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify
import datetime as dt
import numpy as np

#################################################
# Database Setup
#################################################
# Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.

# Use FLASK to create your routes.

# Create an engine for the chinook.sqlite database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
#Base.classes.keys()

# Save references to the invoices and invoice_items tables
Station = Base.classes.hawaii_station
Measurement = Base.classes.hawaii_measurement

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
         f"Avalable Routes:<br/>"
         
         f"/api/v1.0/precipitation<br/>"
         f"- Dates and Temperature Observations from last year<br/>"
         
         f"/api/v1.0/stations<br/>"
         f"- List of weather stations from the dataset<br/>"

         f"/api/v1.0/tobs<br/>"
         f"- List of temperature observations (tobs) from the previous year<br/>"

         f"/api/v1.0/<start><br/>"
         f"- List of min, avg, and max temperature for a given start date<br/>"
        
         f"/api/v1.0/<start>/<end><br/>"
         f"- List of min, avg, and max temperature for a given start/end range<br/>"
    )
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of Dates and precipitation from last year"""
    # Query Invoices for Billing Country
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date <= '2017-12-31').\
        filter(Measurement.date >= '2017-01-01').all()

    # Convert the query results into a dictionary using date as the key and precipitation as the value
    all_prcp = []
    for result in results:
        prcp_dict = {}
        prcp_dict["date"] = result[0]
        prcp_dict["prcp"] = float(result[1])

        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)
    
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of weather stations from the dataset """
    # Query all stations
    results = session.query(Station.station).all()
    
    stations_list = list(np.ravel(results))
    
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations from the previous year """
    # Query for all temperature observations from previous year
    results = session.query(Measurement.date, Measurement.tobs).\
        group_by(Measurement.date).\
        filter(Measurement.date <= '2017-12 31').\
        filter(Measurement.date >= '2017-01-01').all()

    tobs_list = list(np.ravel(results))
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
    """Return a list of min, avg, max for specific dates"""
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results= session.query(*sel).filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps2 = list(np.ravel(results))
    return jsonify(temps2)

if __name__ == '__main__':
    app.run()