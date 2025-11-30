import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ingestion import fetch_market_data
from src.llm_client import analyze_data

def main():
    print("--- Market Sentinel Engine v0.2 (Live Data) ---")
    print("Initializing analysis...\n")

    # Fetch all data
    market_data = fetch_market_data()

    print("\n1. Analyzing Crypto Data (Bitcoin)...")
    crypto_report = analyze_data(market_data["crypto"])
    if crypto_report:
        print(crypto_report.model_dump_json(indent=2))
    else:
        print("Failed to analyze Crypto Data.")

    print("\n--------------------------------------------------\n")

    print("2. Analyzing Stock Data (OCBC)...")
    ocbc_report = analyze_data(market_data["ocbc"])
    if ocbc_report:
        print(ocbc_report.model_dump_json(indent=2))
    else:
        print("Failed to analyze Stock Data.")

if __name__ == "__main__":
    main()
