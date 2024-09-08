# AI Bot and Google Search

## Table of Contents
1. [Real-Time Data Retrieval](#objective-1-real-time-data-retrieval)
2. [Multi-Source Data Collection](#objective-2-multi-source-data-collection)
3. [Complex Query Handling](#objective-3-complex-query-handling)
4. [Display URLs with Answers](#objective-4-display-urls-with-answers)
5. [Use GPT-3.5 for Non-Time-Sensitive Queries](#objective-5-use-gpt-35-for-non-time-sensitive-queries)
6. [Handle Multi-Question Queries](#objective-6-handle-multi-question-queries)
7. [User Query and Google Search Integration](#objective-7-user-query-and-google-search-integration)

##  Real-Time Data Retrieval


### Code Explanation
The code focuses on integrating real-time data retrieval with conversational interfaces, leveraging APIs and web scraping techniques.

### Output
1. **User:** How did the president of Iran die?  
   **ChatGPT 3.5:** The current President of Iran, Ebrahim Raisi, is still alive as of my last update. For the latest information, check current news sources.  
   **Bot:** Iran's President Ebrahim Raisi died in a helicopter crash in a remote, mountainous area of Iran's northwest. The crash led to significant political impact in Iran, with concerns about the transition of power.  
   **Inference:** ChatGPT 3.5 cannot provide up-to-date information, while the bot connected to Google Search provides current data.

2. **User:** What is the weather in Bangalore as of today?  
   **ChatGPT 3.5:** I don't have real-time information. Please check a weather website.  
   **Bot:** The best concise answer: "Please check a reliable weather source for current weather conditions in Bangalore."  
   **Inference:** Both systems struggle with real-time weather data.

3. **User:** What is AI?  
   **ChatGPT 3.5:** AI stands for artificial intelligence, which involves simulating human intelligence processes by machines.  
   **Bot:** Artificial intelligence enables machines to simulate human intelligence and perform tasks that usually require human intervention.  
   **Inference:** Both systems can handle generalized questions effectively.

##  Multi-Source Data Collection


### Code Explanation
The code involves querying multiple websites to gather data, ensuring a more comprehensive response. It includes error handling and verification mechanisms.

### Output
1. **User:** What happened in Iran?  
   **Bot:** Found answer: President Ebrahim Raisi died in a helicopter crash near the Azerbaijan border, but could not verify with additional sources.

2. **User:** Is Deepika pregnant?  
   **Bot:** Found answer: Yes, but no further verification available.

3. **User:** What is the temperature in Bangalore?  
   **Bot:** Verified similar answer: No clear answer.

4. **User:** Who is the current Prime Minister of India?  
   **Bot:** Verified similar answer: Prime Minister Shri Narendra Modi.

5. **User:** Will AI take over jobs?  
   **Bot:** No clear answer found, unable to verify.

6. **User:** What is happening in sports in India?  
   **Bot:** No clear answer found, unable to verify.

7. **User:** What does "no clear answer" mean?  
   **Bot:** No consistent information found in any sources.

**Inference:** The bot encounters difficulties retrieving and verifying information, resulting in "no clear answer" for some queries.

## Complex Query Handling
\

### Code Explanation
This code focuses on distinguishing between factual and non-factual questions. For non-factual questions, it summarizes information from multiple sources.

### Output
1. **User:** Who is the President of India?  
   **Bot:** Verified similar answer: Smt. Droupadi Murmu.

2. **User:** Who is the current Secretary-General of the United Nations in 2024?  
   **Bot:** Summarized information: António Guterres is the current Secretary-General. Selection involves recommendations from the Security Council and appointment by the General Assembly.

3. **User:** Who won the 2024 Nobel Peace Prize?  
   **Bot:** Summarized information: The 2024 Nobel Peace Prize will be announced on October 11, 2024. Candidates include organizations promoting democracy.

4. **User:** What is happening in Iran?  
   **Bot:** Summarized information: Iranian President Ebrahim Raisi died in a helicopter crash. The investigation is ongoing.

5. **User:** Who is the current President of the United States in 2024?  
   **Bot:** Summarized information: The 2024 U.S. presidential election will be held on November 5, 2024, with Joe Biden and Donald Trump as key candidates.

6. **User:** Who is the current President of the United States?  
   **Bot:** Verified similar answer: The 46th President is Joseph R. Biden, Jr.

**Inference:** The bot effectively summarizes and verifies information based on the query type, providing detailed responses for complex queries and concise answers for straightforward facts.

## Display URLs with Answers

### Code Explanation
The code retrieves answers from multiple sources and includes the URLs of these sources to ensure the accuracy and credibility of the information provided.

### Output
1. **You:** How did the president of Iran die?  
   **Bot:** Summarized information: Iran's President Ebrahim Raisi, along with the country's foreign minister and seven others, died in a helicopter crash in a remote, mountainous area in Iran. Following this tragic event, there have been discussions about the transition of power according to the Iranian constitution. Analysts suggest that the Supreme Leader of Iran could use this opportunity to encourage less hard-line presidential candidates to run in the upcoming election. The political establishment in Iran is expected to face challenges with legitimacy after the deaths of the President and Foreign Minister. Meanwhile, the Iranian government held an emergency meeting, during which Iran's supreme leader named First Vice President Mohammad Mokhber as acting president and announced five days of mourning in the country. The crash has left Iran without two significant diplomatic figures amidst regional tensions.  
   **Sources:** [CNN](https://www.cnn.com/2024/05/20/middleeast/ebrahim-raisi-dies-succession-what-is-next-explainer-mime-intl/index.html), [AP News](https://apnews.com/article/iran-president-ebrahim-raisi-426c6f4ae2dd1f0801c73875bb696f48), [Alaska Public](https://alaskapublic.org/2024/05/20/irans-president-has-died-in-a-helicopter-crash-state-media-reports/), [ABC News](https://abcnews.go.com/International/wireStory/latest-sign-life-crash-site-helicopter-carrying-irans-110386169)

## Use GPT-3.5 for Non-Time-Sensitive Queries


### Code Explanation
This code determines if a query requires up-to-date information. If it does, Google Search is used; otherwise, GPT-3.5 is used to provide answers.

### Output
1. **Welcome to the AI bot! Ask me anything.**  
   **You:** What are the recent updates happening in the field of AI?  
   **Bot:** Summarized information: Recent updates in the field of AI include Atera incorporating AI as IT professionals' companion, OpenAI securing access to real-time Reddit content, Microsoft launching a new AI-infused PC, Mozilla planning AI features for its Firefox browser, and a focus on how screens before bed affect sleep. Companies are also offering bundled services for cost-conscious viewers, Elon Musk predicting gloomy labor market futures, and the introduction of the Humane AI Pin as a standalone AI device.  
   **Inference:** Since this question is time-sensitive, it took the answer from Google.

2. **You:** Who is the president of India?  
   **Bot:** Verified similar answer: Smt. Droupadi Murmu.  
   **Inference:** Since this question is time-sensitive, it took the answer from Google.

3. **You:** Does the sun rise from east or west?  
   **Bot:** The sun rises in the east and sets in the west. This is a universal phenomenon caused by the Earth's rotation on its axis from west to east.  
   **Inference:** Not a time-sensitive answer, hence given by ChatGPT.

4. **You:** When was the last solar eclipse?  
   **Bot:** Found answers: ['A total solar eclipse was last visible in the United States in 2017.'], but could not verify similarity.  
   **Inference:** Since this question is time-sensitive, it took the answer from Google and printed the answer.

5. **You:** What is the answer to 16*16?  
   **Bot:** The answer to 16 multiplied by 16 is 256.  
   **Inference:** Not a time-sensitive answer, hence given by ChatGPT.

6. **You:** How did the president of Iran die?  
   **Bot:** Summarized information: Iranian President Ebrahim Raisi, along with the country's foreign minister and other officials,

## Handle Multi-Question Queries

### Code Explanation
The AI bot will now be capable of processing multiple question queries, such as planning an itinerary, writing a research paper, or scheduling an event. It will break down these complex queries into smaller, manageable sub-questions. Time-sensitive sub-questions will be handled by Google Search, while general sub-questions will be answered using GPT-3.5. The responses will then be compiled and summarized cohesively for the user.

### Output
**Bot:** Welcome to the AI bot! Ask me anything.
**You:** Plan an intiernary from Bangalore to Los angeles for 10days
**Bot:** Due to the current unavailability of the 10-day itinerary planning site for travel from Bangalore to Los Angeles, it is important to prioritize safety and security during your trip.
1. **Day 1-2 (Bangalore to Los Angeles):**
   - Fly from Bangalore to Los Angeles via Emirates Airlines.
   - Upon arrival in Los Angeles, make sure to follow the COVID-19 safety protocols issued by the Los Angeles World Airports.
   - Check-in at a hotel in Los Angeles, ensuring it follows necessary health and safety guidelines.
   
   *URL for Emirates Airlines flights from Bangalore to Los Angeles:* [Emirates Airlines](https://www.emirates.com/)


2. **Day 3-5 (Exploring Los Angeles):**
   - Explore popular attractions in Los Angeles such as Hollywood Walk of Fame, Universal Studios, Griffith Observatory, and Santa Monica Pier.
   - Visit COVID-19 vaccination and testing sites located in LA County to prioritize health and safety while traveling.


3. **Day 6-8 (Further Exploration of LA County):**
   - Explore more of LA County, including Beverly Hills, Malibu, and the Getty Center.
   - Take time to enjoy the diverse culinary scene of Los Angeles while adhering to any health and safety guidelines in place.


4. **Day 9-10 (Departure from Los Angeles):**
   - Check for any updated travel advisories from the Department of State and the CDC.
   - Plan your journey back
 Sources: https://in.usembassy.gov/covid-19-information/, https://kemlu.go.id/losangeles/en/news/11727/update-indonesia-travel-restrictions, https://www.flylax.com/travelsafely, https://www.usa.gov/covid-international-travel, https://wwwnc.cdc.gov/travel/diseases/covid19, https://www.emirates.com/us/english/destinations/lax/blr/flights-from-los-angeles-to-bengaluru/, https://www.emeraldpalate.com/4-day-los-angeles-itinerary/, https://girleatworld.net/los-angeles-itinerary/, https://www.bontraveler.com/travel-planning-part-3-planning-the-itinerary/


## User Query and Google Search Integration

### Code Explanation
- Generate relevant questions for the user based on their initial query to gather specific details.

- Collect and analyze the user's responses to these questions, ensuring clarity and context.

- Formulate additional queries for Google search to gather any external, up-to-date information needed to address the user’s query fully.

- Search Google, extract relevant data, and summarize the key insights from the gathered results.

- Integrate the user's responses with the summarized information from Google.

- Consult GPT-3.5 to generate a final, comprehensive answer, combining both the user's input and the external data to provide a complete and accurate response.

### Output
**Bot:** Welcome to the AI bot! Ask me anything.
You: Plan a presentation on sustaibility
Please answer the following questions:
**Bot:** Are you looking for suggestions on how to structure the presentation?  
**You:** yes
**Bot:** Do you need help in identifying key points to cover on sustainability?  
**You:** yes
**Bot:** Would you like assistance in creating visual aids for the presentation?  
**You:** if u are able to
**Bot:** Are you interested in incorporating any case studies or examples in the presentation?
**You:** yes
**Bot:** To plan a comprehensive presentation on sustainability, it is essential to consider structuring, key points, visual aids, and the incorporation of case studies or examples. Here is a suggested approach incorporating the provided additional information:

1. **Introduction**
   - Definition of sustainability and its growing importance in organizational strategies.
   - Mention the survey findings that highlight the recognition of ESG strategies in value creation.
   - Overview of the 10 key environmental trends identified for 2024.

2. **Key Points to Cover on Sustainability**
   - Importance of sustainability in meeting regulatory requirements, responding to economic changes, and satisfying consumer expectations.
   - The impact of a coherent ESG strategy on creating sustainable value and financial success.
   - Discussion on the 10 key environmental sustainability trends shaping organizational decisions in 2024.
   
3. **Structuring the Presentation**
   - Begin with an attention-grabbing introduction to set the context.
   - Present key points logically, building a narrative that emphasizes the urgency of sustainability practices.
   - Conclude with a call to action or reflection on the future of sustainability initiatives.

4. **Visual Aids
   - Incorporate visual elements such as graphs, charts, infographics, and images to enhance the presentation's engagement and clarity.
   - Utilize statistics and data points to visually represent the significance of sustainability efforts.
   - Provide visual comparisons or timelines to illustrate trends and projections effectively.

5. **Case Studies or Examples**
   - Integrate real-world case
 Sources: https://www.techtarget.com/sustainability/feature/Business-sustainability-trends, https://www.epa.gov/sustainability/learn-about-sustainability, https://www.techtarget.com/sustainability/feature/Business-sustainability-trends, https://sustainabilitymag.com/esg/esg-policy-and-regulation-what-to-prepare-for-in-2024, https://www.sapfioneer.com/blog/blogpost/what-to-expect-in-2024-changes-in-esg-regulation-and-what-fsis-need-to-know/, https://www.forbes.com/sites/forbestechcouncil/2024/01/09/five-sustainability-technologies-to-anticipate-in-2024/, https://blog.ragnarson.com/what-are-new-technologies-in-sustainable-development/