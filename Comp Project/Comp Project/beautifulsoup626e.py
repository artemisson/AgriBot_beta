import requests
from bs4 import BeautifulSoup

def google_search(question):
    # Set up the Google Search API endpoint and parameters
    url = "https://www.google.com/search"
    params = {
        "q": question,
        "hl": "en"
    }

    # Send a GET request to the API and retrieve the response HTML
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first search result and extract the text
    result = soup.find("div", class_="Z0LcW")
    if result:
        return result.get_text()
    else:
        return "Sorry, I could not find an answer to your question."

# Example usage
question = input("Ask me a question: ")
answer = google_search(question)
print(answer)
