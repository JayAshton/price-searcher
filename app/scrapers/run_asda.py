from app.scrapers.asda_groceries.api import AsdaAPI

from multiprocessing import Process, Queue
import json

def run_asda(keyword, asda_queue):
    # Index functions
    format_string = AsdaAPI.create_api_url(keyword)
    parsed_json = AsdaAPI.parse_json(format_string)

    parsed_json = parsed_json['items'][:9]

    results = {}

    for item in parsed_json:
        index_url = AsdaAPI.get_index_url(item)
        results[index_url] = {}

        title = AsdaAPI.get_title(item)
        results[index_url]['title'] = title

        price = AsdaAPI.get_price(item)
        results[index_url]['price'] = price

        currency = AsdaAPI.get_currency(item)
        results[index_url]['currency'] = currency

        description = AsdaAPI.get_description(item)
        results[index_url]['description'] = description

        image = AsdaAPI.get_image(item)
        results[index_url]['image'] = image

        found_at = "Asda"
        results[index_url]['found_at'] = found_at

        print("Title: ", title)
        print("Price: ", price)
        print("Currency: ", currency)
        print("Description: ", description)
        print("Image: ", image)
        print("Found At: ", found_at)
        print("URL: ", index_url, "\n\n")

    asda_queue.put(results)
    return results
