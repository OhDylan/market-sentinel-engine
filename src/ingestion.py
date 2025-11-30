import yfinance as yf
import requests
import json
from typing import Optional, Dict, Any

def truncate_text(text: str, max_chars: int = 5000) -> str:
    """Truncates text to a maximum number of characters."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "...(truncated)"

def get_stock_info(ticker: str) -> str:
    """Fetches stock price and news using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        
        # Get current price 
        info = stock.info
        current_price = info.get('currentPrice', info.get('regularMarketPrice', 'N/A'))
        
        # Get news
        news = stock.news
        formatted_news = ""
        if news:
            for item in news[:3]: # Top 3 news items
                title = item.get('title', 'No Title')
                link = item.get('link', 'No Link')
                formatted_news += f"- {title} ({link})\n"
        else:
            formatted_news = "No recent news found via yfinance."

        report = f"""
        Stock Report for {ticker}:
        Current Price: {current_price} {info.get('currency', 'USD')}
        
        Recent News:
        {formatted_news}
        
        Business Summary:
        {info.get('longBusinessSummary', 'N/A')[:500]}...
        """
        return report.strip()
    except Exception as e:
        return f"Error fetching stock data for {ticker}: {e}"

def get_crypto_price(coin_id: str) -> str:
    """Fetches crypto price from CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if coin_id in data:
                price = data[coin_id]['usd']
                change = data[coin_id].get('usd_24h_change', 0)
                return f"{coin_id.upper()} Price: ${price:,.2f} (24h Change: {change:.2f}%)"
            else:
                return f"Coin {coin_id} not found."
        else:
            return f"Error fetching crypto price: Status {response.status_code}"
    except Exception as e:
        return f"Error fetching crypto price for {coin_id}: {e}"

def get_crypto_news() -> str:
    """
    Fetches crypto news. 
    For MVP, we will use a simple RSS feed from CoinDesk or similar if possible,
    or just return a placeholder if we want to avoid XML parsing complexity right now.
    Let's try a simple request to a public API or just mock it for now as per plan 
    (Plan said 'Mock/RSS/CryptoPanic').
    Let's use a mock for the 'News' part to ensure stability, 
    but we have real price from CoinGecko.
    """
    # Placeholder for actual news fetching logic (e.g. CryptoPanic API requires key)
    # We can simulate "latest headlines" or use a very stable RSS if we had an RSS parser.
    # To keep dependencies low (no feedparser yet), let's return a generic message 
    # or try to hit a JSON endpoint if one exists.
    
    # Actually, let's just return a static string for "News" but real "Price" is separate.
    # The prompt expects "Raw Text" to analyze.
    
    return """
    [Real-time news fetching not fully implemented in MVP v0.2 without API Key]
    Market Sentiment appears mixed based on price action.
    Traders are watching key support levels.
    """

def fetch_market_data() -> Dict[str, str]:
    """Orchestrates fetching of all market data."""
    print("Fetching OCBC data...")
    ocbc_data = get_stock_info("O39.SI")
    
    print("Fetching Bitcoin data...")
    btc_price = get_crypto_price("bitcoin")
    btc_news = get_crypto_news()
    
    btc_data = f"""
    {btc_price}
    
    Crypto News Context:
    {btc_news}
    """
    
    return {
        "ocbc": ocbc_data,
        "crypto": btc_data
    }
