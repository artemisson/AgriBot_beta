#wolframalpha ID "3KV6VA-V57L4LYWJW"

import wolframalpha

# Replace YOUR_APP_ID with your Wolfram Alpha app ID
client = wolframalpha.Client("3KV6VA-V57L4LYWJW")

question = input("Ask a question: ")

# Send the question to Wolfram Alpha to get the answer
res = client.query(question)

# Print the answer
print(next(res.results).text)

