import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('2015.csv')

# Create two subplots: Top 20 and Bottom 20
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

df_sorted = df.sort_values('Happiness Rank')

# Top 20 happiest countries
top_20 = df_sorted.head(20)
ax1.barh(top_20['Country'], top_20['Happiness Rank'], color='green', alpha=0.7)
ax1.set_xlabel('Happiness Rank')
ax1.set_title('Top 20 Happiest Countries')
ax1.invert_yaxis()
ax1.grid(axis='x', alpha=0.3)

# Bottom 20 least happy countries
bottom_20 = df_sorted.tail(20)
ax2.barh(bottom_20['Country'], bottom_20['Happiness Rank'], color='red', alpha=0.7)
ax2.set_xlabel('Happiness Rank')
ax2.set_title('Bottom 20 Least Happy Countries')
ax2.invert_yaxis()
ax2.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('happiness_rank_top_bottom.png', dpi=300, bbox_inches='tight')
plt.show()

print("Plot saved as 'happiness_rank_top_bottom.png'")
