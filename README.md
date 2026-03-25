# 🚀 Binance Futures Testnet Trading Bot

A simplified trading bot built using **Python** that allows users to place **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)**.

This project focuses on **clean architecture**, **input validation**, **logging**, and **error handling**, making it production-ready and easy to extend.

---

## 📌 Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based interaction using `click`
* Structured code (client, service, validators, CLI)
* Robust **input validation**
* Detailed **logging** of requests, responses, and errors
* Graceful **exception handling**

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Business logic for orders
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── .env                   # API keys (not committed)
└── trading_bot.log        # Log file
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd trading_bot
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:



```bash
venv\Scripts\activate
```
---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Binance Testnet Setup

1. Visit: https://testnet.binancefuture.com
2. Create a testnet account
3. Generate API Key and Secret

---

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
```

---

## ▶️ How to Run

### 🔹 MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 30000
```

---

## 📤 Output Example

```
📌 Order Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

✅ Order Success
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
```

---

## 🧾 Logging

All API activity is logged in:

```
trading_bot.log
```

### Logs include:

* Order requests
* API responses
* Errors and exceptions

### Example:

```
INFO - Order Request: {...}
INFO - Order Response: {...}
ERROR - Error placing order: Invalid quantity
```

---

## ⚠️ Validation Rules

* `side` must be **BUY** or **SELL**
* `order_type` must be **MARKET** or **LIMIT**
* `quantity` must be greater than 0
* `price` is required for LIMIT orders

---

## ❗ Error Handling

The application handles:

* Invalid user input
* Missing parameters
* Binance API errors
* Network failures

---

## 🧠 Assumptions

* Only **USDT-M Futures Testnet** is used
* Only **MARKET** and **LIMIT** orders are implemented
* User provides valid trading symbols (e.g., BTCUSDT)
* No leverage/margin configuration included

---

## 📦 Requirements

* Python 3.8+
* Binance Testnet account

Dependencies:

```
python-binance
click
python-dotenv
```

---

## 🧪 Sample Logs (Included)

The repository includes logs for:

* ✅ One MARKET order
* ✅ One LIMIT order

---

## 🚀 Future Improvements (Optional)

* Add **Stop-Limit / OCO orders**
* Retry mechanism for failed API calls
* Docker support
* FastAPI backend
* Interactive CLI (menu-based UI)

---

