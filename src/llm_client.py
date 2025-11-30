import os
import google.generativeai as genai
from dotenv import load_dotenv
from .models import MarketReport
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")

def configure_genai():
    if API_KEY:
        genai.configure(api_key=API_KEY)

def analyze_data(text: str) -> MarketReport:
    configure_genai()
    
    model = genai.GenerativeModel(
        'gemini-2.0-flash',
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": MarketReport
        }
    )
    
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    You are a professional financial analyst. 
    Analyze the following raw text and extract structured market intelligence.
    Clean up any HTML tags or irrelevant noise (ads, etc.).
    
    Context Date: {current_date}
    
    If the text contains "No recent news" or similar, return an empty list for 'items'.
    However, you MUST still populate 'timestamp', 'overall_sentiment', and 'key_takeaways' 
    based on the available data (price, business summary, etc.).
    
    Raw Text:
    {text}
    """
    
    try:
        response = model.generate_content(prompt)
        
        # Parse JSON string to dict, then to Pydantic model
        json_data = json.loads(response.text)
        report = MarketReport(**json_data)
        return report
        
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return None
