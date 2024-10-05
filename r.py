import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_titles(url):
    try:
        # Send a GET request to the Wikipedia URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all featured article titles (located in <h1> and <h2> tags)
        titles = soup.find_all(['h1', 'h2'])

        # Print the titles
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text(strip=True)}")

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

if __name__ == "__main__":
    # Wikipedia main page URL
    url = "https://en.wikipedia.org/wiki/Main_Page"
    scrape_wikipedia_titles(url)
