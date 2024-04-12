# CovidTweetViz

## Overview
CovidTweetViz is a web application for analyzing sentiments in COVID-19 related tweets and visualizing sentiment trends over time.

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.

```bash
git clone <repository_url>
cd CovidTweetViz
```

3. Install the required Python dependencies using pip.

```bash
pip install -r requirements.txt
```

## Usage
1. After installing the dependencies, run the Streamlit app using the following command:

```bash
streamlit run app.py
```

2. This will launch the application in your default web browser. 
3. Enter the topic you want to analyze (e.g., "COVID-19") and click on the "Analyze" button.
4. The application will fetch tweets related to the specified topic, perform sentiment analysis, and display the sentiment distribution over time.

## Notes
- Ensure that you have Python installed on your system.
- For best results, use a stable internet connection while running the application to fetch tweets in real-time.
- If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## Acknowledgments
This project utilizes Streamlit for building the web application and various Python libraries for sentiment analysis and data visualization. Special thanks to the developers and contributors of these tools and libraries.
