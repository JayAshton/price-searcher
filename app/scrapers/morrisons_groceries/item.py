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
        import ipdb; ipdb.set_trace()
        item_validation_xpath = tree.xpath('//article[@id="overview"]')
        if not item_validation_xpath:
            item_validation_result = False
        elif item_validation_xpath:
            item_validation_result = True
        else:
            print("Error validating item page")

        return item_validation_result

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
        price = tree.xpath('//meta[@itemprop="price"]/@content')
        price = ''.join(price)

        return price

    def get_currency(tree):
        currency = "GBP"
        return currency

    def get_description(tree):
        description = tree.xpath('//div[@class="gn-accordionElement__content gn-accordionElement__content--expanded"]//text()')
        description = ''.join(description)

        # Clean
        description = description.replace('\n','')
        description = description.replace('\r','')
        description = description.strip()

        return description

    def get_image(tree):
        image = tree.xpath('(//img[@class="bop-gallery__image"])[1]/@src')
        image = ''.join(image)
        image = image.split("?")[0]
        prepend_string = "https://groceries.morrisons.com"
        image = prepend_string + image

        return image