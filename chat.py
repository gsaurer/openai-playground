from ast import While
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

keepGoing = True

while keepGoing:
  message = input("User : ")
  if message:
    if message != "EXIT":
      messages.append(
            {"role": "user", "content": message},
        )
      completion = client.chat.completions.create(
          model="gpt-4o-mini", messages=messages
      )

      print(completion.choices[0].message.content)
    else:
      keepGoing = False