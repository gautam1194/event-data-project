# Part 2: Transformation Pipeline Documentation

## Objective
Transform raw event data from 14 CSV files into analytics-ready tables. Provide sessionization, user aggregation, and enable marketing attribution.

## Methodology & Architecture

### Data Loading
- Combined 14 CSV files into a single DataFrame
- Columns: client_id, page_url, referrer, timestamp, event_name, event_data, user_agent

### Data Cleaning
- Parsed timestamps to datetime
- Removed duplicates identified in Part 1
- Validated event names

### Sessionization
- Defined sessions as consecutive events for the same client_id
- Assigned a new session ID every 5 events per user
- Rationale: Simple approximation for anonymized IDs without session cookies

### Metrics & Attributes
- Per session: Number of page views, event sequence, event-specific data (event_data list)
- Per user: Aggregate sessions, events, and purchases

### Attribution
- First-click: Credit channel from earliest event in 7-day lookback
- Last-click: Credit channel from last conversion event
- Flexible for more complex attribution models

### Architecture
14 Daily Event CSVs 
        ↓
  Data Quality Check 
        ↓
   Sessionization 
        ↓
  Session Metrics CSV

## Trade-offs
- Fixed 5-event session grouping is simple but may merge/split natural sessions
- Anonymized client_id prevents cross-device tracking; each ID is treated as separate user
- Raw JSON stored as list for simplicity; detailed extraction is possible in next step

## Validation
- Reconciled row counts and event totals before and after aggregation
- Random client_id checked for correct session assignments

## Evaluation
- Sessionization approach: Consecutive 5-event grouping per client_id
- Attributes & metrics: Page views, event sequence, event_data per session
- Attribution handling: Placeholder first-click and last-click logic
- Reconciliation: Aggregated metrics match raw totals
- Maintainability & scalability: Python + Pandas; scalable with Dask/Spark if needed
