import numpy as np
import pandas as pd

file_path = 'Mercedes.csv'
mercedes_data = pd.read_csv(file_path)

position_array = mercedes_data['position'].values
mean_position = np.mean(position_array)
finished_race = ~mercedes_data['retired'].values
adjusted_positions = position_array.copy()
adjusted_positions[finished_race] -= 1

print("Mean of positions:", mean_position)
print("Adjusted positions:", adjusted_positions)

laps_array = mercedes_data['laps'].dropna().to_numpy()
max_laps = np.max(laps_array)
laps_percentage = (laps_array / max_laps) * 100
average_laps = np.mean(laps_array)
laps_above_average = laps_array > average_laps
sorted_laps = np.sort(laps_array)
unique_laps = np.unique(laps_array)

print("Laps Percentage:", laps_percentage)
print("Laps Above Average:", laps_above_average)
print("Sorted Laps:", sorted_laps)
print("Unique Laps:", unique_laps)

reversed_positions = np.flip(position_array)
num_drivers = len(position_array)
reverse_positions = num_drivers - position_array
mean_laps = np.mean(laps_array)
lap_diff_from_mean = laps_array - mean_laps

print("Reversed Positions:", reversed_positions)
print("Reverse Positions (from total drivers):", reverse_positions)
print("Mean Laps:", mean_laps)
print("Difference of Each Lap Count from the Mean:", lap_diff_from_mean)
