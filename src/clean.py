import pandas as pd
import os

# Load 1rd file
df1 = pd.read_csv('data/country_wise_analysis_addiction.csv')

# Load 2rd file
df2 = pd.read_csv('data/screen_time_behavior.csv')

# Load 3rd file
df3 = pd.read_csv('data/tiktok_instagram_global_100countries.csv')

max_score_country = df1.loc[df1['addiction_score'].idxmax(), 'country']
min_score_country = df1.loc[df1['addiction_score'].idxmin(), 'country']
print(f'Country with the highest addiction: {max_score_country}', end='\n')
print(f'Country with the lowest addiction: {min_score_country}')

