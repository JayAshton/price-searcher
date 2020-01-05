from app.scrapers.morrisons_groceries.index import Index
from app.scrapers.morrisons_groceries.item import Item
import json

def run_morrisons(keyword):
    # Index functions
    format_string = Index.create_format_string(keyword)
    index_urls = Index.get_index_urls(format_string)

    results = {}

    # Page functions
    for index_url in index_urls:
        tree = Item.visit_item(index_url)
        results[index_url] = {}

        title = Item.get_title(tree)
        results[index_url]['title'] = title

        price = Item.get_price(tree)
        results[index_url]['price'] = price

        currency = Item.get_currency(tree)
        results[index_url]['currency'] = currency

        description = Item.get_description(tree)
        results[index_url]['description'] = description

        image = Item.get_image(tree)
        results[index_url]['image'] = image

        found_at = "Morrisons"
        results[index_url]['found_at'] = found_at

        print("Title: ", title)
        print("Price: ", price)
        print("Currency: ", currency)
        print("Description: ", description)
        print("Image: ", image)
        print("Found At: ", found_at)
        print("URL: ", index_url, "\n\n")

    return results
