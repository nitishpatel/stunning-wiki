from typing import List, Dict, Union

from pydantic import BaseModel
from fastapi import FastAPI
import requests
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

app = FastAPI()

# Download stopwords from NLTK
nltk.download('stopwords')

# Set of English stopwords
stop_words = set(stopwords.words('english'))

# In-memory database
DATABASE = {
    "search_results": []
}

@app.get("/")
def read_root():
    """Root endpoint to welcome users."""
    return {"Message": "Welcome to the assignment"}

class SearchQuery(BaseModel):
    """Pydantic model for search queries."""
    title: str
    count: int

@app.post("/wikipedia-count/")
def fetch_wikipedia_summary(query: SearchQuery):
    """Endpoint to fetch Wikipedia summary and count the most common words."""
    # Wikipedia API URL for search
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query.title}&format=json"
    
    # Make a request to Wikipedia API for search
    response = requests.get(search_url)
    data = response.json()
    
    # Extract search results
    search = data['query']['search']
    
    if len(search) == 0:
        # No search results found
        return {"title": query.title, "count": 0, "search": "No search results found"}

    # Fetching the summary of the first search result
    pageid = search[0]['pageid']
    summary_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&titles={search[0]['title']}&format=json"
    
    # Make a request to Wikipedia API for summary
    response = requests.get(summary_url)
    data = response.json()
    
    # Extract summary
    extract = data['query']['pages'][str(pageid)]['extract']

    # Tokenize words from the summary
    words = re.findall(r'\b\w+\b', extract.lower())
    
    # Remove stop words
    clean_words = [word for word in words if word not in stop_words]
    
    # Count word occurrences
    count = Counter(clean_words)
    
    # Get the most common words
    top_words = count.most_common(query.count)
    
    # Prepare result format
    result = [{"word": word, "count": count} for word, count in top_words]
    
    # Update the in-memory database
    DATABASE["search_results"].append({"title": query.title, "count": query.count, "result": result})
    
    return {"title": query.title, "count": query.count, "result": result}

@app.get("/search-results/")
def get_search_results():
    """Endpoint to retrieve search results from the in-memory database."""
    return DATABASE["search_results"]
