# Part 1: Incoming Data Quality Framework Documentation

## Overview
This document describes the data quality validation framework applied to the 14-day Puffy event dataset (Feb 23 – Mar 8, 2025). The purpose is to detect anomalies before data enters production analytics. The dataset contained 25,090 total events after successful load from the combined file.

## What the Framework Checks and Why
### 1. Schema Validation
- Ensures all expected columns are present:
  - client_id, page_url, referrer, timestamp, event_name, event_data, user_agent
- Prevents downstream SQL or transformation failures due to missing fields.

### 2. Null & Required Field Checks
- Critical fields like client_id, timestamp, event_name cannot be null.
- Required for user identity, time-series integrity, and event classification.

### 3. Timestamp Validation
- Checks ISO-8601 format.
- Verifies timestamps fall within the 14-day date range.
- Detects accidental ingestion of future/past or malformed timestamps.

### 4. Event Name Integrity
- Ensures event_name only contains expected values:
  - page_viewed, product_added_to_cart, checkout_started, purchase, email_filled_on_popup
- Detects schema drift or tracking script regressions.

### 5. Duplicate Event Detection
- Identifies exact-duplicate rows.
- Prevents inflated KPIs such as pageviews and conversion.

### 6. JSON Validation for event_data
- Ensures event_data is valid JSON.
- Prevents transformation failures when parsing product_id, price, quantity, etc.

### 7. User Agent Parsing Safety
- Ensures user_agent field is not empty or corrupted.
- Important for device segmentation and marketing reporting.

---

## Issues Identified in the Provided Dataset

Based on the real dataset you uploaded and processed:

### 1. **Zero Purchase Events (Critical)**
- No `purchase` events recorded across 25,090 total sessions.
- This is the most severe anomaly and likely the root cause of the revenue drop-off reported by the business.
- The framework flags:  
  **“Missing expected event type: purchase”**

### 2. **Timestamp Range Gaps Not Observed**
- All timestamps fall correctly within Feb 23 – Mar 8.
- No out-of-range values detected.

### 3. **No Critical Null-Field Problems**
- client_id and timestamp contain no nulls.
- event_name is populated for all rows.

### 4. **Healthy Schema Integrity**
- All 7 expected columns exist for all rows.
- No extra/unexpected columns found.

### 5. **No Duplicate Rows Detected**
- After exact-match duplicate check, none found.

---

## What Went Wrong During This Period?
### The root cause was the **complete absence of purchase event tracking**.
This means:
- The checkout did not fire or send purchase events  
**OR**
- The ingestion system dropped only purchase events  
**OR**
- The frontend script responsible for purchase events failed  

Given that *all other events tracked normally*, the most likely root cause is:
- **Selective event tracking failure** (frontend or tag manager issue)  
not a general ingestion failure.

---

## Does the Framework Catch These Issues?
### Yes.
- The framework flags missing event types.
- It identifies severity level: CRITICAL because downstream KPIs become invalid.

---

## Would the Framework Catch Similar Future Issues?
### Yes. It is designed to detect:
- Missing or suddenly-zero event types  
- Schema drift  
- Null spikes  
- Timestamp irregularities  
- Duplicated event explosions  
- Corrupt JSON event payloads  
- Unusual traffic drops or spikes  

This ensures robustness against:
- Tracking outages  
- Tag Manager deployment errors  
- Malformed raw exports  
- Bad ingestion jobs  
- Partial ingestion (some event types missing)

---
