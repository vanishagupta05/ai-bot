#tO INSTALL the libraries paste this in the command prompt all the documents till objective 6 will run 
pip install os
pip install requests
pip install google_search
pjp install openai
pip install re

#Importing libraries
import os
import requests
from googlesearch import search
import openai
import re

#FIRST USED THE KEY DIRECTLY BUT DIDN'T WORK HENCE IMPORTED THE OS SYSTEM AND USED THE OPEN API KEY #Using the open API KEY 
from openai import OpenAI


# Create the OpenAI client
client = OpenAI()
def google_search(query, num_results=3):
   """Perform a Google search and return the top URLs."""
   return list(search(query, num_results=num_results))
#Used the search function to google search to get the links to the websites 


def get_text_from_url(url):
   """Fetch and return the first few paragraphs of text from a URL using regex."""
   response = requests.get(url)
   paragraphs = re.findall(r'<p>(.*?)</p>', response.text, re.DOTALL)
   text = ' '.join(paragraph.strip() for paragraph in paragraphs[:7])
   text = re.sub(r'<.*?>', '', text)  # Remove any remaining HTML tags
   return text


def compare_and_summarize( query,text1, text2):
    """Compare two texts using GPT-3.5 and summarize if they are similar."""
    messages = [
       {"role": "system", "content": "You are a Chat Bot. Your job is to provide an answer when the users asks you a query."},
       {"role": "user", "content": f"These two text are answer to the {query}\n Text 1: {text1} \n\n Text 2: {text2}.\nPlease check if these two text provide a good answer.If yes please construct the best concise answer and print only the answer without any explanation"}
   ]
    completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=messages,
       max_tokens=300
   )
#The CHAT Completion method is wrong. Remember to use “ client.chat.completions.create. Now as in the message i used various different prompts a)compare the two text but it wasnt giving the answer it was giving a compare contrast ans 
    return completion.choices[0].message.content.strip()



def get_paragraph(query):
    search_results = google_search(query)
    if len(search_results) < 2:
        return "Not enough information available from search results."


    url_text1 = get_text_from_url(search_results[0])
    url_text2 = get_text_from_url(search_results[1])


    comparison_result = compare_and_summarize(query,url_text1, url_text2)
    return comparison_result


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
