# Booking.com Scraper

[![Run on Apify](https://apify.com/actor-badge?actor=factden/booking-com-scraper)](https://apify.com/factden/booking-com-scraper?fpr=factden)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Scrape **Booking.com** hotels at scale — **reviews**, **prices**, per-room **rates**, **availability & occupancy**, and a forward **availability calendar**. Search a city or country, name an exact hotel, or paste Booking.com links. Output is clean **JSON / CSV / Excel**.

**Watch the walkthrough:**

[![Booking.com Scraper walkthrough — hotels, prices, reviews and availability](https://img.youtube.com/vi/mxaye6x1E8U/maxresdefault.jpg)](https://www.youtube.com/watch?v=mxaye6x1E8U)

<a href="https://apify.com/factden/booking-com-scraper?fpr=factden" rel="sponsored noopener"><img src="https://raw.githubusercontent.com/factden/apify-actor-assets/main/booking-com-scraper/02-hotels-overview.png" alt="Booking.com Scraper output — hotels with prices, scores and occupancy"></a>

> Runs on the [Apify platform](https://apify.com/factden/booking-com-scraper?fpr=factden): API, scheduling, proxy rotation, storage, and integrations (Make, Zapier, n8n, Google Sheets). New accounts get free monthly usage credit.

## What it extracts

- **Hotels** — id, name, stars, guest score, review count, per-night / gross / net price, currency, rooms available, scarcity, per-room rates, geo, address, `markdownContent`.
- **Reviews** — score (0-10), positive/negative text, reviewer country, traveller type, stay date + nights, room type, hotelier reply; rating-only reviews included.
- **Calendar** — forward day-by-day availability + min price.
- **Discovery** — expand a city / region / country into all of its hotels.

See [`FIELDS.md`](./FIELDS.md) for the full field dictionary and [`examples/`](./examples/) for sample input and output.

## Quick start

### API (cURL)

```bash
curl -X POST "https://api.apify.com/v2/acts/factden~booking-com-scraper/runs?token=YOUR_APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{ "searchLocation": ["Rome"], "includePrices": true, "maxResults": 25 }'
```

### Python (apify-client)

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("factden/booking-com-scraper").call(run_input={
    "startUrls": ["https://www.booking.com/hotel/fr/le-meurice.html"],
    "includePrices": True,
    "includeReviews": True,
    "maxReviews": 100,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["hotelName"], item.get("perNightPrice"), item.get("currency"))
```

More runnable snippets: [`snippets/`](./snippets/).

## Output

One flat row per hotel (default dataset), one row per review (`reviews`), one per calendar day (`calendar`). Full samples in [`examples/`](./examples/):

- [`examples/hotels.sample.json`](./examples/hotels.sample.json)
- [`examples/reviews.sample.json`](./examples/reviews.sample.json)

## Use cases

- **Rate shopping / comp-set pricing** — schedule daily runs on a hotel list or city.
- **Market discovery** — build a full hotel catalog for a destination.
- **Guest-sentiment datasets** — every review, with text, score and stay context, for NLP / RAG.
- **Availability & occupancy monitoring** — track sell-out patterns across dates.

## Cost

Pay-per-result, no start fee: Hotel $4 / 1k, Prices $5 / 1k, Review $1 / 1k, Calendar day $0.50 / 1k. A "50 hotels + 20 reviews each" run is well under a dollar. New Apify accounts get free monthly credit.

## FAQ

**Does Booking.com have a public API?** No — its partner APIs need accreditation. This scraper gives anyone structured Booking.com data with no keys.

**Can I discover all hotels in a city?** Yes — put the place in `searchLocation`.

**Are rating-only reviews included?** Yes, flagged `isRatingOnly`. There is no 500-review cap.

**Can AI agents use it?** Yes — it's on the Apify MCP server, and every row has a `markdownContent` block for RAG.

## Other FactDen scrapers

- [Google Hotels Scraper](https://apify.com/factden/google-hotels-scraper?fpr=factden) ([docs](https://github.com/factden/google-hotels-scraper))
- [Expedia Hotel Reviews Scraper](https://apify.com/factden/expedia-hotel-reviews-scraper?fpr=factden) ([docs](https://github.com/factden/expedia-hotel-reviews-scraper))
- [Hotels.com Reviews Scraper](https://apify.com/factden/hotels-com-reviews-scraper?fpr=factden)
- [Ctrip / Trip.com Reviews Scraper](https://apify.com/factden/ctrip-trip-reviews-scraper?fpr=factden) ([docs](https://github.com/factden/ctrip-trip-reviews-scraper))
- [Agoda Hotel Reviews Scraper](https://apify.com/factden/agoda-hotel-reviews-scraper?fpr=factden)
- [TripAdvisor Hotel Reviews](https://apify.com/factden/tripadvisor-hotel-reviews-api?fpr=factden)

[All FactDen actors →](https://apify.com/factden?fpr=factden)

## License

[MIT](./LICENSE) © 2026 FactDen
