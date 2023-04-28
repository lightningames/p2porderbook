# bitcoin orderbook

A simple bot with sat conversion and ticker features

- admin controls (done)
- coingecko cron job for price updates (done)
- sats to fiat converter (done)
- Allow users on group to use bot privately.  (done)

Potential Features to add: 
-  Expiring orders after a certain age (e.g. 90 days)
-  Add 24h johoe mempool chart to /get_mempool_stats
-  DM use restricted by chatroom membership? 
-  allow tg admins to change cron job timing

Datasources: 
- Coingecko API Data for rates and fiat conversions
- Blockstream Bitcoin API data: https://blockstream.info/api/

Commands: 
-   /all    - List Open Offers. 
-   /add    - Add an Offer, Ex: /add Buy 0.05 btc, %Coinbase ATM/Cash.
-   /del    - Delete an offer. Ex: /del [offer_number]
-   /rates  - Get latest BTC to Fiat Rates from Coingecko
-   /table  - Sats to BTC conversion table
-   /btc   - ex. /btc 0.1337 HKD, converts 0.1337 btc to fiat
-   /sats   - ex. /sats 20000 HKD, converts 20k sats to fiat
-   /fiat   - ex. /fiat 1000 HKD, converts 1k fiat to sats
-   /gettx - <txid> get L1 transaction status
-   /fees  -  <size>  Fee suggestions.
-   /get_block_height   - get bitcoin block height
-   /get_mempool_stats  - L1 mempool stats


Create and Edit your config.yml with credentials. 
