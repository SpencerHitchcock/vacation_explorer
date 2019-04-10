from flask import render_template   
from app import app
from app.forms import SearchForm
import requests
import json
import pandas as pd

#Get a list of states to use
#function to loop through eventful API with given dates
#


@app.route('/', methods=['POST','GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        start_date =  form.vacation_end.data.strftime('%Y-%m-%d').replace("-","") + "00"
        end_date = form.vacation_end.data.strftime('%Y-%m-%d').replace("-","") + "00"

        # search the DB and return totals for these dates
        # pass totals into plotly to get the chart
        return render_template('overview.html', form=form, start_date=start_date,end_date=end_date)
    else:
        return render_template('search.html',form=form) 



