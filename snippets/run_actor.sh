#!/usr/bin/env bash
# Run Booking.com Scraper via the Apify API. https://apify.com/factden/booking-com-scraper
curl -X POST "https://api.apify.com/v2/acts/factden~booking-com-scraper/runs?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{ "searchLocation": ["Rome"], "includePrices": true, "maxResults": 25 }'
