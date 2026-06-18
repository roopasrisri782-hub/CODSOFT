import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'title': [
        'Harry Potter',
        'The Hobbit',
        'Lord of the Rings',
        'The Alchemist',
        'Da Vinci Code',
        'Angels and Demons',
        'Sherlock Holmes'
    ],
    'genre_description': [
        'Magic Fantasy Adventure',
        'Fantasy Adventure Quest',
        'Fantasy Adventure War Epic',
        'Inspirational Philosophy Spiritual',
        'Mystery Thriller Crime',
        'Mystery Crime Thriller',
        'Detective Mystery Crime Investigation'
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['genre_description'])

similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_books(book_title, num_recommendations=3):
    if book_title not in df['title'].values:
        return f"Book '{book_title}' not found in database."

    book_index = df.index[df['title'] == book_title][0]

    similarity_scores = list(enumerate(similarity_matrix[book_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended = []

    for idx, score in similarity_scores[1:num_recommendations + 1]:
        recommended.append(df.iloc[idx]['title'])

    return recommended

book = "Da Vinci Code"

print(f"Recommended books similar to '{book}':")
print(recommend_books(book, 3))
