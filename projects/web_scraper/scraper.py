import requests
from bs4 import BeautifulSoup

# Buddy, this is how you extract info from the web!
def scrape_headlines(url):
    print(f"🕵️ Scraping headlines from {url}...")
    try:
        # In a real scenario, use a site you have permission to scrape!
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # This is a generic example - real tags depend on the site!
        headlines = soup.find_all(['h1', 'h2'])
        
        for i, h in enumerate(headlines[:5], 1):
            print(f"{i}. {h.get_text().strip()}")
            
    except Exception as e:
        print(f"❌ Scraper error: {e}")

if __name__ == "__main__":
    scrape_headlines("https://example.com")
