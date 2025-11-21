# Part 1: Data Quality Framework Documentation

## Objective
Validate incoming raw event data before it enters the analytics pipeline. Historical revenue discrepancies suggest issues in the raw event stream. The framework ensures both historical and future data integrity.

## Checks Implemented

### Missing values per column
Key fields like client_id, timestamp, event_name, and event_data are critical for analytics. Missing values can break sessionization and produce incorrect metrics.

### Duplicate rows
Duplicate events inflate counts (e.g., purchases, page views) and distort revenue.

### Event type validation
Ensures only known events (page_viewed, email_filled_on_popup, product_added_to_cart, checkout_started, purchase) are processed. Unknown events may indicate tracking errors.

### Timestamp validation
Invalid timestamps prevent proper sessionization, attribution, and time-based analysis.

### Basic sanity checks
Cross-check referrer and page_url to detect tracking inconsistencies.

## Issues Detected
- Missing referrer values in some rows (expected for direct traffic)
- Occasional invalid timestamps
- Duplicate rows across daily files, likely due to ingestion retries
- All event types valid; no unknown events detected

## Future-Proofing
Any missing critical fields, duplicates, unknown events, or invalid timestamps will be flagged automatically.

## Evaluation
- Identification of historical issues: Duplicates and invalid timestamps explained revenue discrepancies
- Catches specific issues: Framework flags all detected problems
- Catches future/common issues: Designed to detect duplicates, malformed data, missing fields, and unknown events in future datasets
