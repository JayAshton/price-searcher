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
        format_string = "https://groceries.morrisons.com/search?entry={}".format(keyword)

        return format_string

    def visit_index(format_string):
        page_content = requests.get(format_string)
        tree = html.fromstring(page_content.content)

        return tree

    def index_validation(tree):
        validation_xpath = tree.xpath('//ul[@class="fops fops-regular fops-shelf"]')
        if not validation_xpath:
            validation_result = False
        elif validation_xpath:
            validation_result = True
        else:
            print("Error validating item page")

        return validation_result

    def get_index_urls(tree):
        raw_index_urls = tree.xpath('//ul[@class="fops fops-regular fops-shelf"]//div[@class="fop-contentWrapper"]/a[1]/@href')

        # Pre-append https://groceries.morrisons.com to each item in list
        prepend_string = "https://groceries.morrisons.com"
        f = [prepend_string + sub for sub in raw_index_urls]

        # Clean item URLs
        formatted_index_urls = [f.split('?')[0] for f in f]

        return formatted_index_urls