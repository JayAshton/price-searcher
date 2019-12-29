import requests
from lxml import html

class Index:
    def index_validation():
        # We need to check that we are on the correct page
        # We may somehow be navigated/redirected to somewhere else or end up blocked
        # Need to ensure that the page is the index page, then continue scrape
        pass

    def create_format_string(keyword):
        # Need to add support for multiple pages
        # Page generation template {NUM} incremental
        format_string = "https://www.tesco.com/groceries/en-GB/search?query={}".format(keyword)

        return format_string

    def get_index_urls(format_string):
        # Make a request using the format string
        page_content = requests.get(format_string)

        # Gather raw URLS
        tree = html.fromstring(page_content.content)
        raw_index_urls = tree.xpath('//h3[@class="sc-jzJRlG eTAWYm"]//a/@href')

        # Pre-append tesco.com to each item in list
        prepend_string = "https://tesco.com"
        f = [prepend_string + sub for sub in raw_index_urls]

        # Clean item URLs
        formatted_index_urls = [f.split('?')[0] for f in f]

        return formatted_index_urls