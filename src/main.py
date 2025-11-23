import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data import RAW_CRYPTO_NEWS, RAW_OCBC_REPORT
from src.llm_client import analyze_data

def main():
    print("--- Market Sentinel Engine v0.1 ---")
    print("Initializing analysis...\n")

    print("1. Analyzing Crypto News...")
    crypto_report = analyze_data(RAW_CRYPTO_NEWS)
    if crypto_report:
        print(crypto_report.model_dump_json(indent=2))
    else:
        print("Failed to analyze Crypto News.")

    print("\n--------------------------------------------------\n")

    print("2. Analyzing OCBC Report...")
    ocbc_report = analyze_data(RAW_OCBC_REPORT)
    if ocbc_report:
        print(ocbc_report.model_dump_json(indent=2))
    else:
        print("Failed to analyze OCBC Report.")

if __name__ == "__main__":
    main()
