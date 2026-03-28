# Trading Bot (Binance Futures Testnet)

## Setup

1. Clone repo or unzip folder
2. Install dependencies:

pip install -r requirements.txt

3. Set environment variables:

Windows:
set BINANCE_API_KEY=your_key
set BINANCE_API_SECRET=your_secret

Mac/Linux:
export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret

---

## Run Examples

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000

---

## Logs

Logs are stored in:
bot.log

---

## Assumptions

- Using Binance Futures Testnet
- Only MARKET and LIMIT orders supported
- API keys must be set as environment variables


## Note

Due to Binance testnet access restrictions (KYC requirement), 
API calls are simulated using mock responses.

The project demonstrates CLI handling, validation, logging, 
and modular structure as required.