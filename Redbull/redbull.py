import pandas as pd
import numpy as np

file_path = 'RedBull.csv'
redbull_data = pd.read_csv(file_path)

redbull_data['laps'] = pd.to_numeric(redbull_data['laps'], errors='coerce')
redbull_data['position'] = pd.to_numeric(redbull_data['position'], errors='coerce')
redbull_data['pit'] = pd.to_numeric(redbull_data['pit'], errors='coerce')

average_laps = np.nanmean(redbull_data['laps'])
print(f"The average number of laps completed is: {average_laps:.2f}")

std_position = np.nanstd(redbull_data['position'])
print(f"The standard deviation of the drivers' final positions is: {std_position:.2f}")

cleaned_data = redbull_data.dropna(subset=['pit', 'position'])
correlation_coefficient = np.corrcoef(cleaned_data['pit'], cleaned_data['position'])[0, 1]
print(f"The correlation coefficient between the number of pit stops and final positions is: {correlation_coefficient:.2f}")
