import streamlit as st
import joblib
import re
import time

# 1. High-Performance Asset Loading (Cached for local speed)


@st.cache_resource
def load_assets():
    model = joblib.load('genre_model.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    return model, tfidf


model, tfidf = load_assets()

# 2. Page Configuration
st.set_page_config(
    page_title="LyricSense - AI Genre Predictor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. Ultra-Modern CSS with Animated Background
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #1e293b, #0f172a);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating Orbs Animation */
    .stApp::before {
        content: '';
        position: fixed;
        top: 10%;
        left: 10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.15), transparent);
        border-radius: 50%;
        filter: blur(80px);
        animation: float 20s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    .stApp::after {
        content: '';
        position: fixed;
        bottom: 10%;
        right: 10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.15), transparent);
        border-radius: 50%;
        filter: blur(80px);
        animation: float 25s ease-in-out infinite reverse;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(0, 0); }
        25% { transform: translate(50px, -50px); }
        50% { transform: translate(-30px, 30px); }
        75% { transform: translate(40px, 20px); }
    }
    
    /* Main Content Container */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
        position: relative;
        z-index: 1;
    }
    
    /* Title Section */
    .main-title {
        text-align: center;
        font-size: 5.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #10b981 0%, #a78bfa 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -3px;
        animation: fadeInDown 0.8s ease-out;
        line-height: 1.1;
    }
    
    .subtitle {
        text-align: center;
        color: #d1d5db;
        font-size: 1.35rem;
        margin-bottom: 3rem;
        animation: fadeInUp 0.8s ease-out;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    .icon-decoration {
        display: inline-block;
        color: #10b981;
        animation: pulse 2s ease-in-out infinite;
        margin: 0 8px;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.1); }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Glass Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2.5rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease;
        animation: fadeIn 0.6s ease-out;
    }
    
    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6);
        border-color: rgba(168, 85, 247, 0.3);
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.3rem;
        font-weight: 700;
        color: #f3f4f6;
        margin-bottom: 1.5rem;
    }
    
    .section-icon {
        color: #10b981;
        font-size: 1.5rem;
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 2px solid rgba(168, 85, 247, 0.2) !important;
        border-radius: 16px !important;
        color: #f3f4f6 !important;
        font-size: 1.05rem !important;
        padding: 1.2rem !important;
        line-height: 1.7 !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(168, 85, 247, 0.6) !important;
        box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.2) !important;
        background: rgba(15, 23, 42, 0.8) !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: #9ca3af !important;
        opacity: 0.8 !important;
    }
    
    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #10b981 0%, #8b5cf6 100%) !important;
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        padding: 1rem 2.5rem !important;
        border-radius: 16px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3) !important;
        margin-top: 1.5rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 15px 35px rgba(16, 185, 129, 0.4) !important;
        background: linear-gradient(135deg, #059669 0%, #7c3aed 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(1.01) !important;
    }
    
    /* Result Card */
    .result-card {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 3rem 2rem;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        animation: slideInUp 0.6s ease-out;
        margin-top: 2rem;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .result-label {
        text-transform: uppercase;
        color: #9ca3af;
        letter-spacing: 3px;
        font-size: 0.875rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .result-genre {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #10b981 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 1rem 0;
        letter-spacing: -2px;
        animation: scaleIn 0.5s ease-out 0.3s both;
    }
    
    @keyframes scaleIn {
        from {
            transform: scale(0.8);
            opacity: 0;
        }
        to {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    .confidence-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.2);
        border: 2px solid #10b981;
        border-radius: 12px;
        padding: 0.5rem 1.5rem;
        font-size: 1.25rem;
        font-weight: 700;
        color: #10b981;
        margin-top: 1rem;
        animation: fadeIn 0.5s ease-out 0.5s both;
    }
    
    /* Genre Breakdown */
    .breakdown-title {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        color: #f3f4f6;
        margin: 2.5rem 0 1.5rem 0;
    }
    
    .genre-item {
        margin-bottom: 1.5rem;
        animation: fadeInLeft 0.4s ease-out both;
    }
    
    .genre-item:nth-child(1) { animation-delay: 0.1s; }
    .genre-item:nth-child(2) { animation-delay: 0.2s; }
    .genre-item:nth-child(3) { animation-delay: 0.3s; }
    .genre-item:nth-child(4) { animation-delay: 0.4s; }
    .genre-item:nth-child(5) { animation-delay: 0.5s; }
    
    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .genre-label {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e5e7eb;
        margin-bottom: 0.5rem;
    }
    
    .genre-percent {
        color: #a78bfa !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #8b5cf6 0%, #ec4899 100%) !important;
        border-radius: 10px !important;
        height: 8px !important;
    }
    
    .stProgress > div > div > div {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        height: 8px !important;
    }
    
    /* Warning/Info Messages */
    .stAlert {
        background: rgba(245, 158, 11, 0.1) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
        border-radius: 12px !important;
        color: #fbbf24 !important;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: #6b7280;
        font-size: 0.875rem;
        margin-top: 3rem;
        padding: 1rem;
        animation: fadeIn 1s ease-out 0.8s both;
    }
    
    /* Loading Animation */
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255, 255, 255, 0.3);
        border-top-color: #10b981;
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
    }
