from flask import render_template
from app import app

from multiprocessing import Process, Queue

from app.scrapers.run_tesco import run_tesco
from app.scrapers.run_morrisons import run_morrisons
from app.scrapers.run_asda import run_asda

class Search():
    def handle_search(keyword):
        tesco_queue = Queue()
        morrisons_queue = Queue()
        asda_queue = Queue()

        tesco_scraper = Process(target=run_tesco, args=(keyword, tesco_queue))
        tesco_scraper.start()
        morrisons_scraper = Process(target=run_morrisons, args=(keyword, morrisons_queue))
        morrisons_scraper.start()
        asda_scraper = Process(target=run_asda, args=(keyword, asda_queue))
        asda_scraper.start()

        tesco_scraper.join()
        morrisons_scraper.join()
        asda_scraper.join()

        tesco_results = tesco_queue.get()
        morrisons_results = morrisons_queue.get()
        asda_results = asda_queue.get()

        # https://stackoverflow.com/questions/31665328/python-3-multiprocessing-queue-deadlock-when-calling-join-before-the-queue-is-em
        # If description is not limited, queue is full and process hangs
        # Queue should be emptied as after each result

        return render_template('results.html',
        tesco_results=tesco_results,
        morrisons_results=morrisons_results,
        asda_results=asda_results)
