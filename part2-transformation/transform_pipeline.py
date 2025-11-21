import pandas as pd
import glob

# Load all event CSV files
all_files = glob.glob("events_2025*.csv")
df_list = [pd.read_csv(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Sort by client_id and timestamp
df = df.sort_values(['client_id', 'timestamp'])

# Simple sessionization: every 5 events = new session
df['session_id'] = df.groupby('client_id').cumcount() // 5

# Aggregate session metrics
session_metrics = df.groupby(['client_id', 'session_id']).agg({
    'page_url': 'count',
    'event_name': lambda x: list(x),
    'event_data': lambda x: list(x)
}).reset_index()

# Save transformed data
session_metrics.to_csv("session_metrics.csv", index=False)
print("Transformation complete!")
