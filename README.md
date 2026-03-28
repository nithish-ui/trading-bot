# Trading Bot (Binance Futures Testnet Simulation)

#Overview   

This project is a simplified trading bot built in Python that simulates placing orders on Binance Futures (USDT-M). It demonstrates clean architecture, CLI-based interaction, input validation, and structured logging.

The bot supports placing both MARKET and LIMIT orders through a command-line interface.


    
#Features:

- Place MARKET and LIMIT orders
- Supports both BUY and SELL sides
- CLI-based input using argparse
- Input validation with clear error handling
- Structured logging to file (`bot.log`)
- Modular code design (separation of concerns)
- Simulated API responses (mocked)



#Project Structure:
trading-bot/
 cli.py # CLI entry point
 orders.py # Order execution logic
 client.py #  API client wrapper
 logger.py # Logging configuration
 requirements.txt # Dependencies
 README.md # Documentation
 bot.log # Log file (generated)




## Setup Instructions:

1.Clone the repository:
git clone
cd trading-bot

 
2.Create virtual environment:

python -m venv venv
venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

#
 How to Run

# 
Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000

# Sample Output:


Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Response:
Order ID: 40331
Status: FILLED
Executed Qty: 0.001
Avg Price: 65000

SUCCESS

#Logging:

All API requests, responses, and errors are logged in:

bot.log

This ensures traceability and debugging support.

# Note (Important):

Due to Binance testnet access restrictions (KYC requirement),  
actual API calls could not be performed.

Instead, "mock responses" are used to simulate:
Order placement
Execution status
API responses

The architecture is designed such that replacing mock logic  
with real API integration is straightforward.

# Design Decisions:

Modular design separating CLI and business logic
Logging implemented for observability
Validation ensures safe execution
Mock layer used to bypass external dependency constraints


#Requirements:
python-binance==1.0.19
