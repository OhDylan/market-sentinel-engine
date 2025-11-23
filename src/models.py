from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class Sentiment(str, Enum):
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    NEUTRAL = "NEUTRAL"

class NewsItem(BaseModel):
    title: str = Field(description="The headline of the news item")
    summary: str = Field(description="A concise summary of the news content")
    sentiment: Sentiment = Field(description="The sentiment of the news item")
    relevance_score: int = Field(description="Relevance score from 1 to 10")
    source: Optional[str] = Field(description="Source of the news if available")

class MarketReport(BaseModel):
    timestamp: str = Field(description="Date or time of the report context")
    items: List[NewsItem] = Field(description="List of analyzed news items")
    overall_sentiment: Sentiment = Field(description="Overall market sentiment based on the items")
    key_takeaways: List[str] = Field(description="List of 3-5 key bullet points summarizing the market situation")
