**Discussion Analyzer: Unveiling Digital Dialogues**

Welcome to the Discussion Analyzer—a cutting-edge Streamlit web application that harnesses the power of Hugging Face's BERTweet model to decode emotions embedded in Reddit conversations. This tech-savvy tool seamlessly integrates top news topics related to your chosen city, providing a captivating visualization of prevailing sentiments.

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
