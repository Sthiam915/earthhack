ext = '''Herein, we propose an innovative approach to mitigate this problem: Modular Construction. 
    This method embraces recycling and reuse, taking a significant stride towards a circular economy. Modular
    construction involves utilizing engineered components in a manufacturing facility that are later assembled
    on-site. These components are designed for easy disassembling, enabling them to be reused in diverse projects,
    thus significantly reducing waste and conserving resources. Not only does this method decrease construction
    waste by up to 90%, but it also decreases construction time by 30-50%, optimizing both environmental
    and financial efficiency. This reduction in time corresponds to substantial financial savings for
    businesses. Moreover, the modular approach allows greater flexibility, adapting to changing needs over time.
    We believe, by adopting modular construction, the industry can transit from a 'take, make and dispose'
    model to a more sustainable 'reduce, reuse, and recycle' model, driving the industry towards a more
    circular and sustainable future. The feasibility of this concept is already being proven in markets
    around the globe, indicating its potential for scalability and real-world application.'''
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Convert the list of words to a space-separated string
    filtered_text = ' '.join(filtered_words)

    # Use TfidfVectorizer to calculate TF-IDF scores
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([filtered_text])

    # Get feature names (words) and their corresponding TF-IDF scores
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]

    # Combine words with their TF-IDF scores into a list of tuples
    word_tfidf_tuples = list(zip(feature_names, tfidf_scores))

    # Sort the list based on TF-IDF scores in descending order
    sorted_word_tfidf_tuples = sorted(word_tfidf_tuples, key=lambda x: x[1], reverse=True)

    # Extract the top N important phrases (e.g., top 5)
    top_phrases = [word for word, score in sorted_word_tfidf_tuples[:5]]

    # Print the top phrases
    print("Top Phrases:")
    print(top_phrases)
  