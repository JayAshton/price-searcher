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
    results = run_morrisons(keyword)
    print(results)

    return render_template('results.html', results=results)