import pandas as pd

# Load session metrics
df = pd.read_csv("session_metrics.csv")

# Monitor key metrics
total_sessions = df['session_id'].nunique()
total_events = df['page_url'].sum()

if total_sessions == 0 or total_events == 0:
    print("ALERT: Metrics are unusually low!")

print("Total sessions:", total_sessions)
print("Total events:", total_events)
