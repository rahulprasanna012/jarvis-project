# import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Head.Mouth import speak
import os

# Download necessary NLTK data (you only need to run this once, not in production)
# nltk.download('stopwords')
# nltk.download('punkt_tab')

# Load dataset function
def load_dataset(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The dataset file {file_path} does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs]
    return dataset

# Preprocess text function
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# Train the TF-IDF vectorizer function
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']

# Main function that handles user input and provides the answer
def mind(text):
    dataset_path = r'D:\newFinal\Jarvis\Data\brain_data\qna_data.txt'
    try:
        dataset = load_dataset(dataset_path)
        vectorizer, X = train_tfidf_vectorizer(dataset)
        answer = get_answer(text, vectorizer, X, dataset)
        speak(answer)  # Use the speak function to respond
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input loop to keep receiving input
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break  # Stop the loop if the user wants to exit
    mind(user_input)
