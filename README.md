**Discussion Analyzer: Unveiling Digital Dialogues**

Welcome to the Discussion Analyzer—a cutting-edge Streamlit web application that harnesses the power of Hugging Face's BERTweet model to decode emotions embedded in Reddit conversations. This tech-savvy tool seamlessly integrates top news topics related to your chosen city, providing a captivating visualization of prevailing sentiments.

**Objective:**
The goal of this project is to build a comprehensive system that gauges sentiments and discussions circulating around a specific political topic in a chosen city. The approach involves fetching top news topics, extracting keywords, gathering Reddit comments, and employing sentiment analysis.

**APPROACH :**

***Step 1: Fetching Top Topics for a City***
In the initial step, I utilized the News API to gather real-time news about a specified city. The fetch_top_topics function takes parameters such as the country code, API key, and city name to retrieve the top news topics. This sets the foundation for understanding what is currently being discussed in the city.

***Step 2: Extracting Keywords and Fetching Reddit Comments***
To delve deeper into discussions, I employed the extract_keywords function to pull out keywords from the news headlines obtained in Step 1. These keywords act as focal points for further analysis. Subsequently, I used the PRAW library to fetch comments from Reddit using the fetch_reddit_comments function. This step provides a real-time perspective from public forums.

***Step 3: Sentiment Analysis Using a Pre-trained Model***
Sentiment analysis is crucial in understanding the overall mood of discussions. I incorporated a pre-trained model to analyze the sentiment or emotion expressed in the Reddit comments. The get_most_probable_emotion function extracts the most probable emotion from the model's output, providing a nuanced perspective on the discussions.

***Step 4: Building a Front-End with Streamlit***
To make the insights accessible, I developed a user-friendly front-end using Streamlit. This web application allows users to input a city name, select relevant sources (News API and Reddit), and view the analyzed results. The application provides a structured display of top news topics, sentiment analysis, and key comments from Reddit discussions.


**[Live Demo](https://reddit-discussion-analyzer.streamlit.app/)**

### Features:

- **Emotion Analysis:** Leverage Hugging Face's BERTweet model to unearth the emotional undercurrents within Reddit comments.
  
- **News API Integration:** Fetch top news topics for your selected city and unravel the intersections with Reddit discussions.

- **User-Friendly Interface:** Streamlit's intuitive design ensures a seamless and visually appealing user experience.

- **Custom Styling:** Immerse yourself in a sleek and stylish UI, enhancing the overall aesthetic of your exploration.

### How to Use:

1. **City Selection:**
   - Choose a city from the dropdown menu to kickstart the analysis.

2. **Emotionally Intelligent Results:**
   - Explore the top 5 news topics related to your chosen city, complete with Reddit comments and an emotive analysis, elegantly presented in a series of expandable sections.

3. **Interactive Analysis:**
   - Uncover the prevailing emotions in each topic, supported by an emoji-mapped sentiment display.

### Installation:

1. Clone the repository:
   ```bash
   git clone [repository_url]
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run EDA.py
   ```

### Customization:

- **API Keys:**
  - Replace placeholders with your own API keys for Hugging Face and News API.

- **Styling:**
  - Tailor the CSS in the `custom_styles` variable to align with your preferred visual aesthetics.

### Requirements:

- Python 3.x
- Streamlit
- Geonamescache
- Requests
- Praw

### Get Involved:

Contributions and feedback are welcomed! Feel free to open issues, submit pull requests, or share your thoughts to enhance the Discussion Analyzer.

### Acknowledgments:

- Built with Streamlit, Hugging Face, and News API.
- Special thanks to the open-source community for creating the tools that power this project.

Happy analyzing! 🚀✨
