# 🐋 LINK Token Whale Accumulation Analysis (Web3 Data Science)

## 📌 Project Overview
This project aims to detect and analyze the activity of high-net-worth wallets ("Whales") accumulating Chainlink (LINK) tokens across Decentralized Exchanges (DEXs) over the past 7 days. Tracking "smart money" is crucial in the DeFi ecosystem to identify liquidity trends, market sentiment, and potential accumulation phases.

## 🛠️ Tech Stack
* **Data Extraction:** SQL (Dune Analytics Engine)
* **Data Pipeline/API:** `dune-client` (Python)
* **Data Transformation:** Pandas
* **Data Visualization:** Matplotlib

## ⚙️ Data Pipeline Architecture
1. **On-chain Extraction:** Engineered a SQL query on Dune Analytics to extract raw transaction data from the `dex.trades` table, specifically filtering for `LINK` token buys and limiting the timeframe to the last 7 days.
2. **API Integration:** Automated the data ingestion process by utilizing the Dune API (`dune-client` in Python) to fetch the latest query results, transitioning from manual CSV downloads to a reproducible programmatic pipeline.
3. **Data Cleaning:** Sanitized the dataset by handling anomalies and dropping null wallet addresses (`dropna()`) to ensure data integrity.
4. **Business Intelligence:** Aggregated the cleaned data to calculate total whale volume and visualized the Top 5 largest acquiring addresses.

## 📊 Key Findings
Based on the on-chain data pipeline, the analysis revealed:
* **Total Whale Volume:** A significant accumulation of **$3,198,933.64** was executed by the top 50 largest wallets within a 7-day window.
* **Market Dominance:** *(Insert your Matplotlib Bar Chart image here!)*

<img width="1751" height="1102" alt="image" src="https://github.com/user-attachments/assets/1d038e1c-bc47-43c5-9e7c-4a7e7b8e9fa3" />


## 🚀 How to Run the Code
1. Clone this repository.
2. Install the required dependencies: `pip install pandas matplotlib dune-client`
3. Insert your personal Dune Analytics API Key into the `DUNE_API_KEY` variable.
4. Run the Python notebook/script to fetch live data and generate the visualization.
