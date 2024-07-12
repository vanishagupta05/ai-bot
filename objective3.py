#libraries
import os
import requests
from googlesearch import search
import openai
import re

openai.api_key = os.environ["OPENAI_API_KEY"]


from openai import OpenAI


# Create the OpenAI client
client = OpenAI()


def google_search(query):
   """Perform a Google search and return the top URLs."""
   return list(search(query))


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
       max_tokens=300
   )
   response = completion.choices[0].message.content.strip()
   return response.lower() == "yes"


def check_if_fact(query):
   """Check if the query is a fact using GPT-3.5."""
   messages = [
       {"role": "system", "content": "You are a Chat Bot. Your job is to provide an answer when the user asks you a query."},
       {"role": "user", "content": f"Check if {query} is a fact or not. Reply with 'yes' or 'no'."}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )


   response = completion.choices[0].message.content.strip()
   return response




def summarize_texts(query, texts):
   """Summarize the information from multiple texts using GPT-3.5."""
   combined_text = " ".join(texts)
   messages = [
       {"role": "system", "content": "You are a summarizer."},
       {"role": "user", "content": f"Summarize the following information related to {query}:\n\n{combined_text}"}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )


   response = completion.choices[0].message.content.strip()


   return response


def get_paragraph(query):
    search_results = google_search(query)
    if not search_results:
        return "No search results found."


    answers = []
    for i, url in enumerate(search_results[:5]):
        url_text = get_text_from_url(url)
        answer = find_answer_in_text(query, url_text)


        if answer.lower() != "no clear answer":
            answers.append(answer)
            if len(answers) == 2:
                break
    if not answers:
        return "No clear answer found in the first 5 URLs."


    fact_check = check_if_fact(query)
    if fact_check == "Yes":
        if len(answers) == 2 and check_similarity(answers[0], answers[1]):
            return f"Verified similar answer: {answers[0]}"
        else:
            return f"Found answers: {answers}, but could not verify similarity."
    else:
        additional_texts = [get_text_from_url(url) for url in search_results[:5]]
        summary = summarize_texts(query, additional_texts)
        return f"Summarized information: {summary}"


#IT CHECKS IF IT IS FACT IF YES IT WORKS ON CHECK SIMILARITY OR ELSE IT CALLS THE SUMMARIZING FUNCTION.
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
