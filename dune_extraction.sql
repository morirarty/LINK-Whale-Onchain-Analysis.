-- =========================================================================
-- Query Name: LINK Whale Accumulation Tracker
-- Description: Extracts the top 50 largest LINK token buy transactions 
--              from decentralized exchanges (DEXs) over the last 7 days.
-- =========================================================================

SELECT 
    block_time,
    taker AS whale_address, -- Aliasing 'taker' to 'whale_address' for clarity
    taker AS whale_address,
    token_bought_symbol AS token,
    amount_usd 
FROM dex.trades
WHERE token_bought_symbol = 'LINK' 
AND block_time > now() - interval '7' day
ORDER BY amount_usd DESC    -- Sort by the largest transaction volume (Whales)
LIMIT 50                    -- Limit to the top 50 rows for performance
