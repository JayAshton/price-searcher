import requests
from lxml import html

class Item:
    def visit_item(item_url):
        page_content = requests.get(item_url)
        tree = html.fromstring(page_content.content)

        return tree

    def item_validation():
        # We need to add validation to ensure that we are on the correct page
        # We might be redirected or be blocked, do not want to scrape random stuff
        pass

    def get_title(tree):
        title = tree.xpath('//h1[@class="product-details-tile__title"]/text()')
        title = ''.join(title)

        return title

    def get_price(tree):
        price = tree.xpath('//div[@class="product-details-tile__main"]//div[@class="price-control-wrapper"]//span[@data-auto="price-value"]/text()')
        price = ''.join(price)

        return price

    def get_currency(tree):
        currency = "GBP"

        return currency

    def get_description(tree):
        description = tree.xpath('//div[@id="product-description"]//li//text()')
        description = ''.join(description)

        return description

    def get_image(tree):
        image = tree.xpath('//div[@class="product-image__container"]//img/@src')
        image = ''.join(image)
        image = image.split("?")[0]

        return image