import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_wikipedia_data(url):
    try:
        # Send a GET request to the Wikipedia URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing country and capital data
        table = soup.find('table', {'class': 'wikitable'})

        # Prepare lists to store the scraped data
        countries = []
        capitals = []

        # Loop through the rows of the table
        for row in table.find_all('tr')[1:]:  # Skip the header row
            cells = row.find_all('td')
            if len(cells) >= 2:  # Ensure there are enough columns
                country = cells[0].get_text(strip=True)
                capital = cells[1].get_text(strip=True)
                countries.append(country)
                capitals.append(capital)

        # Create a DataFrame using the scraped data
        df = pd.DataFrame({
            'Country': countries,
            'Capital': capitals
        })

        return df

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    # URL of the Wikipedia page to scrape
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"
    
    # Scrape data and get the DataFrame
    country_capital_df = scrape_wikipedia_data(url)

    # Print the DataFrame
    if country_capital_df is not None:
        print(country_capital_df)

        # Optionally, save the DataFrame to a CSV file
        country_capital_df.to_csv('countries_and_capitals.csv', index=False)
        print("Data saved to 'countries_and_capitals.csv'.")
