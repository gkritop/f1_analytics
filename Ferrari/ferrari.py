import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats

df = pd.read_csv('Ferrari.csv')

def convert_time(time_str):
    if pd.isna(time_str):
        return None
    try:
        return pd.to_timedelta('00:' + time_str)
    except ValueError:
        return None

df['best_lap_time'] = df['best_lap_time'].apply(convert_time)
df['driver_time'] = df['driver_time'].apply(convert_time)

print("Descriptive Statistics:\n", df.describe())

total_laps = df.groupby('driver_name')['laps'].sum()
print("\nTotal Laps by Each Driver:\n", total_laps)

average_lap_time = df.groupby('track')['best_lap_time'].mean()
print("\nAverage Best Lap Time by Track:\n", average_lap_time)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(df['best_lap_time'].dropna().dt.total_seconds(), kde=True)
plt.title('Distribution of Best Lap Times')
plt.xlabel('Seconds')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
df['best_lap_time_seconds'] = df['best_lap_time'].dt.total_seconds()
sns.lineplot(x='track', y='best_lap_time_seconds', data=df, estimator='mean')
plt.xticks(rotation=90, ha='center', fontsize=8)
plt.tight_layout()
plt.title('Average Best Lap Time by Track')
plt.xlabel('Track')
plt.ylabel('Average Lap Time (Seconds)')
plt.show()

def time_to_seconds(time_str):
    if pd.isna(time_str) or time_str == '':
        return np.nan
    try:
        minutes, seconds = map(float, time_str.split(':'))
        return minutes * 60 + seconds
    except ValueError:
        return np.nan

df['best_lap_time_seconds'] = df['best_lap_time'].apply(time_to_seconds)

df = df.dropna(subset=['best_lap_time_seconds'])

fig = px.bar(df, x='track', y='best_lap_time_seconds', color='driver_name', barmode='group',
             title='Best Lap Time Comparison of Ferrari Drivers Across Tracks')

fig.update_layout(
    xaxis_title='Track',
    yaxis_title='Best Lap Time (seconds)',
    legend_title='Driver',
    xaxis_tickangle=-90)

fig.show()

fig_positions = px.scatter(df, x='track', y='position', color='driver_name', 
                           symbol='driver_name', size_max=10,
                           title='Finishing Positions of Ferrari Drivers Across Tracks')

fig_positions.update_traces(marker=dict(size=12))
fig_positions.update_layout(
    xaxis_title='Track',
    yaxis_title='Finishing Position',
    yaxis=dict(autorange="reversed"),
    legend_title='Driver',
    height=600,
    xaxis_tickangle=-90
)
fig_positions.show()

df['driver_time_int'] = pd.to_numeric(df['driver_time_int'], errors='coerce')
df.dropna(subset=['driver_time_int', 'track'], inplace=True)

anova_df = df[['track', 'driver_time_int']]
unique_tracks = anova_df['track'].unique()
driver_time_arrays = [anova_df['driver_time_int'][anova_df['track'] == track] for track in unique_tracks]

F_statistic, p_value = stats.f_oneway(*driver_time_arrays)
print(f"F-statistic: {F_statistic}, P-value: {p_value}")

if p_value < 0.05:
    print("We reject the null hypothesis - there is a significant difference in the mean driver times across tracks.")
else:
    print("We fail to reject the null hypothesis - there is no significant difference in the mean driver times across tracks.")

plt.figure(figsize=(12, 6))
sns.boxplot(x='track', y='driver_time_int', data=anova_df)
plt.xticks(rotation=90)
plt.title('Driver Time Intervals by Track')
plt.xlabel('Track')
plt.ylabel('Driver Time Int')
plt.show()
