import requests
from lxml import html

class Index:
    def create_format_string(keyword):
        # Need to add support for multiple pages
        # Page generation template {NUM} incremental
        format_string = "https://groceries.asda.com/search/{}".format(keyword)

        return format_string

    def visit_index(format_string):
        page_content = requests.get(format_string)
        tree = html.fromstring(page_content.content)

        return tree

    def index_validation(tree):
        validation_xpath = tree.xpath('//section[@class="products-tab products-tab__body"]')
        # Asda seem to block requests, "outdated browser version
        # May require use of web services/selenium/puppeteer
        import ipdb; ipdb.set_trace()
        if not validation_xpath:
            validation_result = False
        elif validation_xpath:
            validation_result = True
        else:
            print("Error validating item page")

        return validation_result

    def get_index_urls(tree):
        raw_index_urls = tree.xpath('//div[@class="co-product"]//h3[@class="co-product__title"]//a/@href')

        # Pre-append tesco.com to each item in list
        prepend_string = "https://groceries.asda.com"
        f = [prepend_string + sub for sub in raw_index_urls]

        # Clean item URLs
        formatted_index_urls = [f.split('?')[0] for f in f]

        return formatted_index_urls