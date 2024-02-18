
# AI Cocktail Assistant

The AI Cocktail Assistant is a Streamlit-based web application designed to recommend cocktail recipes based on user preferences. It leverages artificial intelligence (AI) techniques to analyze cocktail recipes and suggest those matching the flavors or ingredients users are interested in.

## Features

- **Cocktail Recommendations**: Users can enter their preferred ingredients or cocktail names to get personalized cocktail suggestions.
- **User-friendly Interface**: The application features an easy-to-navigate interface, making it simple for users to find what they're looking for.

## AI-Driven Recommendation Engine

The core of the AI Cocktail Assistant is its recommendation engine, which utilizes content-based filtering techniques to provide personalized cocktail suggestions. Here's how it works:

- **Data Preparation**: The engine starts by processing a comprehensive dataset of cocktail recipes, including ingredients and flavor profiles.

- **Feature Extraction**: For each cocktail, it extracts features based on the ingredients, their proportions, and associated flavor notes. This step involves natural language processing (NLP) techniques to analyze and encode the recipe text into numerical vectors.

- **Similarity Calculation**: When a user enters a preference, the engine calculates the similarity between the user's input and the feature vectors of all cocktails in the dataset. This calculation uses cosine similarity, a metric for measuring the angle between two vectors in a multi-dimensional space.

- **Cocktail Recommendations**: Based on the similarity scores, the engine ranks the cocktails and suggests the ones most closely matching the user's preferences.

### Installation

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/AICocktailAssistant.git
cd AICocktailAssistant
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the AI Cocktail Assistant, execute the following command from the root directory of the project:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you should be able to access the application by navigating to `http://localhost:8501` in your web browser.

## Usage

- Upon launching the AI Cocktail Assistant, you'll be greeted with a text input box.
- Enter an ingredient (e.g., "Gin") or a cocktail name (e.g., "Negroni") you're interested in.
- The application will display a list of recommended cocktails based on your input.
- If no recommendations are found, try entering a different ingredient or cocktail name.

## Contributing

Contributions to the AI Cocktail Assistant are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License

