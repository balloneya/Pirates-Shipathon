import streamlit as st
import joblib
import re

# Load the saved model and vectorizer
model = joblib.load('genre_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

st.set_page_config(page_title="LyricSense", page_icon="🎵")

st.title("🎵 LyricSense: Genre Predictor")
st.markdown("Enter song lyrics below to see which genre our model identifies.")

# User Input
user_lyrics = st.text_area(
    "Song Lyrics", placeholder="Paste lyrics here...", height=200)

if st.button("Predict Genre"):
    if user_lyrics.strip():
        # Preprocessing (Matching your 'Zero-Loop' training logic)
        cleaned = user_lyrics.lower()
        cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned)

        # Transformation and Prediction
        features = tfidf.transform([cleaned])
        prediction = model.predict(features)[0]
        probs = model.predict_proba(features)[0]

        # Results UI
        st.subheader(f"Predicted Genre: **{prediction}**")

        # Displaying probabilities for each genre
        st.write("### Confidence Breakdown")
        for genre, prob in zip(model.classes_, probs):
            st.write(f"**{genre}**")
            st.progress(float(prob))
    else:
        st.warning("Please enter some lyrics first!")
