import streamlit as st
import joblib
import re

model = joblib.load('genre_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

st.set_page_config(page_title="LyricSense", page_icon="🎵", layout="centered")

st.markdown("""
    <style>
    /* Background with light staff notation */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/music.png");
        background-color: #f8f9fa;
        background-attachment: fixed;
    }

    /* Styling the main title */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #1DB954; /* Spotify Green */
        text-align: center;
        margin-bottom: 0px;
    }

    /* Subtitle styling */
    .sub-title {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Customizing the prediction button */
    div.stButton > button:first-child {
        background-color: #1DB954;
        color: white;
        width: 100%;
        border-radius: 20px;
        border: none;
        height: 3em;
        font-weight: bold;
    }

    /* Result Card */
    .result-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<p class="main-title">🎵 LyricSense</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI-Powered Music Genre Prediction</p>',
            unsafe_allow_html=True)


st.write("---")
user_lyrics = st.text_area("Paste song lyrics below:",
                           placeholder="e.g., Neon lights hum over cracked concrete dreams...", height=200)

if st.button("Identify Genre"):
    if user_lyrics.strip():

        cleaned = user_lyrics.lower()
        cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned)

        features = tfidf.transform([cleaned])
        prediction = model.predict(features)[0]
        probs = model.predict_proba(features)[0]

        st.markdown(f"""
            <div class="result-card">
                <h2 style='text-align: center; color: #1DB954;'>Predicted Genre: {prediction}</h2>
            </div>
        """, unsafe_allow_html=True)

        st.write("### 📊 Confidence Breakdown")
        cols = st.columns(len(model.classes_))

        for i, genre in enumerate(model.classes_):
            with cols[i]:
                confidence = float(probs[i]) * 100
                st.metric(label=genre, value=f"{confidence:.1f}%")
                st.progress(float(probs[i]))
    else:
        st.warning("Please enter some lyrics first!")
