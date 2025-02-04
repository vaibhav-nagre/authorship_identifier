import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def process_data(filename, known_dir):
    with open(filename, 'r') as file:
        input_text = file.read()
    
    known_texts = []
    author_names = []
    for author_file in os.listdir(known_dir):
        author_path = os.path.join(known_dir, author_file)
        if os.path.isfile(author_path):
            with open(author_path, 'r') as file:
                known_texts.append(file.read())
                author_names.append(os.path.splitext(author_file)[0])

    texts = [input_text] + known_texts
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    best_match_index = cosine_similarities.argmax()
    
    best_match_author = author_names[best_match_index]
    
    print(f"Debug: Found best match author: {best_match_author}")
    return best_match_author

def extract_author_name(best_match_author):
    # Since process_data now returns the author name directly, we can just return it
    if best_match_author is None:
        print("Debug: No best match author provided")
        return None
    
    print(f"Debug: Extracted author name: {best_match_author}")
    return best_match_author

def make_guess(known_dir):
    filename = input('Enter filename (include the full path if needed): ').strip()
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    best_match_author = process_data(filename, known_dir)
    print(f"Debug: best_match_author = {best_match_author}")  # Debug print
    author_name = extract_author_name(best_match_author)  # Extract the author's name
    print(f"Debug: author_name = {author_name}")  # Debug print
    print(f"The most likely author match for '{filename}' is: {author_name}")

# Run the function
if __name__ == "__main__":
    make_guess('known_authors')