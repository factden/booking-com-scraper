# Field dictionary

## Hotels dataset (default)

| Field | Type | Description |
|---|---|---|
| hotelId | integer | Booking.com numeric property id |
| hotelName | string | Property name |
| url | string | Booking.com hotel URL |
| stars | integer | Star class (0 for apartments/unrated) |
| reviewScore | number | Guest score 0-10 (null when unrated) |
| reviewCount | integer | Number of guest reviews |
| propertyType | string | e.g. Hotels, Apartments |
| perNightPrice | number | Per-night price (2dp) for the search dates |
| grossPrice | number | Total gross price for the stay |
| netPrice | number | Net price |
| strikethroughPrice | number | Original price when discounted (else null) |
| currency | string | ISO currency of the prices |
| availableRooms | integer | Rooms available for the dates |
| scarcityMessage | string | e.g. "We have 2 left" |
| soldOutRooms | integer | Sold-out room count when present |
| rooms | array | Per-room rates (see Rooms & rates below) |
| city / country / countryCode | string | Location |
| latitude / longitude | number | Coordinates |
| address | string | Street address |
| checkInDate / checkOutDate | string | Stay dates used |
| markdownContent | string | LLM-ready per-hotel markdown |
| scrapedAt | string | ISO-8601 UTC timestamp |

### Rooms & rates (each entry in `rooms[]`)
`roomName`, `rateName`, `pricePerNight`, `priceTotal`, `currency`, `mealPlan`, `breakfastIncluded` (bool), `refundable` (bool), `freeCancellationUntil`, `maxOccupancy`, `roomSurfaceM2`, `geniusDiscountPct`.

## Reviews dataset

| Field | Type | Description |
|---|---|---|
| hotelId / hotelName / hotelUrl | - | Hotel context |
| reviewId | string | Review id |
| score | number | 0-10 |
| title | string | Review title |
| reviewText | string | Positive + negative merged (null for rating-only) |
| textPositive / textNegative | string | Split liked / disliked |
| reviewerName | string | Reviewer display name |
| reviewerCountryCode | string | ISO country code (e.g. NL) |
| travellerType | string | Couple, Solo traveler, Family, etc. |
| roomType | string | Room the reviewer stayed in |
| stayDate | string | Check-in date of the stay (YYYY-MM-DD) |
| stayNights | integer | Nights stayed |
| publishedAt | string | Review date (ISO-8601 UTC) |
| hotelierResponse | object | { text, date } of the hotel's reply |
| isRatingOnly | boolean | True = score with no written text |
| markdownContent | string | LLM-ready per-review markdown |

## Calendar dataset

| Field | Type | Description |
|---|---|---|
| hotelId / hotelName / hotelUrl | - | Hotel context |
| date | string | Calendar day (YYYY-MM-DD) |
| available | boolean | Bookable that day |
| minPrice | number | Cheapest price (null when sold out) |
| currency | string | ISO currency |
| lengthOfStay | integer | Nights the price is for |
