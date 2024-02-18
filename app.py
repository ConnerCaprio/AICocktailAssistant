import streamlit as st
from recommendation_engine import recommend_cocktails

st.title('AI Cocktail Assistant')

user_preference = st.text_input('Enter your preferred ingredient or cocktail name, Try "Negroni"!').strip()

if user_preference:
    recommended_cocktails = recommend_cocktails(user_preference)
    if recommended_cocktails and isinstance(recommended_cocktails, list) and recommended_cocktails != []:
        st.subheader('Recommended Cocktails:')
        # Display each recommended cocktail in a bulleted list
        for cocktail in recommended_cocktails:
            st.markdown(f"- {cocktail}")
    elif isinstance(recommended_cocktails, str):
        # Handle the case where a message is returned instead of a list
        st.write(recommended_cocktails)
    else:
        st.write("No recommendations found. Try another ingredient or cocktail name.")
