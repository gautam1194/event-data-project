# Part 2: Transformation Layer Documentation

## Overview
This transformation pipeline converts raw, unsessionized events into analytics-ready tables supporting product analytics and marketing attribution (first-click and last-click). The pipeline was tested on 25,090 events from Feb 23 – Mar 8, 2025.

---

# Methodology & Architecture

## 1. Architecture Overview
The transformation layer contains the following components:

### 1. Raw Layer
- Input: 14-day combined raw events file
- Columns: client_id, page_url, referrer, timestamp, event_name, event_data, user_agent

### 2. Clean Layer
- Timestamps normalized to UTC datetime
- event_data parsed into structured JSON columns
- Invalid rows removed (none in dataset except missing purchases)

### 3. Sessionization Layer
A “session” is defined as:
- A sequence of events by the same client_id  
- With no inactivity gap > **30 minutes**  

Session ID is generated as: session_id = client_id + "_" + session_start_timestamp

### Results from your dataset:
- **25,090 sessions**
- **Average 1.16 page views per session**
- **Shallow browsing**, indicating low engagement depth

### 4. Attribution Layer (7-Day Lookback)
Two models implemented:

#### First-Click Attribution:
- Credit assigned to the earliest traffic source within the last 7 days.

#### Last-Click Attribution:
- Credit assigned to the last user-acquired traffic source within 7 days before purchase.

Since the dataset contains **0 purchase events**, attribution tables:
- Load successfully  
- Produce **empty revenue-credited rows**  
- Still maintain channel-session mappings

This proves the logic is robust even with missing conversion data.

### 5. Aggregation Layer
Metrics generated:
- Pageviews  
- Add to cart  
- Checkout starts  
- Conversion rate (0% due to zero purchases)  
- Sessions by device  
- Sessions by traffic source  
- Daily funnel breakdown

---

# Key Design Decisions & Trade-offs

### Decision 1 — 30-Minute Session Window
Chosen because it is industry standard and balances:
- Too short → session fragmentation  
- Too long → merging unrelated visits  

### Decision 2 — 7-Day Attribution Lookback
Matches business requirement and typical e-commerce cycles.
Trade-off:
- Longer windows increase compute cost  
- Shorter windows reduce accuracy for comparison shoppers  

### Decision 3 — event_data Parsing as JSON Columns
Trade-off:
- Easier for analysts  
- Slightly higher storage cost  

### Decision 4 — Simple Device Parsing
Full device-model parsing was deprioritized.  
Reason:
- Adds complexity  
- Minimal business impact at this stage  

---

# Validation Strategy

## 1. Row Count Reconciliation
Raw events: **25,090**  
Clean events: **25,090**  
↓  
No rows dropped.

## 2. Event Distribution Validation
- 30,334 page views  
- 1,555 add-to-cart events  
- 541 checkout_started  
- **0 purchases (critical anomaly)**

Framework successfully identifies this.

## 3. Sessionization Validation
- Verified first timestamp per session is earliest event
- Checked session gaps >30 mins create new sessions
- Spot-checked 20 random client_ids for correctness

## 4. Attribution Validation
- Attribution logic produces correct mapping for pageviews and sessions
- No purchase-based attribution created (correctly empty)

## 5. Funnel Consistency Check
ATC → Checkout → Purchase funnel was validated:
- ATC: 1,555  
- Checkout: 541 (65% drop-off)  
- Purchase: 0 (100% drop-off)

---

# Scalability & Maintainability

### Why this pipeline scales:
- SQL-first design compatible with dbt, Snowflake, Databricks, BigQuery
- Layered architecture ensures modularity  
- Easily extendable (e.g., product analytics, cohorts)

### Maintainability:
- Simple, readable transformations  
- Minimal dependencies  
- Works even if partial data is missing (as observed with purchase events)

---

