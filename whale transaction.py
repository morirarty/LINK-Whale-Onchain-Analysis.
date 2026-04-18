# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from dune_client.client import DuneClient

# ==========================================
# 1. API SETUP & DATA EXTRACTION
# ==========================================
# Initialize the Dune client with personal API key
DUNE_API_KEY = "iEuaSNBZeMLZcwoqQdAqWa1uVUgyQ8d3" 
dune = DuneClient(DUNE_API_KEY)

# The specific Query ID from Dune Analytics URL
QUERY_ID = 6897733

print("Fetching live on-chain data from Dune Analytics...")
# Fetch the latest execution result of the SQL query
query_result = dune.get_latest_result(QUERY_ID)

# Convert the fetched JSON/List data into a Pandas DataFrame for analysis
df = pd.DataFrame(query_result.result.rows)
print("Data successfully loaded!")

# ==========================================
# 2. DATA CLEANING & AGGREGATION
# ==========================================
# Data Sanitization: Drop rows where the 'whale_address' is missing (Null)
df_clean = df.dropna(subset=['whale_address'])

# Business Intelligence: Calculate the total USD volume accumulated by these whales
total_whale_volume = df_clean['amount_usd'].sum()

print(f"Total LINK Whale Accumulation (7 Days): ${total_whale_volume:,.2f}")

# ==========================================
# 3. DATA VISUALIZATION
# ==========================================
print("Generating visualization for the Top 5 Whales...")

# Sort the dataframe to isolate the top 5 largest transactions
df_top_5 = df_clean.sort_values(by='amount_usd', ascending=False).head(5)

# Initialize the canvas size for the plot
plt.figure(figsize=(10, 6))

# Shorten wallet addresses for better readability on the X-axis (e.g., "0x1234...")
short_addresses = df_top_5['whale_address'].str[:6] + "..." 

# Create a bar chart
plt.bar(short_addresses, df_top_5['amount_usd'], color='skyblue', edgecolor='black')

# Add professional titles and labels
plt.title('Top 5 LINK Whales by Transaction Volume (Last 7 Days)', fontsize=14, fontweight='bold')
plt.xlabel('Wallet Address', fontsize=12)
plt.ylabel('Transaction Value (USD)', fontsize=12)

# Format the Y-axis to show readable comma-separated dollar amounts (e.g., 1,000,000)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Save the chart as a PNG file for the GitHub README repository
plt.savefig('whale_chart.png', bbox_inches='tight')

# Render the chart on the screen
plt.show()
