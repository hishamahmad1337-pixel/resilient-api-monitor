import random
import logging
import time
import json 
from datetime import datetime

logging.basicConfig(
    filename="monitor.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Fake API
def fake_api():
    number = random.randint(1, 5)
    if number != 2:
        raise ConnectionError("API request failed!")
    return {"status": "success", "data": "Important API Data"}


# Retry Logic
def run_with_retry(func, retries=3):
    attempts = 0
    success = False
    response = None

    for i in range(retries):
        attempts += 1
        try:
            response = func()
            success = True
            print("API Success")
            break
        except Exception as e:
            delay = 2 ** i
            logging.error(f"Attempt {attempts} failed: {e}")
            print(f"Retrying in {delay} sec...")
            time.sleep(delay)

    if not success:
        logging.error("API failed after all retries")
        print("API Down")

    return {
        "timestamp": str(datetime.now()),
        "success": success,
        "attempts": attempts,
        "response": response
    }


# Save report
def save_report(data):
    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Report saved → report.json")


# MAIN EXECUTION
if __name__ == "__main__":
    result = run_with_retry(fake_api)
    save_report(result)
    input("Press Enter to exit...")
def monitor_multiple(api_func, runs=5):
    results = []
    success_count = 0

    for i in range(runs):
        print(f"\n--- Monitoring Attempt {i+1} ---")
        result = run_with_retry(api_func)
        results.append(result)

        if result["success"]:
            success_count += 1

    success_rate = (success_count / runs) * 100

    summary = {
        "total_runs": runs,
        "successful_runs": success_count,
        "success_rate_percent": success_rate,
        "detailed_results": results
    }

    return summary   
if __name__ == "__main__":
    retries = int(input("Enter retry attempts (e.g. 3): "))

    print("\nStarting multiple API monitoring...\n")

    final_report = monitor_multiple(fake_api, runs=5)

    save_report(final_report)

    print("\n📊 Final Success Rate:", final_report["success_rate_percent"], "%")

    input("\nPress Enter to exit...")