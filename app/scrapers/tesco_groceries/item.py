import requests
from lxml import html

class Item:
    def visit_item(item_url):
        try:
            page_content = requests.get(item_url, timeout=5)
        except:
            print("Error: Page timed out/Unable to visit page")

        tree = html.fromstring(page_content.content)

        return tree

    def item_validation(tree):
        item_validation_xpath = tree.xpath('//div[@class="product-details-tile"]')
        if not item_validation_xpath:
            item_validation_result = False
        elif item_validation_xpath:
            item_validation_result = True
        else:
            print("Error validating item page")

        return item_validation_result

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