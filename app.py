import streamlit as st
from recommendation_engine import recommend_cocktails

st.title('AI Cocktail Assistant')

# User inputs for preferences
user_preference = st.text_input('Enter your preferred ingredient or cocktail name')

# Display recommendations based on the engine
if user_preference:
    recommended_cocktails = recommend_cocktails(user_preference)
    st.write('Recommended Cocktails:', recommended_cocktails)
