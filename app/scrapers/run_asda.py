from app.scrapers.asda_groceries.index import Index
from app.scrapers.asda_groceries.item import Item

from multiprocessing import Process, Queue
import json

def run_asda(keyword, asda_queue):
    # Index functions
    format_string = Index.create_format_string(keyword)
    tree = Index.visit_index(format_string)
    index_validation_result = Index.index_validation(tree)

    if index_validation_result:
        index_urls = Index.get_index_urls(tree)
    elif not index_validation_result:
        print("Index validation failed for {} \n\n".format(format_string))
        exit(1)

    index_urls = index_urls[:9]

    results = {}

    # Page functions
    for index_url in index_urls:
        tree = Item.visit_item(index_url)
        results[index_url] = {}

        item_validation_result = Item.item_validation(tree)

        if item_validation_result:
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

            found_at = "Asad"
            results[index_url]['found_at'] = found_at

            print("Title: ", title)
            print("Price: ", price)
            print("Currency: ", currency)
            print("Description: ", description)
            print("Image: ", image)
            print("Found At: ", found_at)
            print("URL: ", index_url, "\n\n")
        elif not item_validation_result:
            del results[index_url]
            print("Item validation failed for {}".format(index_url))

    asda_queue.put(results)
    return results
