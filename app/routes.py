from flask import render_template
from flask import request

from app.scrapers.run_tesco import run_tesco
from app.scrapers.run_morrisons import run_morrisons

from app import app

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('search.html')

@app.route('/search', methods=["GET", "POST"])
def search():
    # Get keyword
    keyword = request.form.get("keyword")

    # Run scraper and get results
    # These should be made asynchronous
    tesco_results = run_tesco(keyword)
    morrisons_results = run_morrisons(keyword)

    return render_template('results.html',
    tesco_results=tesco_results,
    morrisons_results=morrisons_results)