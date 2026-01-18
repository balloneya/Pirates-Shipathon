import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

df = pd.read_csv('train.csv', engine='python', on_bad_lines='skip')

if len(df) > 50000:
    df = df.sample(n=50000, random_state=42)


df['Lyrics'] = df['Lyrics'].str.lower()
df['Lyrics'] = df['Lyrics'].str.replace(
    r'[^a-z0-9\s]', '', regex=True).fillna('')


tfidf = TfidfVectorizer(stop_words='english',
                        max_features=2000, min_df=10, sublinear_tf=True)
X = tfidf.fit_transform(df['Lyrics'])
Y = df['Genre']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)


model = OneVsRestClassifier(LogisticRegression(
    solver='liblinear', max_iter=1000))
model.fit(X_train, Y_train)

joblib.dump(model, 'genre_model.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')

print(f"Accuracy: {model.score(X_test, Y_test):.2f}")

test_lyric = "Neon lights hum over cracked concrete dreams"

cleaned_lyric = test_lyric.lower()
cleaned_lyric = re.sub(r'[^a-z0-9\s]', '', cleaned_lyric)

numerical_features = tfidf.transform([cleaned_lyric])
prediction = model.predict(numerical_features)
probabilities = model.predict_proba(numerical_features)

print(f"Predicted Genre: {prediction[0]}")
