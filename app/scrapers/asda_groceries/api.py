import requests
from lxml import html
import json

# Asda seem to block requests, "outdated browser version
# May require use of web services/selenium/puppeteer
# May be able to to scrape asda via their API and parse JSON
# https://groceries.asda.com/api/items/search?requestorigin=gi&keyword=red&pagenum=1

class AsdaAPI:
    def create_api_url(keyword):
        # Need to add support for multiple pages
        # Page generation template {NUM} incremental
        format_string = "https://groceries.asda.com/api/items/search?requestorigin=gi&keyword={}&pagenum=1".format(keyword)

        return format_string

    def parse_json(format_string):
        json_results = requests.get(format_string)
        json_results = json.loads(json_results.text)

        return json_results

    def get_index_url(item):
        id = item['shelfId']
        index_url = "https://groceries.asda.com/product/{}".format(id)

        return index_url

    def get_title(item):
        title = item['name']

        return title

    def get_price(item):
        raw_price = item['price']
        price = raw_price.replace('£', '')

        return price

    def get_currency(item):
        currency = "GBP"

        return currency

    def get_description(item):
        description = item['aisleName']

        return description

    def get_image(item):
        image = item['extraLargeImageURL']

        return image