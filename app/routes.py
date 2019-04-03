from flask import render_template   
from app import app
from app.forms import SearchForm


@app.route('/', methods=['POST','GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        start_date =  form.vacation_end.data.strftime('%Y-%m-%d')
        end_date = form.vacation_end.data.strftime('%Y-%m-%d')
        return render_template('results.html', form=form, start_date=start_date,end_date=end_date)
    else:
        return render_template('search.html',form=form) 