import pandas as pd
import glob

# Load all 14 event CSV files
all_files = glob.glob("events_2025*.csv")
df_list = [pd.read_csv(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)

# Basic checks
print("Missing values per column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nEvent types count:")
print(df['event_name'].value_counts())

# Validate timestamp format
invalid_ts = df[pd.to_datetime(df['timestamp'], errors='coerce').isna()]
print("\nSample invalid timestamps:")
print(invalid_ts.head())
