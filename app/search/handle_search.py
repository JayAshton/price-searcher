from flask import render_template
from app import app

import asyncio

from app.scrapers.run_tesco import run_tesco
from app.scrapers.run_morrisons import run_morrisons

class Search():
    async def handle_search(keyword):
        #tesco_results = run_tesco(keyword)
        #morrisons_results = run_morrisons(keyword)

        tesco_scraper = asyncio.create_task(run_tesco(keyword))
        morrisons_scraper = asyncio.create_task(run_morrisons(keyword))

        tesco_results = await tesco_scraper
        morrisons_results = await morrisons_scraper

        return render_template('results.html',
        tesco_results=tesco_results,
        morrisons_results=morrisons_results)
