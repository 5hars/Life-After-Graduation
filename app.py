# import necessary libraries
import json
from flask import (Flask, render_template, jsonify, request)
import pandas as pd
import numpy as np
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, desc 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Create a list to hold our data
# engine= create_engine("sqlite:///heatmap.sqlite")
# Base = automap_base()
# Base.prepare(engine, reflect = True )

# Cities = Base.classes.cities
# Houses = Base.classes.houses
# Jobs = Base.classes.jobs
# Recreation = Base.classes.recreation

# session = Session(engine)

@app.route("/")
def homepage():
	return render_template("index.html")


@app.route("/map2")
def homepage2():
	return render_template("index_2.html")

# @app.route('/names')

# def names():
# 	results = session.query(Cities).statement
# 	df = pd.read_sql_query(results, session.bind)
# 	df.set_index("id", inplace = True)

# 	return jsonify(list(df.columns))



if __name__ == "__main__":
	app.run(debug=True)