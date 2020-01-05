from flask import render_template
from flask import request

from app.search.handle_search import Search

from app import app

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('search.html')

@app.route('/search', methods=["GET", "POST"])
def search():
    # Get keyword
    keyword = request.form.get("keyword")

    # Handle search
    search_results = Search.handle_search(keyword)

    return search_results
