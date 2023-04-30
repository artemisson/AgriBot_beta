import wikipedia
import re

# Prompt user to enter a question
question = input("What do you want to know? ")

# Search wikipedia for the question
results = wikipedia.search(question)

# If there are no results, inform the user
if not results:
    print("Sorry, no results found on Wikipedia.")
else:
    # Select the first result and get the page
    page = wikipedia.page(results[0])

    # Clean up the text of the page by removing newlines and references
    text = re.sub(r"\n|\[.*?\]", "", page.content)

    # Split the text into sentences and print the first 5
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
    for i in range(5):
        if i < len(sentences):
            print(sentences[i])
