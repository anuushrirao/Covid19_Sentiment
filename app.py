import streamlit as st
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

def set_background(image_url):
    # Embed background image using HTML
    html_code = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(html_code, unsafe_allow_html=True)

# Sentiment Analysis Function
def get_sentiment(text):
    # Create a TextBlob object to analyse sentiment of the text
    blob = TextBlob(text)
    # Extract sentiment polarity and subjectivity from the TextBlob object
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    # Determine sentiment label based on polarity
    if sentiment_polarity > 0:
        sentiment_label = 'Positive  😊'
    elif sentiment_polarity < 0:
        sentiment_label = 'Negative 😞'
    else:
        sentiment_label = 'Neutral 😐'
    # Create a dictionary containing sentiment analysis results
    result = {
        'polarity': sentiment_polarity,
        'subjectivity': sentiment_subjectivity,
        'sentiment': sentiment_label
    }
    # Return the sentiment analysis results dictionary
    return result

# Keyword Extraction Function
def get_tokens(docx, num=30):
    # Count occurrences of each token
    word_tokens = Counter(docx)

    # Get the most common tokens
    most_common = word_tokens.most_common(num)

    # Convert most common tokens into a dictionary
    result = dict(most_common)

    # Return the result
    return result

# Word Cloud Function
def plot_wordcloud(docx):
    mywordcloud = WordCloud().generate(docx)
    st.image(mywordcloud.to_array(), use_column_width=True)

# Function to plot sample graphs from Jupyter files
def plot_graphs():
    count_data = {'sentiment': ['Positive', 'Negative', 'Neutral', 'Positive', 'Positive', 'Negative']}
    count_df = pd.DataFrame(count_data)

    # Plotting countplot
    plt.figure(figsize=(8, 6))
    sns.countplot(data=count_df, x='sentiment')
    st.pyplot()

# Main function to define the Streamlit app
def main():
    set_background("https://img.freepik.com/free-photo/coronavirus-infection-background-with-copy-space_24972-949.jpg?size=626&ext=jpg&ga=GA1.1.1036887265.1712166005&semt=ais")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Covid Sentiment Analysis and Keyword Extraction App")

    # Text input for user to enter text for sentiment analysis
    text = st.text_area("Enter text or tweet for sentiment analysis:", height=200)

    # Button to trigger sentiment analysis
    if st.button("Analyze Sentiment"):
        if text:
            # Perform sentiment analysis
            sentiment = get_sentiment(text)
            st.write(f"Sentiment: {sentiment['sentiment']}")
        else:
            st.warning("Please enter some text.")

    # Button to trigger keyword extraction and word cloud generation
    if st.button("Generate Keyword Word Cloud"):
        if text:
            # Perform keyword extraction
            tokens = text.split()  # Split text into tokens
            keywords = get_tokens(tokens)
            st.write("Keywords:", keywords)

            # Generate and display word cloud
            plot_wordcloud(text)
        else:
            st.warning("Please enter some text.")

    # Button to display sample graphs
    if st.button("Display Bar plot Graphs"):
        plot_graphs()

if __name__ == "__main__":
    main()
