from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()
import streamlit as sl


print(type(sentiment.polarity_scores("meow")))
sl.title("Enter A Statement")
text = str(sl.text_input("Type Here"))
pol=sentiment.polarity_scores(text)
sl.dataframe(pol)