import wikipedia

question = input("What would you like to know? ")
results = wikipedia.search(question)

if len(results) > 0:
    page = wikipedia.page(results[0])
    print(page.summary)
else:
    print("Sorry, I could not find an answer to your question.")
