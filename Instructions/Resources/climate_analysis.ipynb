{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Now you can use Python and SQLAlchemy to do basic climate analysis and data exploration on your new weather station tables. \n",
    "# All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.\n",
    "\n",
    "# Create a Jupyter Notebook file called climate_analysis.ipynb and use it to complete your climate analysis and data exporation.\n",
    "\n",
    "# Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.\n",
    "\n",
    "# Use SQLAlchemy create_engine to connect to your sqlite database.\n",
    "\n",
    "# Use SQLAlchemy automap_base() to reflect your tables into classes.\n",
    "#Save a reference to those classes called Station and Measurement."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Dependencies\n",
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session, create_session\n",
    "from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, inspect, func\n",
    "import datetime as dt\n",
    "import numpy as np\n",
    "# Import and establish Base for which classes will be constructed \n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "Base = declarative_base()\n",
    "\n",
    "# Import modules to declare columns and column data types\n",
    "from sqlalchemy import Column, Integer, String, Float, Date\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Use SQLAlchemy create_engine to connect to your sqlite database.\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\", echo=False)\n",
    "conn = engine.connect()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hawaii_measurement', 'hawaii_station']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use SQLALchemy automap_base() to reflect your tables into classes.\n",
    "\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect = True)\n",
    "Base.classes.keys()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Save a reference to those classes called Station and Measurement.\n",
    "Station = Base.classes.hawaii_station\n",
    "Measurement = Base.classes.hawaii_measurement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Start your engines! Instantiate a session.\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-cff47c6b6fc6>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-7-cff47c6b6fc6>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    Measurement.\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#use tab when you put your cursor after the period to be able to see the columns for each class.\n",
    "Measurement.\n",
    "Station."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>prcp</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-01-01</th>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-02</th>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-03</th>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-04</th>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-05</th>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            prcp\n",
       "date            \n",
       "2017-01-01   0.0\n",
       "2017-01-02   0.0\n",
       "2017-01-03   0.0\n",
       "2017-01-04   0.0\n",
       "2017-01-05   0.0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Design a query to retrieve the last 12 months of precipitation data\n",
    "#Select only the date and prcp values\n",
    "\n",
    "qry1 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date <= '2017-12-31').\\\n",
    "        filter(Measurement.date >= '2017-01-01').all()\n",
    "plot1_pd = pd.DataFrame(data=qry1, columns=[\"date\", \"prcp\"])\n",
    "plot1_pd = plot1_pd.set_index('date', drop=True)\n",
    "plot1_pd.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Create variables to use in our data plot\n",
    "prcp1 = plot1_pd['prcp']\n",
    "date1 = plot1_pd.index.values\n",
    "#date1\n",
    "#prcp1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2126db5a278>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\nsXXrVjz++ON46qmnXPex2Wyorq5Gamqq28dJTk4GAGg0Glx//fXNfnb+/HkUFhYiNDRUmSdBRESy\n45wIIiISVV5ejpUrVyIxMRF33nknqqurAbTuMdi4cSNMJhNsNpvrNrW68evFOcSpZ8+euPrqq/H5\n55+jrKzMdT+r1Yr//d//xW9/+9tmv09ERIGNPRFERISvvvoKsbGxAACz2YwLFy5g8+bNMJvNePfd\ndxESEoJRo0YhIiICr732GoqLixEVFYUDBw5g27ZtCA4ORn19vevxnHMo3nvvPdx0002YNGkS/vCH\nP+CBBx7AzJkzce+99yImJgZffvkljh8/jmeffdb194mIKPCpBE8z4YiIqEtbvHgxPv/882a3hYeH\nIykpCddccw1+9atfIT093fWzI0eOYOnSpTh9+jR0Oh3S09Mxf/58ZGVlYc2aNfjuu+8QHx+P2tpa\nPPXUUzh8+DBSUlKwfft2AEB2djbeeustHD58GDabzfX7M2bM6NDnTURE7cMigoiIiIiIJOGcCCIi\nIiIikoRFBBERERERScIigoiIiIiIJGERQUREREREkrCIICIiIiIiSVhEEBERERGRJCwiiIiIiIhI\nEhYRREREREQkCYsIIiIiIiKShEUEERERERFJ8v8BuwYMVPX21GsAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2126e3cf320>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create the plot\n",
    "sns.set()\n",
    "plt.clf()\n",
    "plt.figure(figsize=[12.8, 8])\n",
    "labels = 'precipitation'\n",
    "x_axis = date1\n",
    "y_axis = prcp1\n",
    "plt.xlabel(\"Date\", fontsize=18)\n",
    "plt.ylabel(\"Precipitation\", fontsize=18)\n",
    "plt.tick_params(axis='y', labelsize=16)\n",
    "plt.tick_params(axis='x', labelsize=16, rotation=45)\n",
    "\n",
    "# Have to plot our chart once again as it doesn't stick after being shown\n",
    "plot1 = plt.plot(x_axis, y_axis, color='steelblue', linewidth=5)\n",
    "plt.legend(labels=labels, loc='upper right', fontsize='large', frameon=True, edgecolor='black')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>prcp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1397.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.165436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.432264</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.010000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.160644</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6.250000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              prcp\n",
       "count  1397.000000\n",
       "mean      0.165436\n",
       "std       0.432264\n",
       "min       0.000000\n",
       "25%       0.000000\n",
       "50%       0.010000\n",
       "75%       0.160644\n",
       "max       6.250000"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use pandas to print the summary statistics for the precipitation data\n",
    "plot1_pd.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Design a query to calculate the total number of stations\n",
    "qry2 = session.query(Station.station).count()\n",
    "#qry2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('USC00519281', 2772),\n",
       " ('USC00519397', 2724),\n",
       " ('USC00513117', 2709),\n",
       " ('USC00519523', 2669),\n",
       " ('USC00516128', 2612),\n",
       " ('USC00514830', 2202),\n",
       " ('USC00511918', 1979),\n",
       " ('USC00517948', 1372),\n",
       " ('USC00518838', 511)]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Design a query to find the most active stations\n",
    "#Do this by listing the stations and observation counts in descending order\n",
    "qry3 = session.query(Measurement.station, func.count(Measurement.tobs)).\\\n",
    "    group_by(Measurement.station).\\\n",
    "    order_by(func.count(Measurement.tobs).desc())\n",
    "qry3.all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('USC00519281', 2772)]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Which station has the highest number of observation counts?  \n",
    "qry3.limit(1).all()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Design a query to retrieve the last twelve months of temperature observation data (tobs)\n",
    "qry4 = session.query(Measurement.date, Measurement.tobs).group_by(Measurement.date).\\\n",
    "    filter(Measurement.date <= '2017-12-31').filter(Measurement.date >= '2017-01-01').all()\n",
    "#qry4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Use the same query but also filter by station with highest number of temperature observation counts\n",
    "qry5 = session.query(Measurement.station, Measurement.date, Measurement.tobs).group_by(Measurement.date).\\\n",
    "    filter(Measurement.date <= '2017-12-31').filter(Measurement.date >= '2017-01-01').\\\n",
    "    filter(Measurement.station==\"USC00519281\").all()\n",
    "#qry5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tobs</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-01-01</th>\n",
       "      <td>72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-02</th>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-03</th>\n",
       "      <td>64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-04</th>\n",
       "      <td>63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-05</th>\n",
       "      <td>63</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            tobs\n",
       "date            \n",
       "2017-01-01    72\n",
       "2017-01-02    70\n",
       "2017-01-03    64\n",
       "2017-01-04    63\n",
       "2017-01-05    63"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Put queried data into dataframe so it can be plotted as histogram\n",
    "plot2_pd = pd.DataFrame(data=qry5, columns=[\"station\", \"date\", \"tobs\"])\n",
    "plot2_pd = plot2_pd.set_index('date', drop=True)\n",
    "plot2_pd = plot2_pd.drop(columns=\"station\", axis=1)\n",
    "plot2_pd.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAvAAAAIBCAYAAAAvaIvGAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzs3Xt8zvX/x/HndZk5bWY0h0YOsS1N\nM2nOmnMjYd9G2HeFUmqEKMqXzkyisTBhjRIhh28JjRLKITmlmkhOOWbYgW3s8/vDb9fXZXPYbK59\ntsf9dut2a+/35/p8Xvvs7bqe1+d6f96XxTAMQwAAAABMweroAgAAAADcOgI8AAAAYCIEeAAAAMBE\nCPAAAACAiRDgAQAAABMhwAMAAAAmQoAHTGrEiBHy9va+6X8jRoxwdKkOdfjwYUeXkCuXLl3S/Pnz\n1bNnTz300EPy9/dX586dFRUVpTNnzji6PJsJEybI29tbO3bsuKPHvXz5so4ePXrd/v3799/Svw9v\nb2+dOnUqX2v95JNP5O3trd27d+frcTLt3bvX9rtNnDjxutstXbrUtl1+j6mr/x1+++238vb21sqV\nK/P1mEBh5uToAgDkTo8ePdSkSRPbz9u2bdOCBQvUo0cPPfjgg7b2e+65xxHlFQifffaZJkyYoG3b\ntjm6lBw5e/asBgwYoJ9//lnNmzdXeHi4ihcvrl9++UXR0dGaP3++pk6dqgceeMDRpTrE2bNn1adP\nHwUFBal///7ZblOpUiWNHz/eru2tt95SyZIlNXz4cLv2smXL5lutjrZmzRoNHTr0un35LT09XX37\n9lWdOnU0evTofD8eUFQQ4AGT8vf3l7+/v+3ny5cva8GCBapfv766dOniwMoKji1btigtLc3RZeSI\nYRh66aWXtHv3bk2ePFkdOnSw6+/Xr5/69u2r/v37a8WKFSpfvryDKnWcf/75R7/++quCgoKuu42L\ni0uWfwfjx4/Ptr2wqlq1qvbt26eDBw+qevXqdn0XL17U+vXrVb58+Xy9+p6WlqYtW7aoTp06+XYM\noChiCg0AFCDffvutNmzYoOeeey5LeJeke++9V2PHjlVCQoIiIyMdUCHMok2bNrJYLNlead+wYYPS\n0tL08MMPO6AyALeLAA8UIVu3blVYWJj8/f3VoEEDPf3009qzZ4/dNs2aNVNERITmzZundu3a6YEH\nHlD37t3166+/6sSJEwoPD5e/v78efvhhTZkyRYZhSJJSU1Pl7e2tmTNnKioqSs2aNVODBg30zDPP\naO/evVlqiYuLU0hIiPz8/BQQEKAXX3xRhw4dsvVn7i8qKkpPP/20fH191aVLF2VkZCgtLU0ffvih\nOnfuLD8/P/n5+alr165aunSp7fHdu3fXihUrlJaWJm9vb9vH982aNVO/fv2y1HNte7NmzfTmm29q\n+PDhqlevnlq1aqXExMRbPo9nzpzR8OHD1bJlS/n6+qp9+/b64IMPbvqJwNKlS2WxWNSrV6/rbtO0\naVP5+Pho5cqVSk9PV1RUlLy9vbVv3z677TIyMtSiRQs988wztrbff/9dzz33nBo2bCg/Pz/17t1b\nP/74o93junfvrueff14RERGqX7++mjVrpj///POGdd+KDRs2qF+/fgoICJCvr68efvhhvfHGG0pK\nSrKrOTIyUh06dFC9evXUvHlzjRw5UidOnJAkff/99+rYsaMk6f3338+TOezLli2Tt7e3fvjhB1vb\npUuX5O/vrxYtWmS7bea5TklJ0fjx49WqVSv5+vqqXbt2mjZtmi5dupTtsQ4dOnTduekRERGqW7eu\n/vnnn1zt+1qVKlXS/fffr7Vr12bpi4uLU8OGDeXu7p6lLykpSePGjVNgYKB8fX3Vtm1bRUZG2o3d\nzHn9+/fv16BBg/Tggw+qQYMGevHFF21/q71796pBgwaSpE8//TTLfQCJiYkaNWqUGjVqJH9/f/Xr\n1y/LONuwYYOeeOIJPfjgg/L391doaKg2bNhwS78/UJgR4IEi4rvvvtNTTz2l1NRUDR48WM8++6wO\nHjyoXr16adeuXXbbfvXVV4qOjlbPnj01YMAAxcfHa+DAgXryySdVsmRJjRgxQtWrV1dUVJS+/vpr\nu8d++umnmjt3rnr37q1nnnlGu3btUu/eve1uYps/f75eeOEFubm56eWXX1ZYWJi2bt2qkJCQLDed\nzpo1S5I0atQoPf7447JarRo2bJimTZumJk2aaNSoURowYIDOnz+vV155RTt37pQkDRw4UPXr11fx\n4sU1fvx4Pf744zk+Z0uWLNFff/2lUaNGKSQkRK6urrd8HsPDw7Vx40b17NlTY8aMkb+/v6ZNm5Zl\nXva1duzYoerVq990akzjxo119uxZ7du3T507d5akLH+Ln376SSdPnrT1//LLL+rZs6cOHTqkAQMG\naPDgwbpw4YL69eunuLg4u8f++OOPWrt2rV555RV169ZNNWvWvOXzlp21a9fq6aefVnp6ul588UWN\nHDlSPj4+mjdvnt577z3bdpMnT9aMGTMUGBio0aNHKzg4WCtWrFD//v1lGIZ8fHxsc9g7duyo8ePH\n3/Yc9hYtWshqtWrTpk22tt27dyslJUUnT560e2O5YcMGeXp6qnbt2rb53fPmzVOHDh302muvqUGD\nBvrggw80bNiwbI91zz33yM/PL8sNnIZhaOXKlWratKkqVKiQq31np23btvr555/tpslcunRJ3377\nrdq1a5dl+wsXLigsLEyxsbFq2bKlRo4cKT8/P02dOlXPPvusLl++bLd95t902LBhCg4O1qpVq2x/\nnypVqujtt9+WdOUN8fjx41WtWjXbY9955x0dOHBAgwcPVq9evbR582Y9/fTTtjcov//+u55//nmV\nKFFCL730koYMGaKEhAT1798/yxtmoMgxABQKixcvNry8vIzFixdn6UtPTzdatmxphIWFGRkZGbb2\nxMREo1WrVkb37t1tbU2bNjV8fHyM/fv329reeustw8vLy3jllVdsbefPnzd8fHyMkSNHGoZhGBcv\nXjS8vLyM++67z4iPj7dt99tvvxk+Pj7GiBEjDMMwjISEBMPPz8/2c6Zjx44Z/v7+xpAhQ+z216hR\nIyMxMdG23ZEjRwwvLy9jypQpdo//7bffDC8vLyMiIsLWNnjwYMPX19duu6ZNmxp9+/bNco6ubW/a\ntKlRt25d4++//87xeTx69Kjh5eVlzJ071+4YQ4cONZ555pksx77afffdZ/Tu3fuG2xiGYcycOdPw\n8vIyvvvuO8MwDOPxxx83OnbsaLfNmDFjDD8/PyM5OdkwDMMICQkxgoKCjAsXLti2SU1NNUJCQoyW\nLVsa6enptu28vLyM7du337SO995775a2DQ0NNdq3b287RqYuXboYjRs3tv3cunVrY+DAgXbbxMbG\nGl26dLH9Lfbt22d4eXkZ0dHRN63vak2bNjU6dOiQbd/jjz9uhISE2H6eNm2a0bx5c8Pb29tYtGiR\nYRiGkZGRYTRt2tR44403DMMwjLlz5xre3t7G1q1b7fY1e/Zsw8vLy/jhhx9s23l5eRm7du0yDMMw\n5syZY3h5eRl79uyxPWbbtm2Gl5eXsXTp0hztOzvx8fGGl5eXMXPmTGPv3r2Gl5eX8cUXX9j6f/jh\nB8Pb29s4duyYMW7cOMPLy8v4559/DMP437j6/PPP7fYZGRlpeHl5GUuWLLH7nV5++WW77YYNG2Z4\neXkZx48fNwzDMJKSkgwvLy/bOTMMw1i7dq3h5eVl9OrVy7h8+bKtPSIiwvDy8jJ27txpGIZhfPDB\nB4a3t7eRkpJi2+bYsWNG+/bts9QHFDVcgQeKgJ07d+r48eNq27atEhISdObMGZ05c8Y2B3bHjh12\nV+hq166tWrVq2X6uUaOGpCtX8zK5urrKzc0ty/SFVq1aycvLy/azj4+PmjRpYvsY//vvv9eFCxfU\npk0bWx1nzpyRs7OzAgIC9N1339mm5UhXbtZ1cXGx/ezp6alt27bp6aeftrUZhmG7apeSknI7p8rO\nvffeqypVqth+vtXzWK5cOZUsWVJz585VXFycLl68KOnKlI8ZM2Zc93gZGRmSpGLFit20NienK2sQ\nZJ6rzp07a9++ffrjjz8kXbmpefXq1WrTpo1Kly6tEydOaOfOnQoMDFRKSoqt9qSkJLVt21bHjx/X\n77//btu/q6ur6tevn8Mzdn0xMTFasGCBrW7pyjQjV1dXu79Z5cqVtWHDBn366ae2MRkWFqalS5fa\n/S3yWsuWLfXLL7/YpvNs3rxZLVu2VM2aNfXTTz9Jkn799VedPn3aNm981apVuvvuu1WrVi27sdy6\ndWtJV+5nyE7Hjh3l5ORk94nJihUrVKpUKdu/sdzu+1p16tRR9erV7ebBx8XFydfXV5UrV86y/dq1\na3XXXXfpX//6l137M888o+LFi2eZT3/tjcT33XefJNmmAd1IUFCQrNb/xZB69epJku05pXLlyjIM\nQ2+88YZtbFauXFmrVq1SSEjITfcPFGasQgMUAZnTUt5++23bR9rXOn78uG3aRoUKFez6MgNldu2Z\noTNT7dq1s+y7evXq2rhxo5KSkmzTEV544YXr1nv+/HmVLFky22NKkrOzs5YtW6aNGzfqr7/+0sGD\nB20h8Np6bse1x77V81i3bl2NGTNGr7/+ul544QWVKFFCAQEB6tChg7p06SJnZ+dsH2u1WnXXXXfd\nUvg5efKkJKlixYqSroTCcePGaeXKlapTp442bdqkf/75R4899pgk2c77rFmzbNOSrnXs2DH5+vpK\nUp6vbuPk5KQDBw5oyZIl2r9/vw4dOmT7Ha4+HyNHjtSAAQP05ptv6u2335avr6/atGmjkJCQbMdC\nXmnZsqWioqK0detWNWvWTNu3b1eXLl1kGIa2bt0q6cr0mZIlS6px48aSroyHY8eO2S3nerVjx45l\n216hQgU1btxYK1eu1EsvvaSMjAytXLlSbdq0UZkyZW5r39lp06aN5s+fr9TUVJUoUUJxcXHq3bt3\nttseOXJE1atXtwvWklSqVCndfffdWdbev3acZP4tr51qk51rH5v5bz49PV2S1K1bN61du1ZLlizR\nkiVLVLlyZT388MMKDg7O0zeXgBkR4IEiIPPFdNiwYbr//vuz3ebq9eKvdwXYYrHc9FjFixe/7vGv\nDvzjxo1TpUqVst1HqVKlbFeWrw0SqampevLJJ7V79241btxYzZs3V79+/fTAAw+offv2N63verIL\nHNceOyfnMTg4WIGBgYqLi9O6dev0448/av369Zo/f77mz5+f7XmSpIYNG+rrr7/WmTNnbhiit23b\nprJly9reMN11111q0qSJVq5cqYEDB2rFihVyd3dXs2bN7Gp/6qmnrrvyyNWfnFz7u9+u2NhYvfvu\nu7r33nvVsGFDBQUFyc/PTx999JHd1WRfX1+tWbNG69at07fffqv169dr0qRJiomJ0cKFC/Ptew3q\n1asnd3d3bdq0Sa6urrpw4YIeeughSdLixYt18uRJbdiwQY0bN1aJEiUkXTmnN/qytBv9/Tp37qxX\nXnlFe/bsUVJSkk6dOqVHH33U1n87+75WmzZtNHv2bP34448qX768jh8/nu38d0l2n35dKyMjI8ub\nz1t5Triem40xZ2dnRUdHa8+ePfrmm2+0fv16ff7551qwYIH+85//KDQ0NNfHBsyOAA8UAZ6enpKu\nrI3dtGlTu74dO3YoKSnpuleFc+rqG/4yHTx4UBUrVlSpUqVstVSoUCFLLT/++KMsFoucnZ2Vmpqa\n7f6XLl2q7du3a8KECbabM6Vb/8ZVq9WaZSWYtLQ02wozN3Kr5zEpKUm///67fHx81L17d3Xv3l1p\naWl65513NH/+fG3ZssUWrK/VpUsXffXVV/r444+v+wU8O3bs0Pbt29W9e3e7v1tmKPzjjz8UFxdn\nm6pxde3FixfPUvvevXt17Ngx2xXQvJaUlKT33ntPLVq0UHR0tN0bxKs/bbh06ZJ+//13ubm5qV27\ndraQuXTpUr3yyitavHixhgwZki81Wq1WNW/eXJs2bVK5cuXk6ekpT09PW0Bdt26dtm/frldffdX2\nGE9PT9tV8quD7MWLF7V27VrbOc9Ou3bt9PrrrysuLk4JCQkqV66cmjdvnif7vlaDBg1UoUIFrV27\nVu7u7qpdu/Z1b0r29PTUwYMHlZGRYRewL1y4oOPHj9s+obkTDh8+rNOnT8vf31/333+/Bg8erMOH\nDyssLEyzZs0iwKNIYw48UAT4+/vL3d1dsbGxunDhgq393LlzGjRokEaPHm03N/l2rF692raMnCTt\n2bNHmzdvtq1p3qJFCxUvXlwzZ860Ww7vyJEjGjBggCZPnnzD/Z89e1ZS1qk6sbGxkuyvpFut1ixX\nFD08PLR//367EL9q1apbWprvVs/jnj171Lt3b7tlLZ2dnW3zg2905fHhhx9WmzZtNHPmTH311VdZ\n+g8dOqShQ4fK3d1dgwcPtutr27atSpYsqffff19nz561e4NTrVo1eXl5aeHChXahOS0tTa+88kqW\nfeWllJQUpaenq2bNmnbhfdeuXdqxY4ftb5aenq7evXvbrUojyfaNs5nnLXMfeTldSroyjSY+Pl7f\nfPONAgICJEl33323PD09FR0drfT0dLtPL1q3bq3jx4/b/Z2lK2NxyJAh+vnnn697rDJlyqh169b6\n7rvvtHbtWgUFBdl9KnM7+76W1WpVq1atbMe63tV36co9LKdPn9bixYvt2mNiYpSenq7AwMBbPq50\ne3+ryMhI9e3b1+7+nGrVqqlChQp5/gkRYDZcgQeKgBIlSui1117T8OHD9a9//UvBwcFycnLS559/\nrpMnT2ry5Ml59oKYkZGhnj17qlevXrp48aJiY2NVsWJFPf/885KuzNkeOHCgJk6cqF69eqlTp05K\nTU3Vp59+qoyMjCxfc3+tZs2aKTIyUkOHDlWvXr1ktVoVFxenTZs2qXjx4kpOTrZtW758eds66QEB\nAQoICFCnTp00fvx49e/fXx07dtSBAwe0aNGiW7pB8lbPY+Ya6+PHj9ehQ4dUp04dHT16VHPnzpW3\nt7ctHF7P+PHj9eKLL2ro0KFaunSpWrZsqRIlSmjPnj1atmyZXFxcNH369Cxzwl1cXNS6dWutWLFC\nVatWta3BnWnUqFHq16+funXrpp49e6ps2bJavny5fv31V40cOdLuZuGcmjlzZrbTOlq2bKm2bdvq\nvvvu0/z581WiRAlVr15d8fHxWrRokYoVK6bU1FRdvHhRpUqVUq9evTR79mwNGjRITZs2VUpKiubP\nn68yZcooODhYkmxrl69evVoVKlRQUFDQbdWeqXnz5rJYLLY3YJkaNWqkL774Ql5eXnZXvv/973/r\nv//9r1577TVt375d999/v/bs2aOFCxfK399fnTp1uuHxOnfurOeee872/1e73X1fq23btlq0aJFO\nnDihcePGXXe7zOOOHj1au3fvlo+Pj3bs2KFly5apUaNGWeq8mZIlS6p06dLauHGjFi5cmKMvjgoL\nC9PKlSvVq1cvde/eXWXKlNGGDRu0e/dujRw5Mkd1AIUNAR4oIjp37qxy5copOjpaH374oYoVKyZv\nb2999NFHWb6s5nZ06dJF5cuX10cffSTDMNSyZUsNHz7cLtw9++yzqlKlimJjY/X++++rVKlSqlev\nngYOHCg/P78b7t/X11eTJk3S1KlTNWHCBLm4uMjLy0uxsbGaOXOmtm7dqsuXL6tYsWIKDQ3Vtm3b\nNH36dP36668KCAjQk08+qcTERH3xxRd66623VLduXU2bNk1RUVG39PvdynksVqyYpk+frilTpigu\nLk7z5s2Tu7u7OnXqpMGDB990lRkXFxfNmDFDK1as0Oeff66pU6fq4sWLqlq1qvr166devXpd94bO\nzp07a8WKFXbzqTM1atRI8+bN05QpUzRz5kxlZGSoVq1aWaYj5cY333yTbXvZsmXVtm1bRUVFaezY\nsVq4cKHS09Pl6empF154QVWqVNFLL72kTZs2KTAwUC+99JIqVKigJUuW6Pvvv1fx4sX14IMPavLk\nybY1xN3c3DRw4EDFxsbqnXfeUe3ateXv739b9UtX3vD5+vpq165dtvnvkvTQQw/piy++UMuWLe22\nL1WqlD799FNNmTJF33zzjb744gtVqlRJTz31lAYMGHDTaWnNmzdXuXLlVKZMmSxvtm5339dq2rSp\nSpcuLXd39+vev3H1cSdPnqzVq1friy++kKenpwYOHKj+/fvf0gpJ13r55Zc1efJkvfXWW3Jzc7vu\n/R/XeuCBBzRr1ixNnTpVM2bMUEpKimrVqqW33npL3bt3z3EdQGFiMW50xwoA3KLU1FQ98MAD6tGj\nh958801HlwMAQKHFJDIAAADARAjwAAAAgIkQ4AEAAAATYQ48AAAAYCJcgQcAAABMpNAuI3nq1M2/\nVbEwcHcvrYSEFEeXAQdjHCATYwGZGAvIxFgwJw8P1+v2cQXe5Jyccr4mLwofxgEyMRaQibGATIyF\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2126e4f9ba8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set()\n",
    "#Plot the results as a histogram with bins=12\n",
    "x = plot2_pd['tobs']\n",
    "num_bins = 12\n",
    "# the histogram of the data\n",
    "#n, bins, patches = \n",
    "plt.figure(figsize=[12.8, 8])\n",
    "temp_plot = plt.hist(x, num_bins, facecolor='steelblue', label='tobs', alpha=0.9)\n",
    "\n",
    "plt.xlabel('Temperature Observation', fontsize=18)\n",
    "plt.ylabel('Frequency', fontsize=18)\n",
    "plt.title('Temperatures Over Last Twelve Months', fontsize=18)\n",
    "plt.tick_params(axis='y', labelsize=16)\n",
    "plt.tick_params(axis='x', labelsize=16)\n",
    "legend = plt.legend(frameon=True, edgecolor='black', fontsize='large')\n",
    "\n",
    "# Tweak spacing to prevent clipping of ylabel\n",
    "plt.subplots_adjust(left=0.15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Write a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d \n",
    "#and return the minimum, average, and maximum temperatures for that range of dates.\n",
    "def calc_temps(start_date, end_date):\n",
    "    select = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "    return session.query(*select).group_by(Measurement.date).filter(func.strftime(\"%Y-%m-%d\", Measurement.date) >=start_date).\\\n",
    "    filter(func.strftime(\"%Y-%m-%d\", Measurement.date) <=end_date).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Calculate the temps for my trip by running calc_temps function using matching dates from last year\n",
    "data = calc_temps(\"2017-05-01\", \"2017-05-15\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tmin</th>\n",
       "      <th>tavg</th>\n",
       "      <th>tmax</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-05-01</th>\n",
       "      <td>65</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-02</th>\n",
       "      <td>73</td>\n",
       "      <td>76.500000</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-03</th>\n",
       "      <td>70</td>\n",
       "      <td>75.600000</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-04</th>\n",
       "      <td>74</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-05</th>\n",
       "      <td>70</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            tmin       tavg  tmax\n",
       "date                             \n",
       "2017-05-01    65  72.000000    78\n",
       "2017-05-02    73  76.500000    79\n",
       "2017-05-03    70  75.600000    78\n",
       "2017-05-04    74  76.333333    78\n",
       "2017-05-05    70  76.333333    79"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Put the results into a dataframe so that it can be plotted\n",
    "plot3_pd = pd.DataFrame(data=data, columns=[\"date\", \"tmin\", \"tavg\", \"tmax\"])\n",
    "plot3_pd = plot3_pd.set_index('date', drop=True)\n",
    "#plot2_pd = plot2_pd.drop(columns=\"station\", axis=1)\n",
    "plot3_pd.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Create variables for my plot\n",
    "p3_date = plot3_pd.index.values\n",
    "p3_tmin = plot3_pd['tmin']\n",
    "p3_tavg = plot3_pd['tavg']\n",
    "p3_tmax = plot3_pd['tmax']\n",
    "#p3_tavg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2126e0f0780>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlwAAAGiCAYAAAAybBhEAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3XtgzvX///HHde08NjO2Oc6MzVk5\nROVQSD7lIymFFZW+OZQkhULOlEif4iOVjo4RygeVD3KKfBxzDGGEMYflFNu1Xe/fH35WV5eZQ6/r\numz321/btWvv92PP1vt6eL3f13s2y7IsAQAAwBi7twMAAADkdRQuAAAAwyhcAAAAhlG4AAAADKNw\nAQAAGEbhAgAAMMzf2wEAeN6wYcO0du1aSdKePXtUsmRJBQcHS5K++OKL7I8vadmypSZNmqTw8PBr\n2s/Jkyd19913q1WrVho8ePDfE15S9+7dtX//fknSzz//rMTERNntdoWHh2vSpEl/235yM3PmTH3/\n/fcaP378dX3/qlWr1KVLF5UtW1aS5HQ6VaRIEXXu3Fl33HFHrt//6quv6oknnlDFihWva/8APIfC\nBeRD/fv3z/64cePGGj16tKpVq5bj87/++uvr2s+XX36pJk2aaN68eXrxxRcVERFxXdv5q3fffTf7\n4woVKuizzz5TZGTk37JtTytbtqzLfLdv365nnnlGEyZMuOJ/E0n64Ycf1KFDB9MRAfwNKFwA3FSt\nWlVNmjTRzz//rNGjR6t169ZavXq1li5dqm+//VZOp1OHDx9WTEyM3njjDcXExLhtw+l06osvvtDA\ngQP1+++/a8aMGerUqZMkqW3btnrqqafUrFkzSdKoUaMkST179tSbb76pJUuWKCwsTNWrV9eePXuu\nedVq3bp1euutt3ThwgXZ7XZ1795dd911l2bOnKklS5YoMzNTKSkpKlGihFq1aqWpU6cqOTlZTz/9\ntJ588knNnDlTixcvlsPhUEpKiooVK6aRI0cqKirKbV9Hjx7V008/rdTUVJUqVUpDhw7V+fPn9eCD\nD2rZsmUqWLCgLMtS06ZN9d577ykhIeGK2StXrqx27drps88+0+jRo7V+/XqNGTNG6enpOnbsmBo2\nbKihQ4dq9OjROnnypHr06KHRo0crNjZWw4cP1y+//CKHw6F69eqpV69e8vPz09tvv60lS5YoICBA\n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\nW6fevXvr888/18qVK/XVV1+pf//++vnnnxUREaESJUp4O65H2e12BQcHq1q1amrQoIH27t2rvXv3\nyul0Zpeu/CYrK0v/+9//dOutt+r48ePavn27HnvsMZ0+fVppaWmqXr26tyN6VEBAgM6ePatvvvlG\ntWvXVo8ePVSnTh2dOHFCWVlZSkhI8GgeCpcBlw6SO3fu1KJFi3T33XcrMjJSBQsWVNWqVbVy5Urt\n2rVLJUuWVEREhLfjesRfXzheffVVFSxYUJGRkWrVqpXi4+O1ceNGpaenq0aNGt6O6xEDBw5U0aJF\n9fjjj2vmzJlasmSJ+vbtqxIlSmjixIk6cOCAli5dqieffDJfXMf153nMmzdPc+fOVYsWLRQSEqIj\nR45o2LBhat68eb66XunSTNq3b68ZM2ZozZo1eu+991S3bl0VKlRITqdTM2bMUFJSUr6Zy4gRI5SZ\nmamyZcvKbrcrNDRUERERKl++vJKTk7V582YFBASodOnS3o7qMSNGjFB6errKly+v+vXrKzQ0VIUK\nFVLz5s0VExOjzZs3Ky0tTbfffru3o3rEiBEjlJGRofj4eMXFxen06dOqVauWYmJiZLfbtXr1al24\ncEE1a9b0aK788c9EDxs0aJCKFSumtm3b6tChQ+rSpYsCAwMlSUWLFlWnTp1kWVa+eBG95NJMHnvs\nMe3YsUOdOnWSJAUGBmr27NmaP3++1q1bpyZNmng5qWdYliWHw6H69esrKipKEyZMkMPhUNeuXSVJ\ne/bs0aFDhzRw4ECVKlXKy2nN++s8/v3vfysoKEidO3eWJD3yyCNq166d199l5El/ncl7772n33//\nXc8++6wiIiJ05swZzZs3T8OHD89Xp4qOHDmisWPHavHixdlnELKyshQeHq4HH3xQZcuWVYUKFbwd\n06OOHDmi8ePHZ8/kkq+++krTp0/XsmXL1LJlSy8m9KwjR47o3//+txYtWqSAgAA99thjKleunD79\n9FN9+umnWrNmje655x6P56Jw/c3+epAcP368AgMD1aVLl+znREdH66WXXso371i83EyCg4OzZ7Jz\n507t2rVLAwcOVJkyZbyc1rxL15ZUq1ZNW7du1eHDhyVdvFDcZrNp5cqVev311/Xcc895fMnbG3Ka\nx7vvvqvAwEDNmzdP0sV36MXGxnozqsfkNJPx48fLZrNp6dKlSkpKUr9+/VSxYkUvp/Wc/fv3S5Ke\nfPJJffjhh1q0aJGki5cpZGVlKSIiQklJSfnm2Cq5z2Tx4sWSpIyMDB04cEDnzp3TgAEDVLZsWW/G\n9Jg/z2PixIlatGiR7Ha7AgICdPToUdntdg0aNMgrrzWcUvwbXTpIpqam6vDhwypWrJjCwsJ03333\n6bvvvpOk7BfQ/HINypVmsmDBAoWFhenxxx/X7bffriJFing7rnF/fTfm8uXLJV28ILpw4cLav3+/\ngoODlZiY6K2IHpXbPJKTk1W4cOF8UTwvuZrfkZCQEFWoUEH+/v7eiukVoaGh8vPzU/PmzRUZGamJ\nEycqMjIy+/SilP/eyfrXmXz44YeKiIhQQkKC6tatq5o1a+arAnq535FChQopMTFR9evX1y233OK1\neVC4/iZX88Jx6X+C/OJqXzgSExPz/EHSsiydOXNGwcHBsixLlmWpWLFiysrK0pYtW7Rx40atXbtW\nK1asUFJSUp5/Q8W1zKNdu3Z5fh4SvyM5uXR/PqfTKX9/f8XHx8tutys+Pl5RUVEaNWqUSpUqpbi4\nOG9H9ZjcZjJ69GiVLFky38zkZpkHhesG8cLhjhcOV06nU926ddP58+dVvXp12Ww22Ww2bd68WatW\nrVKTJk2UkJCgs2fPqmvXrl4/KJjGPNwxE3d/Po5cYrPZdOrUqexbYMTFxSkuLk5ly5bNF9fEXstM\n4uPj8/xMbrp5WLhuWVlZVteuXa3Jkye7PP7TTz9Zo0aNstatW2etXbvW+uSTT6wDBw54KaVnMRNX\nTqfTev75560ZM2ZYmZmZ1q+//mqlpKRYqampVosWLayVK1d6O6JHMQ93zMTdlY4jr732mpWamuql\nZN7DTFzdjPOgcF0nDpLumIm7hQsXWg8//LDlcDiszp07W71797YeeOABa9WqVdb+/fuzn+d0Or2Y\n0nOYhztm4upKx5EHHnggXx5HmImrm3UeFK7rxEHSHTO5vP79+1t169a1vvzyS8uyLGvBggVW69at\nrcOHD3s5mXcwD3fM5A9XexzJT5iJq5t1HlzDdZ3KlSunLVu2qH///mrfvr26d++uiIgIjR8/Xv/8\n5z+z/wRJXr8Y/M+YyUVOp1PvvPOOfv75Z2VlZalFixby8/PTrbfeqpiYGCUkJGjHjh3ZF3TmdczD\nHTPJ2dUcR6x89md7mImrm3UeFK5rwEHSHTNx17VrV0VGRio4OFhbtmzRunXrlJSUpPj4eM2dO1f7\n9u3T/Pnz1aZNGxUoUMDbcY1jHu6YiatrPY742gupCczEVV6YR/66icsNevbZZ5WYmCjLsrRo0SIt\nWrRITz31lKKjozV37lwFBgZq06ZN2XcLzw+YiasLFy4oKipKPXv2lCTt2rVL8+fP1xdffKGGDRtq\n9erVysrK0ujRoxUdHe3ltOYxD3fMxB3HEXfMxFVemAcrXFfpwoULWr9+vfr166caNWooOjpae/fu\n1Y4dOxQcHKxvv/1We/fuVd++ffPN3/BiJu7Onz+vadOmKSAgQImJiQoPD1eBAgW0Y8cO3XHHHWrV\nqpUaNGiQb15ImYc7ZuKK44g7ZuIqr8yDwnWVOEi6YyZ/sCxL0sWbupYuXVoDBgxQsWLFVKFCBRUr\nVkyzZ89WsWLFVKZMGfn5+fnkcvffiXm4YyaXx3HEHTNxlVfmQeHKBQdJd8zkD06nU3v37s3+UxGZ\nmZkqXbq0EhMTNWTIEAUFBWnLli366aef9OijjyosLIx55KN5SMwkJxxH3DETV3ltHhSuHHCQdMdM\nXFmWpe7du2vHjh1q0qSJsrKyFBAQoHXr1unkyZNq2bKl9u/fr+PHj6tLly55/g9zMw93zMQdxxF3\nzMRVXp2HzbpUIZHNsiw9//zzKlSokIYPH67MzEz5+/tr3bp1Sk1NVdGiRbVx40adPn1arVq1Uvny\n5b0d2Thm4srpdKpXr146fPiwihcvrjFjxkiSkpOT1atXLz377LNq1KiRl1N6DvNwx0zccRxxx0xc\n5eV58C7Fv7h0kDxx4oQCAwMlSf7+/kpOTtbIkSP17LPPqk6dOqpTp46Xk3oOM3E3cOBAxcfH6623\n3tLw4cN19OhRxcTE6MyZMxoyZIgqVarkk/eBMYV5uGMmrjiOuGMmrvL6POzeDuBrLh0kp02bpiJF\niujo0aOSlH2QbNSokfLboiAzcZWZmanGjRvrueeek9Pp1IEDB7R8+XJJUrVq1VSpUiVJef8Gr5cw\nD3fMxB3HEXfMxFVenwfXcP1JZmam/Pz89Oijj8rpdGrq1Kny8/NTlSpVFBMTk33jzvx0kGQmf7As\nS2vWrFFsbKzKli0r6eLPHRsbq4ULFyoxMVGFChXyckrPYR7umMnlcRxxx0xc5Yd5ULjEQfJymIm7\nXbt26cknn1SFChVUtmxZWZYlp9OpoKAgJScny7IsxcfH39QHhGvBPNwxE1ccR9wxE1f5aR6cUtTF\ng2SXLl30/fffS7r4C5CVlaXSpUurZMmS2rFjh5xOp5dTehYzcXfpGpwBAwZozpw5stls8vPzU2Rk\npOLi4rRw4UJlZGR4O6bHMA93zMQVxxF3zMRVfpoHK1yStm/frg0bNmjhwoUqXLiwKlWqJLvdrpCQ\nEKWmpmrx4sW6++675e+ff95jwEzcJScnq3Xr1nr00UfVu3dvRUZGqmLFipKkChUq6M4778wXf/fu\nEubhjpm44jjijpm4ylfzsGAtXbrU2rFjh7Vv3z6rfv361pw5c1y+fvr0aS8l8x5mYllOp9P65JNP\nrO+//9765ZdfLMuyrKNHj1qWZVmbNm2yGjVqZM2YMcObET2KebhjJlfGccQdM3GVn+aRL1e4LMvS\nZ599pt9++01ZWVmqUaOGnE6nSpYsqVq1amnIkCEKDQ1VlSpVJF28y21ex0xcWZalLl26yGazKSUl\nRRs3btThw4d1++23S5KKFSumKlWq6F//+pdatmypgICAPH1dDvNwx0zccRxxx0xc5ed55LvCxUHS\nHTNxl5KSoi1btmjIkCG69dZbFRERoRUrVui3335TpUqVsg8QrVu3VmhoKPPIZ/OQmMlfcRxxx0xc\n5fd55LvCxUHSHTP5g9Pp1NKlS7V+/XodPHhQNWvWVOHChVWoUCEFBwdr69atql69uoKCgrIviGYe\n+WceEjPJCccRd8zEVX6fRx64Cu3qOJ1OLVu2TMnJyTp//rxSU1MVHR2tSpUq6dy5c1q7dq3OnDmj\nggULSlL2XW7zMmbiyrIsPfvssypRooT27dun1atX68CBA3rvvfcUExOj22+/XbNmzVJaWprCwsIk\n3dz3hMkN83DHTNxxHHHHTFwxj4vyReHiIOmOmbj77LPPFBkZqQEDBigrK0tvvvmm/Pz81KFDB40c\nOVLJyck6ffq0goODvR3VI5iHO2biiuOIO2biinn8IV8ULg6S7piJu1KlSum3337ThQsX9Ntvv2nH\njh36/PPPValSJS1ZskSHDx9W//79FR0d7e2oHsE83DETVxxH3DETV8zjD/micHGQdMdM3NWsWVNV\nqlRRcHCw/Pz8dOHCBUlSSEiIYmJi9MILL8jPz8/LKT2HebhjJq44jrhjJq6Yxx/yReHiIOmOmbiL\njIzM/jgkJES33HKLFi9erEmTJql///7MI5/PQ2Imf8VxxB0zccU8/pAv3qUYEhKSfW7YsiwlJyfL\n4XBo0qRJateunYoWLerlhJ7HTK7s5MmT6tmzpw4dOqThw4erXLly3o7kVczDHTPhOHI5zMQV8/gT\nT91h1VekpKRYFSpUsB599FFr37593o7jE5iJu99//93q2bMn8/j/mIc7ZuKK44g7ZuIqv88jX6xw\n/Zmfn58OHjyofv36KS4uzttxfAIzcRcQEKBGjRqpSJEi3o7iE5iHO2biiuOIO2biKr/Pw2ZZluXt\nEJ6WkZGRZ+/zcb2YCYAbxXHEHTNxlZ/nkS8LFwAAgCfZvR0AAAAgr6NwAQAAGEbhAgAAMCxf3PgU\nwM1j8ODB2rBhgxwOhw4cOJB9f6sOHTro4Ycfdnluv3791LZtW1WrVu2qtl2hQgVVrFhR0sWLd8uV\nK6devXqpTJkyV/y+V199Vd26dVPJkiWv4ycCAC6aB+CjDh48qA4dOmjJkiV/2zYrVKignTt3Zn8+\nbdo0ffTRR1qwYMEV3znVuHFjff755ypVqtTflgVA/sIKF4CbxtixY7Vp0yalpKTo8ccf1zfffKNu\n3bpJksaPHy9/f38dPHhQ1atX1/Dhw3N9+3m7du00efJkrVixQk2aNNHbb7+t1atX69SpU4qOjtbb\nb7+t2bNnKzU1VZ06ddKUKVP066+/6vXXX9eFCxdUuHBhDR48WKVLl9Ynn3yiOXPmyG63q3r16hoy\nZIgnRgLgJsE1XABuKhkZGVqwYIGSkpJcHt+4caP69eunb7/9Vunp6ZoyZcpVba98+fLau3ev9u/f\nr71792r69On67rvvVLx4cc2dO1edOnVSdHS0PvjgAxUoUED9+/fXW2+9pTlz5uipp57Sa6+9pqys\nLL3//vuaNWuWZs+eLYfDoaNHj5r48QHcpFjhAnBTqV69+mUfv+222xQfHy9JatmypWbMmKGnnnoq\n1+3ZbDYFBwerTJky6tOnj2bOnKl9+/Zp06ZNio2NdXlucnKyfv31V3Xt2jX7sbNnz8rPz081atRQ\n69at1aRJEz311FOKiYm5gZ8SQF5D4QJwUwkODr7s435+ftkfW5bl8vmV7Ny5U23atNHWrVv10ksv\n6cknn1SzZs1kt9v110tcnU6nSpUqpa+//lqSlJWVpePHj0u6eEpz06ZNWr58uf7v//5Po0ePVp06\nda7nRwSQB3FKEUCesH79eh09elROp1NfffWVGjZsmOv3TJ06VTabTXXr1tXatWtVp04dtWvXTnFx\ncVq6dKmysrIkXSxzWVlZio+P16lTp7Ru3TpJ0qxZs/Tyyy/r5MmTuv/++5WYmKgXXnhB9erVc7k4\nHwBY4QKQJ0RHR6t37946evSo6tWrp0ceeeSyz2vZsqWki6tVpUuX1ocffii73a77779f3bp1U4sW\nLSRJVatW1cGDByVJd999tzp16qSJEyfqnXfe0fDhw5Wenq6CBQtq5MiRioyMVJs2bdS6dWuFhISo\nbNmybrewAJC/cVsIADe9NWvWaNy4cZo0aZK3owDAZXFKEQAAwDBWuAAAAAxjhQsAAMAwChcAAIBh\nFC4AAADDKFwAAACGUbgAAAAMo3ABAAAY9v8A90AFS0WJu7IAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2126e0f0128>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.clf()\n",
    "plt.figure(figsize=[10, 6])\n",
    "#Plot the min, avg, and max temperature from your previous query as a bar chart.\n",
    "#Use the average temperature as the bar height.\n",
    "\n",
    "#pmin = plt.bar(p3_date, p3_tmin, width, yerr=15)\n",
    "pavg = plt.bar(p3_date, p3_tavg, yerr=15, label='Error bar is Min to Max Temp')\n",
    "#pmax = plt.bar(p3_date, p3_tmax)\n",
    "plt.ylabel('Temp (F)')\n",
    "plt.xlabel('Trip Dates')\n",
    "plt.title('Trip Avg Temp by Dates')\n",
    "plt.xticks(rotation=45)\n",
    "plt.legend()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75.23111111111112"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Calculate the total Avg Temp for my trip\n",
    "totalavg = plot3_pd['tavg'].mean()\n",
    "totalavg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n4JtvvoGFhQWUSmWFbXTdcEwmk0GS1JXu81/16+eBI0dSkJr6X3Tr5qpZnpAQDzMzcyxatATDh4/G\n48ePIEkSbt26if37f8KQIcFYs2ZV5QU9w97eEQsXfoLVq79GaOh7cHN7XVNzZYqLi3HlypM7Ivz2\nWyqcnNpUeZvacMSrhr9ONQFgxYqvtLZv2rQpxo+fghkzpkAmk6NVq9YIDX0P+/f/pPU5RkZGmDVr\nBvLz8zF+/GRYWFjC29sXkyePg7m5OZo1ewn37mVXqV5n57aYNGkMmjZtBisrK3Ts2LnCdj169MKy\nZREIC1tQpX4r0rFjZ6xfvxoREcsq3OeKmJmZwdraGnZ2rcr84XJ17YHFi+fh7Nn/wsTEBK1atUZW\n1l18/PECzJw5Cy4u3TBz5lQcOXIIb7zRT2dts2aF4eOPF6C0tBRyuRzh4Qtx585tnc+TJAnffrsZ\nd+/ehq2tHf7+9xlVfj204bWaVAav1Szv7bd9sWtXXLnjYl14rSZRHcMRj8rgiFdzOOIR1TEMHpEA\nDB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHmm4unaGo6Oj6DIa\nBQaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gA\nBo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAh\nwUtKSoK/vz8CAgIwZswYXL9+HaWlpVi6dCl8fHzg5eWF7du3iyiNSC8U+t7go0ePMHv2bMTGxsLB\nwQHffPMNlixZAnd3d2RmZiI+Ph4FBQUIDg5Gp06d0LVrV32XSFTr9D7ilZaWQpIk5OXlAQAKCgpg\nbGyM5ORkBAUFQaFQwNLSEoMGDUJcXJy+yyPSC72PeKampoiIiMDw4cPRtGlTqNVqbN++HVOmTIGt\nra2mnY2NDdLT0/VdHpFe6D146enpWLNmDRISEmBvb48tW7Zg+vTpUKvVkMlkmnaSJEEu1z0gN2um\nhEJhUJslNxpy+ZPX38rKXHAlDZ/eg3f06FG89tprsLe3BwCMGjUKy5YtQ69evaBSqTTtVCoVbGxs\ndPZ3/35hrdXa2KjVEuRyGbKz80SX0iBU9gdM78d4HTt2xMmTJ3Hv3j0AQHJyMlq1agUPDw/8+OOP\nKCkpwYMHD7B37154enrquzwivdD7iOfm5oYJEyYgJCQEhoaGsLS0xNq1a+Hk5ITr168jICAAxcXF\nCA4ORs+ePfVdHpFeyCRJkkQX8SI4Lao5rq6dIZfLcPLkb6JLaRDq1FSTiBg8IiEYPCIBGDwiARg8\nIgEYPCIBGDwiARg8IgEYPCIBGDwiAfR+raa+GV5OEF1C/VFcCMhlfM2eQ3Fb32o9jyMekQAMHpEA\nDB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAM\nHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwe\nkQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6RAAwekQAMHpEADB6R\nAAwekQBCgpeeno6QkBAEBgYiKCgIaWlpAIANGzbAx8cHXl5eiIqKgiRJIsojqnV6D97Dhw8xYcIE\nTJw4ETExMZg6dSpmzZqFlJQUJCYmIjo6GvHx8Th+/DgSExP1XR6RXij0vcFjx46hdevWcHd3BwB4\neHigVatW2Lp1K/z8/KBUKgEAQUFBiIuLg6+vr75LbLTORq+G0tQYhQWPRZfS4Ok9eFevXoWVlRXm\nzZuH33//HRYWFpg9ezbu3LkDNzc3TTsbGxtkZWXp7K9ZMyUUCgOt64vuGNdI3Y2J0pSvWVUZWZlX\n63l6D15JSQlSUlKwZcsWuLi4IDk5GZMnT0abNm0gk8k07SRJglyueyZ8/35hpesN+df7uXDEez65\n2Xla11lVEkq9H+NZW1vD2dkZLi4uAABPT0+UlpZCLpdDpVJp2qlUKtjY2Oi7PCK90Hvw3nzzTdy8\neVNzJvPkyZOQyWQYO3Ys4uLiUFhYiKKiIkRHR8PT01Pf5RHphd6nmlZWVlizZg0iIiLw8OFDGBkZ\nISoqCt27d8fFixcxdOhQFBcXw8PDA4GBgfouj0gvZFI9f7Msu5I5NgAYXk7QUyUNA4/xnk9xW+1n\n3evUMR4RMXhEQjB4RAIweEQC6DyrmZKSgqSkJFy9ehVyuRxt2rSBj49PmatMiOj5aD2rmZmZibCw\nMCiVSvTp0wetWrWCQqHAzZs3ceTIETx8+BBLlixBmzZt9F1zGTyrWbN4VvP5VPesptYRLyoqCpGR\nkXBwcCi3bty4cbh69SqioqKwcuXK5yyViPg+HpXBEe/51Pj7eIsXL9Y8zs3NrV5VRFQhrcFLTU3V\nPB43bpw+aiFqNLQG79kZaD2fjRLVOVV6H+/Zz8kR0YvTelZTrVYjPz8fAFBaWqp5/JSZmVntVkbU\ngGkN3sWLF9GjRw/NNLN79+6QyWSQJAkymQwXLlzQW5FEDY3W4J07d06fdRA1KlqP8U6ePAkDAwOt\nPwDw888/661QooZEa/BSUlIwffp0HD16FGq1WrO8pKQEP//8M6ZOnYoDBw7opUiihqbSK1dOnz6N\nqKgopKamwsbGBmq1GiqVCn/7298wdepUdO/eXZ+1VohXrtQsXrnyfKp75UqVLhnLzc1FZmYmZDIZ\nHBwcYGlpWb0qawGDV7MYvOdT4xdJP8vS0lJzOz4ienH8ICyRAAwekQBVDl5+fj4ePnxYm7UQNRo6\ng5eZmYng4GD06NEDrq6uGDt2LO7evauP2ogaLJ3BCwsLw+DBg5Gamopff/0Vb731FubPn6+P2oga\nLJ3BKygowKhRo2BkZIQmTZpg3LhxZb5chIien87gOTk5lflQbEZGBuzs7Gq1KKKGTuf7eCqVCiNH\njkSnTp1gYGCAtLQ0WFlZ4e233wYA7N69u9aLJGpodAbv/fff10cdRI2KzuC5ubkhJyen3A2PnJyc\naq0oooZOZ/AiIyOxZcsWmJqaaj4UK5PJcOLEiVovjqih0hm8ffv24ciRI2jevLk+6iFqFHSe1XRw\ncEDTpk31UQtRo6FzxAsJCcGYMWPQu3dvKBT/ax4aGlqrhRE1ZDqDt3HjRpiYmCA7O1uzjLf7I3ox\nOoNXWFiI7777Th+1EDUaVTrGu3Tpkj5qIWo0dI542dnZePvtt+Hg4AAjIyPNcl6xQlR9OoM3ffp0\nfdRB1KjonGq6ubnBwsICN2/ehKurK0xNTfk1zEQvSGfwYmJiMGvWLGzYsAEPHjzApEmT8MMPP+ij\nNqIGS2fw/v3vf2Pnzp0wMzNDixYtEB0djc2bN+ujNqIGS2fw5HI5zM3/d39AOzs7zS3ciah6dAbP\nwsIC6enpmjfNExIS6tQNbYnqI51nNefPn4/3338fN27cgLu7O+RyOdatW6eP2ogaLK3BKyoqgpGR\nEdq2bYvY2FhkZGRArVbD2dm5zPt5RPT8tE41g4ODNY8VCgXat2+PDh06MHRENUBr8KrwXSZEVE1a\np5qPHz/G+fPntQawU6dOtVYUUUOnNXg3btzA9OnTKwyeTCbD/v37a7UwooZMa/Datm2LmJgYfdZC\n1Gjw24KIBNAavLrwNctEDZXW4H300Uf6rIOoUeFUk0gABo9IAKHBS05ORrdu3TS/b9iwAT4+PvDy\n8kJUVBTfxKcGS1jwMjMzERkZqfk9JSUFiYmJiI6ORnx8PI4fP47ExERR5RHVKiHBe/jwIWbPno2w\nsDDNsqSkJPj5+UGpVMLY2BhBQUGIi4sTUR5RrdP5saDasHDhQgQHB6N9+/aaZXfu3ClzLxcbGxtk\nZWXp7KtZMyUUCu0fzC26Y/xixTZCSlO+ZlVlZGWuu1EF9B68bdu2QaFQYMiQIbh586ZmuSRJZe5Q\nLUkS5HLdA/L9+4WVrjcseFz9YhshpakxCvmaVVludp7WdVaVhFLvwdu9ezcePXqEgIAAFBcXax53\n7NixzHerq1Qq2NjY6Ls8Ir3Qe/CevUPZzZs34e/vj9jYWBw4cACrV6/GsGHDoFAoEB0djaCgIH2X\nR6QXQo7xKtK/f39cvHgRQ4cORXFxMTw8PBAYGCi6LKJaIZPq+Ztl2ZXMsQHA8HKCnippGHiM93yK\n2/pqXVfZMR6vXCESgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKA\nwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDB\nIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEj\nEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMSgMEjEoDBIxKAwSMS\ngMEjEkBI8GJjYzF48GAEBARg+PDh+O233wAAGzZsgI+PD7y8vBAVFQVJkkSUR1TrFPre4JUrV/DF\nF18gOjoa1tbWSElJwfTp0xEREYHExERER0fDwMAAEyZMgLOzM3x9ffVdIlGt0/uIZ2RkhCVLlsDa\n2hoA0LlzZ9y7dw//+c9/4OfnB6VSCWNjYwQFBSEuLk7f5RHphd5HvFatWqFVq1YAAEmSsGzZMvTv\n3x8qlQp9+/bVtLOxsUFWVpa+yyPSC70H76nCwkKEhYXh7t272LhxI2bOnAmZTKZZL0kS5HLdA3Kz\nZkooFAZa1xfdMa6RehsTpSlfs6oysjKv1vOEBO/27dsIDQ2Fs7MztmzZAhMTE9ja2kKlUmnaqFQq\n2NjY6Ozr/v3CStcbFjx+4XobE6WpMQr5mlVZbnae1nVWlYRS78d4+fn5CAkJwYABA/Dll1/CxMQE\nAODh4YG4uDgUFhaiqKgI0dHR8PT01Hd5RHqh9xFv27ZtuH37NpKSkpCUlKRZ/s0332DAgAEYOnQo\niouL4eHhgcDAQH2XR6QXMqmev1mWXclQDwCGlxP0VEnDwKnm8yluq/3trjo11SQiBo9ICAaPSAAG\nj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaP\nSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9I\nAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gA\nBo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IAAaPSAAGj0gABo9IgDoXvEOHDsHf3x/e3t6YMWMG\n8vPzRZdEVOPqVPBycnIQHh6OqKgo7Nu3D61bt8by5ctFl0VU4+pU8I4ePYouXbrA0dERADBixAjs\n2bMHkiSJLYyohtWp4N29exc2Njaa321sbJCfn4+CggKBVRHVPIXoAp6lVqshk8nKLZfLtf99sLIy\nr7xTq+AXLavRMRJdQCNQp0Y8W1tbqFQqze9ZWVmwtLSEUqkUWBVRzatTwevbty9SU1ORmZkJANix\nYwc8PDzEFkVUC2RSHTtzkZKSghUrVqC4uBj29vaIjIxE06ZNRZdFVKPqXPCIGoM6NdUkaiwYPCIB\nGLx66NSpUxg6dChcXV3h6emJHTt2AAByc3Mxbdo0uLq6ol+/fti1a1e55z5+/BjDhg3DwYMHNcsm\nTpyIbt26aX5cXFzQvn17nD59usLt37x5E2PHjkW3bt3g7e1dpq+zZ8+iQ4cOZfpbv359Db8CDYBE\n9cqff/4p9ejRQ4qNjZVKS0ultLQ0qUePHtKxY8ek6dOnS7NmzZIePXokpaamSj179pQuXLigeW56\nero0bNgwqV27dtKBAwe0bmPOnDnShx9+qHV9UFCQtHz5cqmoqEg6dOiQ1K1bN+mPP/6QJEmSvv/+\ne2ny5Mk1t8MNFEe8eub27dtwd3fH4MGDIZfL0alTJ/Tq1QunT59GcnIyZsyYAWNjY3Tt2hV+fn6a\nUe/WrVsICQmBt7c3Xn75Za39Jycn45dffkFERESF6zMyMnDx4kVMmzYNhoaGcHd3R8+ePRETEwMA\nOH/+PF599dWa3/EGhsGrZzpDp9YzAAAE5UlEQVR06IAvvvhC83tubi5OnToFAFAoFGjdurVmnZOT\nEy5dugQAaNasGZKTkzF+/PgKrw4CgJKSEixbtgxz586FmZlZhW2uXLkCOzs7mJiYVLidCxcu4PTp\n0+jfvz/69euHyMhIFBUVvdhON0AMXj2Wl5eH0NBQzaj3bBgAwMTEBI8ePQIAKJVKmJtXfnldQkIC\njI2N4ePjo7VNYWEhmjRponU7zZo1Q//+/REfH49vv/0Wx48fx1dffVWd3WvQGLx66saNGxg+fDgs\nLS2xevVqKJVKzX/+px49evRcl9tFR0dj2LBhZa6NffbEy8SJE9GkSZNKt7N+/Xq8++67UCqVaN26\nNaZMmYKkpKQX2NOGicGrh86dO4dhw4ahb9++WLt2LUxMTODg4ICSkhLcvn1b0+7q1ato27ZtlfrM\nz8/HyZMnMXDgwDLLN27ciDNnzuDMmTPYuHEjnJ2dcevWrTLTx6fbyc3NRWRkZJkPLz9+/BjGxsYv\nuMcND4NXz9y7dw8TJ07Eu+++i/DwcM3oZGZmBg8PD6xYsQIPHz7E2bNnER8fD39//yr1m5aWBmtr\na7Rs2bLSds7Ozmjbti1WrVqFoqIipKSk4Pjx4/Dx8YG5uTmSkpKwevVqFBcX49q1a1i/fj2CgoJe\neL8bmjr1sSDS7YcffkBOTg7WrVuHdevWaZaPGTMGn3zyCRYtWgR3d3colUrMnj0bLi4uVer31q1b\nsLKyqlLbqKgoLFy4EG5ubmjRogVWrlwJW1tbAE+mmkuWLEHv3r1hYmKC4OBgjB079vl3tIHjtZpE\nAnCqSSQAg0ckAINHJACDRyQAg0ckAINHJACDV4/l5+fDz88PN2/erLTdzp07ER8fX61trFq1ClFR\nUZrfT5w4gV69eiEgIAABAQEIDw8vt42wsDBER0dXa3uNBYNXT6WmpmLEiBGaO7JV5vTp08/9CYG8\nvDzMmzcPmzdvLrM8LS0N48ePR2xsLGJjY7Fs2bJqb6Mx45Ur9dTOnTuxaNEizJkzR7MsPz8fH374\nIe7duwcAmDZtGpo0aYIDBw7gl19+gZWVFd54440q9b9//344Ojri3XffLbP8t99+w7179xAfHw87\nOzssWrQIV69eLbMN4MmXz3z33Xf4448/EBoaiuBg3lj4WQxePbV06dJyy5KSkmBnZ4evv/4aFy5c\nQFxcHObOnYv+/fujZ8+eVQ4dAAQGBgJAmWkmAJibm2PgwIEYMGAAtm/fjg8++AA7duwos429e/ei\nqKgIu3btwqVLlzBmzBgG7y8YvAakW7duWLlyJbKystCvXz9Mmzatxrfx8ccfax6PGDECK1asQF5e\nXrl2Hh4ekMlkeOWVV3D//v0ar6O+4zFeA+Lo6IjExET4+/vj1KlTGDJkCNRqtdb2T0+QBAQEVKl/\ntVqNdevWobS0tMxyAwODcm2fLtP2affGjiNeA7J161bcuHED4eHhePPNN/HWW28hPz8fBgYG5cIC\nALGxsc/Vv1wuR1JSEhwcHODr64uYmBi4uLhAqVRq3QZVjMFrQAIDA/Hhhx/C398fBgYGmD17Niws\nLNCnTx+sXLkS5ubmld7WoSoiIyOxYMECrFmzBs2bN8fnn38OAGW2QbrxY0FEAvAYj0gABo9IAAaP\nSAAGj0gABo9IAAaPSAAGj0gABo9IgP8DuRz4JqgKyl0AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2126e472320>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Plot the total Avg Temp for My Trip\n",
    "plt.figure(figsize=[3, 6])\n",
    "\n",
    "totalavg_plt = plt.bar('2017-05', totalavg, yerr=15, color='sandybrown', alpha=.5, label='Error bar is Min to Max Temp')\n",
    "#pmax = plt.bar(p3_date, p3_tmax)\n",
    "\n",
    "plt.ylabel('Temp (F)', fontsize=12)\n",
    "plt.xlabel('1st - 15th')\n",
    "plt.title('Trip Avg Temp', fontsize=14)\n",
    "plt.legend()\n",
    "plt.xticks(fontsize=13)\n",
    "plt.yticks(np.arange(0, 120, 20), fontsize=12)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Optional Analysis\n",
    "#Calculate the rainfall per weather station using the previous year's matching dates\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Calculate the daily normals. Normals are the averages for min, avg, and max temperatures.\n",
    "\n",
    "# Create a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic tobs that match that date string.\n",
    "# Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.\n",
    "# Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.\n",
    "# Use Pandas to plot an area plot (stacked=False) for the daily normals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.\n",
    "\n",
    "# Use FLASK to create your routes.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData]",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
