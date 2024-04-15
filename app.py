import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

def ask_model(question):
    response = openai.ChatCompletion.create(
        model="ft:davinci-002:personal:stats-group-1:9ECSxCFl",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

st.set_page_config(page_title="Material Finder", layout="wide")

col1, col2 = st.columns([2, 1])

with col1:
    st.title('Material Recommendation System')
    material_query = st.text_input('What material or property are you interested in?')
    if material_query:
        # Display user query
        st.write("You're interested in:", material_query)
        
        # Fetching and displaying the results
        results = ask_model(material_query)
        if results:
            st.write("Results:")
            st.write(results)
        else:
            st.write("Results will be displayed here.")

with col2:
    st.image("TheComp.png", width=300)