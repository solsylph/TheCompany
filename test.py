
import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

def ask_model(question):
    response = openai.ChatCompletion.create(
        model="ft:davinci-002:personal:stats-group-1:9ECSxCFl",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

def main():
    st.title('GPT-based Q&A App')
    user_input = st.text_input("Ask a question:")
    if user_input:
        answer = ask_model(user_input)
        st.text("Answer: " + answer)

if __name__ == "__main__":
    main()
