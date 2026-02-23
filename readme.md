# Resilient API Monitor 🔍

A production-style **Python automation tool** designed to monitor APIs with:
- Retry mechanism  
- Exponential backoff  
- Error logging  
- Multi-run monitoring  
- Success rate analytics  
- JSON-based reporting  

This project simulates real-world API failures and demonstrates how an automation engineer handles unstable APIs using robust retry logic.

---

## 🚀 Features

### ✅ **Retry Logic**
Automatically retries API calls when a failure occurs.

### ⏳ **Exponential Backoff**
Delays double on each retry (1s → 2s → 4s).

### 📝 **Error Logging**
Stores all failures in `monitor.log`.

### 📊 **Success Rate Calculation**
Runs API multiple times and generates:
- Total runs  
- Successful runs  
- Percentage success  

### 📄 **JSON Report Output**
Stores structured results in `report.json`.

### 🎛 **Interactive CLI**
User defines retry attempts.

---

## 🧠 Architecture Overview
User Input → Retry Logic → API Call → Logging → JSON Report → Summary Output

---

## 📂 Project Structure

resilient_api_monitor/
│
├── main.py # Main automation script
├── README.md # Documentation
├── monitor.log # Error logs (auto-generated)
└── report.json # API results summary (auto-generated)

---

## ▶ How to Run
python main.py

Enter your retry attempts when asked.

---

## 🛠 Tech Stack

- Python  
- Logging Module  
- JSON Handling  
- Exception Handling  
- CLI Interaction  

---

## 📈 Future Improvements

- Monitor multiple URLs  
- Add email/Telegram alerts  
- Cron-based auto-run  
- GUI version  

---

## 🧑‍💻 Author
**Ahmad Ali**  
Python Automation Developer  
(https://github.com/hishamahmad1337-pixel/resilient-api-monitor)




