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
        title = tree.xpath('//title//text()')
        title = ''.join(title)

        # Clean
        title = title.replace('Morrisons:', '')
        title = title.replace('(Product Information)', '')
        title = title.replace('\n', '')
        title = title.replace('\r', '')
        title = title.strip()

        return title

    def get_price(tree):
        price = tree.xpath('//div[@class="typicalPrice"]//meta[@itemprop="price"]/@content')
        price = ''.join(price)

        return price

    def get_currency(tree):
        currency = "GBP"
        return currency

    def get_description(tree):
        description = tree.xpath('//div[@class="bopSection"]//text()')
        description = ''.join(description)

        # Clean
        description = description.replace('\n','')
        description = description.replace('\r','')
        description = description.strip()

        return description

    def get_image(tree):
        image = tree.xpath('//ul[@id="galleryImages"]//a/@href')
        image = ''.join(image)
        image = image.split("?")[0]
        prepend_string = "https://groceries.morrisons.com"
        image = prepend_string + image

        return image