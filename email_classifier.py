from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

class EmailClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, emails, labels):
        X = self.vectorizer.fit_transform(emails)
        self.model.fit(X, labels)

    def classify(self, email):
        X = self.vectorizer.transform([email])
        return self.model.predict(X)[0]
