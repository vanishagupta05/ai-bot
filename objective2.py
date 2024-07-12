import os
import requests
from googlesearch import search
import openai
import re

from openai import OpenAI


# Create the OpenAI client
client = OpenAI()


def google_search(query, num_results=20):
   """Perform a Google search and return the top URLs."""
   return list(search(query, num_results=num_results))


def get_text_from_url(url):
   """Fetch and return the first few paragraphs of text from a URL using regex."""
   response = requests.get(url)
   paragraphs = re.findall(r'<p>(.*?)</p>', response.text, re.DOTALL)
   text = ' '.join(paragraph.strip() for paragraph in paragraphs[:7])
   text = re.sub(r'<.*?>', '', text)  # Remove any remaining HTML tags
   return text


def find_answer_in_text(query, text):
   """Check if the text contains an answer to the query using GPT-3.5."""
   messages = [
       {"role": "system", "content": "You are a Chat Bot. Your job is to provide an answer when the user asks you a query."},
       {"role": "user", "content": f"Query: {query}\nText: {text}\nDoes this text contain a clear answer to the query? If yes, please provide only the answer no explanation required, otherwise say 'No clear answer'."}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )
   response = completion.choices[0].message.content.strip()
   return response


def check_similarity(answer1, answer2):
   """Check if two answers are similar using GPT-3.5."""
   messages = [
       {"role": "system", "content": "You are a similarity checker."},
       {"role": "user", "content": f"Are these two answers similar?\nAnswer 1: {answer1}\nAnswer 2: {answer2}\nReply with 'Yes' or 'No'."}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=10
   )
   response = completion.choices[0].message.content.strip()
   return response.lower() == "yes"


def get_paragraph(query):
   search_results = google_search(query)


   if not search_results:
       return "No search results found."


   for i, url in enumerate(search_results):
       url_text = get_text_from_url(url)
       answer = find_answer_in_text(query, url_text)


       if answer.lower() != "no clear answer":
           # Check if a similar answer can be found in the next URL for verification
           if i + 1 < len(search_results):
               next_url_text = get_text_from_url(search_results[i + 1])
               verification_answer = find_answer_in_text(query, next_url_text)


               if verification_answer.lower() != "no clear answer" and check_similarity(answer, verification_answer):
                   return f"Verified similar answer: {answer}"
               else:
                   return f"Found answer: {answer}, but could not verify with the next URL."
           else:
               return f"Found answer: {answer}, but no more URLs to verify."


   return "No clear answer found in any of the URLs."
#The difference in the code is that rather than taking only 2 urls it iterates through more number of urls and tries to find the answer it verifies with the next link and returns the answer.

def main():
   print("Welcome to the AI bot! Ask me anything.")
   while True:
       user_input = input("You: ")
       if user_input.lower() == 'exit':
           print("Exiting...")
           break
       paragraph = get_paragraph(user_input)
       print("Bot:", paragraph)


if __name__ == "__main__":
   main()