</style>
""", unsafe_allow_html=True)

# 4. Header Section
st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="margin-bottom: 1.5rem;">
            <span style="font-size: 4rem;">🎵</span>
            <span class="icon-decoration" style="font-size: 2rem;">✨</span>
        </div>
        <h1 class="main-title">LyricSense</h1>
        <p class="subtitle">
            <span class="icon-decoration">✨</span>
            AI-Powered Genre Intelligence Engine
            <span class="icon-decoration">✨</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. Main Content - Input Section
col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-header">
            <span class="section-icon">🎤</span>
            <span>Drop your lyrics below</span>
        </div>
    """, unsafe_allow_html=True)

    user_lyrics = st.text_area(
        "",
        placeholder="Paste your song lyrics here...\n\nExample:\nBaby, I'm dancing in the dark\nWith you between my arms\nBarefoot on the grass\nListening to our favorite song...",
        height=280,
        label_visibility="collapsed"
    )

    analyze_button = st.button("🚀 Analyze Track")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Prediction Logic
if analyze_button:
    if user_lyrics.strip():
        # Show loading state
        with st.spinner(''):
            st.markdown("""
                <div style="text-align: center; padding: 2rem;">
                    <div class="loading-spinner"></div>
                    <p style="color: #9ca3af; margin-top: 1rem;">Analyzing lyrics with AI...</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)  # Brief pause for UX

        # Preprocessing on local hardware
        cleaned = user_lyrics.lower()
        cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned)
        features = tfidf.transform([cleaned])
        prediction = model.predict(features)[0]
        probs = model.predict_proba(features)[0]

        # Get top confidence score
        max_prob = max(probs) * 100

        # Display Result Card
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.markdown(f"""
                <div class="result-card">
                    <p class="result-label">Predicted Genre</p>
                    <h1 class="result-genre">{prediction}</h1>
                    <div class="confidence-badge">{max_prob:.0f}% Confidence</div>
                </div>
            """, unsafe_allow_html=True)

            # Genre Breakdown Section
            st.markdown(
                '<h3 class="breakdown-title">📊 Genre Breakdown</h3>', unsafe_allow_html=True)

            st.markdown(
                '<div class="glass-card" style="margin-top: 1.5rem;">', unsafe_allow_html=True)

            genre_probs = sorted(zip(model.classes_, probs),
                                 key=lambda x: x[1], reverse=True)

            # Show top 5 genres
            for i, (genre, prob) in enumerate(genre_probs[:5]):
                percentage = float(prob) * 100

                st.markdown(f'<div class="genre-item">',
                            unsafe_allow_html=True)

                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(
                        f'<p class="genre-label">{genre}</p>', unsafe_allow_html=True)
                with c2:
                    st.markdown(
                        f'<p class="genre-percent">{percentage:.1f}%</p>', unsafe_allow_html=True)

                st.progress(float(prob))
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some lyrics to analyze!")

# 7. Footer
st.markdown("""
    <div class="footer-text">
        <p>Powered by Advanced Machine Learning • Logistic Regression Model</p>
    </div>
""", unsafe_allow_html=True)
