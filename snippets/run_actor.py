"""Run Booking.com Scraper. https://apify.com/factden/booking-com-scraper"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("factden/booking-com-scraper").call(run_input={
    "searchLocation": ["Rome"],
    "includePrices": True,
    "maxResults": 25,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["hotelName"], item.get("perNightPrice"), item.get("currency"))
