import requests
from lxml import html

class Index:
    def create_format_string(keyword):
        # Need to add support for multiple pages
        # Page generation template {NUM} incremental
        format_string = "https://www.tesco.com/groceries/en-GB/search?query={}".format(keyword)

        return format_string

    def visit_index(format_string):
        page_content = requests.get(format_string)
        tree = html.fromstring(page_content.content)

        return tree

    def index_validation(tree):
        validation_xpath = tree.xpath('//div[@id="product-list"]')
        if not validation_xpath:
            validation_result = False
        elif validation_xpath:
            validation_result = True
        else:
            print("Error validating item page")

        return validation_result

    def get_index_urls(tree):
        raw_index_urls = tree.xpath('//div[@class="product-details--content"]//h3/a/@href')

        # Pre-append tesco.com to each item in list
        prepend_string = "https://tesco.com"
        f = [prepend_string + sub for sub in raw_index_urls]

        # Clean item URLs
        formatted_index_urls = [f.split('?')[0] for f in f]

        return formatted_index_urls