import streamlit as st
from geonamescache import GeonamesCache
from datetime import datetime, timedelta
import requests
import praw

import requests

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-emotion-analysis"
HEADERS = {"Authorization": "Bearer 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"}  

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

def get_most_probable_emotion(output):
    if output and isinstance(output, list) and output[0]:
        # Extract the inner list of dictionaries from the 'output'
        inner_list = output[0]

        # Remove dictionaries with the label 'others' from the inner list
        inner_list_without_others = [d for d in inner_list if d.get('label') != 'others']

        # Check if there are remaining dictionaries after removing 'others'
        if inner_list_without_others:
            # Find the dictionary with the highest 'score' within the updated inner list
            most_probable_dict = max(inner_list_without_others, key=lambda x: x['score'])

            # Extract the emotion label from the dictionary
            most_probable_emotion = most_probable_dict.get('label', None)

            # Return the most probable emotion label
            return most_probable_emotion

    # Return None if 'output' is empty or not in the expected format
    return None

def query_api(texto):
    result = query({"inputs": texto})
    return get_most_probable_emotion(result)

def analyze_emotions(reddit_comments):
    emotions = [query_api(comment) for comment in reddit_comments]
    
    most_common_emotion = max(set(emotions), key=emotions.count, default=None)

    return most_common_emotion

# Function to fetch top topics from News API
def fetch_top_topics(city_name):
    # Using News API key
    api_key = 'd70cc473c63a4533954eebb70e218b8c' 

    # Calculate the start date (one week ago) and end date (today)
    end_date = datetime.now().isoformat()  # Current date and time
    start_date = (datetime.now() - timedelta(days=7)).isoformat()  # One week ago

    url = f'https://newsapi.org/v2/everything?apiKey={api_key}&q={city_name}&sortBy=popularity&from={start_date}&to={end_date}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        top_topics = []

        for article in articles[:5]:
            title = article.get('title', 'N/A')
            description = article.get('description', 'N/A')

            # Append the formatted information to the top_topics list
            top_topics.append({
                'title': title,
                'description': description
            })

        return top_topics
    else:
        print(f"Error: {response.status_code}")
        return []

# Function to fetch Reddit comments
def fetch_reddit_comments(topic, subreddit_name='all', limit=5, max_comments=20):
    reddit = praw.Reddit(client_id='hOs9o7wIw79c3KFKDrdBEQ',
                         client_secret='6ZGyXd5tuynhrGl-l11KgkWo00vGiw',
                         user_agent='EDA by Phantom_Harsh',
                         check_for_async=False)

    comments_list = []

    # Iterate through the top posts
    for submission in reddit.subreddit(subreddit_name).search(topic, sort='hot', limit=limit):
        # Check if the submission is a self-post (text-based Reddit post)
        if submission.is_self:
            submission.comments.replace_more(limit=None)
            comments_list.extend([comment.body for comment in submission.comments.list() if isinstance(comment, praw.models.Comment)])

        # Check if we have reached the desired number of comments
        if len(comments_list) >= max_comments:
            break

    return comments_list[:max_comments]

# Fetch a list of city names
gc = GeonamesCache()
all_cities = [city['name'] for city in gc.get_cities().values()]

# Custom CSS for styling
custom_styles = """
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
    }
    .stButton {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton:hover {
        background-color: #45a049;
    }
"""

# Emotion to Emoji mapping
emotion_to_emoji = {
    'joy': '😊',
    'sadness': '😢',
    'anger': '😡',
    'fear': '😨',
    'disgust': '🤢',
    'neutral': '😐'
}

def main():
    # Apply custom CSS
    st.markdown(f'<style>{custom_styles}</style>', unsafe_allow_html=True)

    st.title('Discussion Analyzer')

    with st.form(key='city_form'):
        # Form to enter the city name with autocomplete using selectbox
        city_name = st.selectbox('Enter City Name:', all_cities, key='city_input')

        # Trigger analysis when Enter key is pressed
        submit_button = st.form_submit_button(label='Submit')

        if submit_button and city_name:
            # Call the fetch_top_topics function to retrieve top topics for the selected city
            topics = fetch_top_topics(city_name)

            with st.spinner(f"Fetching top topics for the city: {city_name}..."):
                st.markdown("---")
                # Display the top 5 topics from News API in expanders
                st.subheader(f'Top 5 Topics in {city_name} (News API and Reddit Comments):')
                for i, topic in enumerate(topics, 1):
                    # Call the fetch_reddit_comments function to retrieve Reddit comments for each topic
                    reddit_comments = fetch_reddit_comments(topic['title'])
                    most_common_emotion = analyze_emotions(reddit_comments)

                    # Display sentiment in bracket and bold format with corresponding emojis
                    if most_common_emotion:
                        sentiment_display = f"**[{most_common_emotion.capitalize()} {emotion_to_emoji.get(most_common_emotion, '')}]**"
                    else:
                        sentiment_display = "**[Neutral 😐]**"

                    with st.expander(f"{i}. {topic['title']} {sentiment_display}"):
                        st.write(f"**Description:** {topic['description']} \n\n **Reddit Comments:**\n")
                        st.write('\n'.join([f"- {comment}" for comment in reddit_comments]))
                    st.markdown("---")

if __name__ == "__main__":
    main()
