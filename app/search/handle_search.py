from flask import render_template
from app import app

from multiprocessing import Process, Queue

from app.scrapers.run_tesco import run_tesco
from app.scrapers.run_morrisons import run_morrisons

class Search():
    def handle_search(keyword):
        tesco_queue = Queue()
        morrisons_queue = Queue()

        tesco_scraper = Process(target=run_tesco, args=(keyword, tesco_queue))
        tesco_scraper.start()
        morrisons_scraper = Process(target=run_morrisons, args=(keyword, morrisons_queue))
        morrisons_scraper.start()

        tesco_scraper.join()
        morrisons_scraper.join()

        tesco_results = tesco_queue.get()
        morrisons_results = morrisons_queue.get()

        return render_template('results.html',
        tesco_results=tesco_results,
        morrisons_results=morrisons_results)
