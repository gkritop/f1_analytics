import pandas as pd

df = pd.read_csv("McLaren.csv")

print("First 5 rows of the DataFrame:")
print(df.head())

print("\nDataFrame Info:")
print(df.info())

average_laps = df['laps'].mean()
print("\nAverage number of laps:", average_laps)

lando_races = df[df['driver_name'] == 'Lando Norris (GBR)']
print("\nRaces where Lando Norris was the driver:")
print(lando_races)

lando_races.to_csv('lando_races.csv', index=False)

print("\nDataFrame with missing values:")
print(df.isnull().sum())

df["driver_name"].fillna("Unknown Driver", inplace=True)
df["position"].fillna(df["position"].mean(), inplace=True)

print("\nDataFrame after filling missing values:")
print(df)

df["total_time_minutes"] = df["laps"] * 1.5

sorted_df = df.sort_values(by="position")
print("\nDataFrame sorted by position:")
print(sorted_df)

sorted_df.to_csv("processed_McLaren.csv", index=False)

print("\nSummary statistics:")
print(df.describe())

print("\nDriver names:")
print(df['driver_name'])

top_5_finishes = df[df['position'] <= 5]
print("\nTop 5 finishes:")
print(top_5_finishes)

average_laps_per_track = df.groupby('track')['laps'].mean()
print("\nAverage laps per track:")
print(average_laps_per_track)

sorted_by_best_lap = df.sort_values(by='best_lap_time')
print("\nSorted by best lap time:")
print(sorted_by_best_lap[['track', 'driver_name', 'best_lap_time']])

top_5_finishes.to_csv('top_5_finishes.csv', index=False)
print("\nExported top 5 finishes to 'top_5_finishes.csv'")
