# recommendation_engine.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data_preparation import cocktails_df  # Import the DataFrame from data_preparation module

def calculate_similarity():
    # Calculate the cosine similarity matrix
    similarity_matrix = cosine_similarity(cocktails_df.values)
    return pd.DataFrame(similarity_matrix, index=cocktails_df.index, columns=cocktails_df.index)

def recommend_cocktails(cocktail_name, top_n=5):
    similarity_matrix = calculate_similarity()
    if cocktail_name not in similarity_matrix.index:
        return f"No data for cocktail named '{cocktail_name}'."
    # Get similarity values with other cocktails
    similarities = similarity_matrix[cocktail_name]
    # Get top N most similar cocktails, excluding itself
    recommended = similarities.sort_values(ascending=False)[1:top_n+1]
    return recommended.index.tolist()
