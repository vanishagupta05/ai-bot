#Importing libraries 
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
   text = ' '.join(paragraph.strip() for paragraph in paragraphs[:4])
   text = re.sub(r'<.*?>', '', text)  # Remove any remaining HTML tags
   return text


def find_answer_in_text(query, text):
   """Check if the text contains an answer to the query using GPT-3.5."""
   messages = [
       {"role": "system", "content": "You are a Chat Bot. Your job is to provide an answer when the user asks you a query in 60-70 words."},
       {"role": "user", "content": f"Query: {query}\nText: {text}\nDoes this text contain a clear answer to the query? If yes, please provide only the answer no explanation required, otherwise say 'No clear answer'."}
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
       {"role": "user", "content": f"Summarize the following information related to {query} in a concise way atmost 80 words :\n\n{combined_text} "}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )
   response = completion.choices[0].message.content.strip()
   return response


def is_recent_information_needed(query):
   """Check if the query requires information from the last 2 years using GPT-3.5."""
   messages = [
       {"role": "system", "content": "You are a Chat Bot. Your job is to determine if a query requires recent information."},
       {"role": "user", "content": f":Provide me with any  time sensitive  factual information that will make you answer the following query in a better way in the form of 1-4 relevant short  proper  questions with key words  the query is Query: {query} Please consider recent trends, updates, or changes in the relevant field.?"}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )
   response = completion.choices[0].message.content.strip()
   return response


def get_answer_from_gpt(answer,query):
   """Get the answer directly from GPT-3.5."""
   messages = [
       {"role": "system", "content": "You are a knowledgeable assistant."},
       {"role": "user", "content": f"Answer the following query :\nQuery: {query}  in the best possible way with  the additional information{answer} and use your own previous knowgledge to give the full answer  with the urls"}
   ]
   completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )
   response = completion.choices[0].message.content.strip()
   return response




def get_paragraph(query):
    """Decide whether to use Google search or directly use GPT-3.5 based on the recency requirement of the query."""
    sub_questions=is_recent_information_needed(query).split('\n')
    additional_texts = []
    info_per_question=[]
    url_lst = []
    for question in sub_questions:
        search_results = google_search(question)
        for url in search_results[:3]:
            text = get_text_from_url(url)
        if text:
            info_per_question.append(text)
            url_lst.append(url)
        summary = summarize_texts(query, info_per_question)
        additional_texts.append(summary)
    if additional_texts:
        final_answer = get_answer_from_gpt(additional_texts, query)
        return f"{final_answer}\n Sources: {', '.join(url_lst)}"
    else:
        return "No relevant information found."





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