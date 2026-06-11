import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read all the CSV files
df_2015 = pd.read_csv('2015.csv')
df_2016 = pd.read_csv('2016.csv')
df_2017 = pd.read_csv('2017.csv')
df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')

# Standardize column names for easier access
df_2015['Year'] = 2015
df_2016['Year'] = 2016
df_2017['Year'] = 2017
df_2018['Year'] = 2018
df_2019['Year'] = 2019

# Rename columns to be consistent
rename_dict_2015 = {'Country': 'Country'}
rename_dict_2016 = {'Country': 'Country'}
rename_dict_2017 = {'Country': 'Country'}
rename_dict_2018 = {'Country or region': 'Country'}
rename_dict_2019 = {'Country or region': 'Country'}

# Apply renames
df_2015.rename(columns=rename_dict_2015, inplace=True)
df_2016.rename(columns=rename_dict_2016, inplace=True)
df_2017.rename(columns={'\"Country\"': 'Country'}, inplace=True)
df_2018.rename(columns=rename_dict_2018, inplace=True)
df_2019.rename(columns=rename_dict_2019, inplace=True)

# Combine all data
df_2017['Country'] = df_2017['Country'].str.strip('"')
all_data = pd.concat([df_2015[['Country', 'Happiness Rank', 'Year']], 
                       df_2016[['Country', 'Happiness Rank', 'Year']],
                       df_2017[['Country', 'Happiness Rank', 'Year']],
                       df_2018[['Overall rank', 'Country', 'Year']].rename(columns={'Overall rank': 'Happiness Rank'}),
                       df_2019[['Overall rank', 'Country', 'Year']].rename(columns={'Overall rank': 'Happiness Rank'})],
                      ignore_index=True)

# Select top 10 and bottom 10 countries to track
top_countries = df_2019.nsmallest(10, 'Overall rank')['Country or region'].tolist()
bottom_countries = df_2019.nlargest(10, 'Overall rank')['Country or region'].tolist()

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Plot top 10 countries
for country in top_countries:
    country_data = all_data[all_data['Country'] == country].sort_values('Year')
    if len(country_data) > 0:
        ax1.plot(country_data['Year'], country_data['Happiness Rank'], marker='o', label=country, linewidth=2)

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Happiness Rank', fontsize=12, fontweight='bold')
ax1.set_title('Top 10 Happiest Countries - Rank Trajectory (2015-2019)', fontsize=14, fontweight='bold')
ax1.legend(loc='best', fontsize=9)
ax1.invert_yaxis()  # Lower rank number = higher happiness
ax1.grid(True, alpha=0.3)
ax1.set_xticks([2015, 2016, 2017, 2018, 2019])

# Plot bottom 10 countries
for country in bottom_countries:
    country_data = all_data[all_data['Country'] == country].sort_values('Year')
    if len(country_data) > 0:
        ax2.plot(country_data['Year'], country_data['Happiness Rank'], marker='o', label=country, linewidth=2)

ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Happiness Rank', fontsize=12, fontweight='bold')
ax2.set_title('Bottom 10 Countries - Rank Trajectory (2015-2019)', fontsize=14, fontweight='bold')
ax2.legend(loc='best', fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xticks([2015, 2016, 2017, 2018, 2019])

plt.tight_layout()
plt.savefig('happiness_rank_trends.jpg', dpi=300, format='jpg', bbox_inches='tight')
print("Plot saved as 'happiness_rank_trends.jpg'")
plt.close()

# Create a second plot showing all countries' evolution
fig, ax = plt.subplots(figsize=(16, 10))

# Plot all countries with lighter colors
for country in all_data['Country'].unique():
    country_data = all_data[all_data['Country'] == country].sort_values('Year')
    if len(country_data) > 1:
        ax.plot(country_data['Year'], country_data['Happiness Rank'], alpha=0.3, linewidth=1, color='gray')

# Highlight top performers
colors = ['red', 'blue', 'green', 'purple', 'orange']
for idx, country in enumerate(top_countries[:5]):
    country_data = all_data[all_data['Country'] == country].sort_values('Year')
    if len(country_data) > 0:
        ax.plot(country_data['Year'], country_data['Happiness Rank'], marker='o', label=country, 
                linewidth=3, color=colors[idx])

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Happiness Rank', fontsize=12, fontweight='bold')
ax.set_title('Happiness Rank Evolution (2015-2019) - Top 5 Highlighted', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=11)
ax.invert_yaxis()
ax.grid(True, alpha=0.3)
ax.set_xticks([2015, 2016, 2017, 2018, 2019])

plt.tight_layout()
plt.savefig('happiness_rank_all_countries.jpg', dpi=300, format='jpg', bbox_inches='tight')
print("Plot saved as 'happiness_rank_all_countries.jpg'")
plt.close()

print("All plots generated successfully!")
