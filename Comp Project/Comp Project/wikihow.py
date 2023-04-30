import requests
from bs4 import BeautifulSoup

# Prompt user to enter a search query
query = input("What do you want to learn on wikiHow? ")

# Construct the search URL with the query
url = f"https://www.wikihow.com/wikiHowTo?search={query}"

# Send a GET request to the search URL and get the HTML response
response = requests.get(url)
html = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the search result titles and summaries on the page
results = soup.select(".searchresult")

# Print the titles and summaries of the top 5 search results
for i in range(5):
    if i < len(results):
        # Find the title and summary elements for each search result
        title_element = results[i].select_one(".result_title > a")
        summary_element = results[i].select_one(".searchresult_summary")

        # Extract the title and summary text from the elements
        title = title_element.text.strip()
        summary = summary_element.text.strip() if summary_element else ""

        # Print the title and summary of the search result
        print(f"{i+1}. {title}\n{summary}\n")
