from flask import render_template
from app import app

from app.scrapers.run_tesco import run_tesco
from app.scrapers.run_morrisons import run_morrisons

class Search():
    def handle_search(keyword):
        # Need to speed up search time
        # 1. Run below in parallel
        # 2. Limit scrape results e.g. 10 per scraper
        tesco_results = run_tesco(keyword)
        morrisons_results = run_morrisons(keyword)

        return render_template('results.html',
        tesco_results=tesco_results,
        morrisons_results=morrisons_results)
