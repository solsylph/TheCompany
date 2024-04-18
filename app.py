
import streamlit as st
import openai
import clipboard

# Using Streamlit's secrets management for secure use of OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Target fine-tuned model
job_id = "ftjob-GxFmlxBOpMJNbO9ySigJl427"
model_name_pre_obj = openai.FineTuningJob.retrieve(job_id)
model_name = model_name_pre_obj.fine_tuned_model
print(f"Using model: {model_name}")

# Function which makes the API call to OpenAI for the fine-tuned model's generation
def get_recommendations(title, description):
    try:
        response = openai.ChatCompletion.create(
            model=model_name
            , messages=[
                {"role": "system", "content": "You are a chatbot trained to be an expert in e-commerce optimization of product titles and descriptions for better sales on Amazon."},
                {"role": "user", "content": f"Can you suggest improvements for this product?\nTitle: {title}\nDescription: {description}. Simply add the new title and description right after Title and Description, don't add a new line or markdown."}
            ]
        )
        # Extracting content and ensuring it's treated as plain text
        generated_text = response['choices'][0]['message']['content'].strip()
        # Optionally remove Markdown or other formatting if still present
        plain_text = generated_text.replace('#', '').replace('*', '')  # Simple example of Markdown removal
        return plain_text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to extract the title and description from generated text
def parse_recommendations(recommendations):
    lines = recommendations.split('\n')
    for l in lines:
        if l.startswith('Title'):
            new_title = l.replace('Title:', '').strip()
        elif l.startswith('Description'):
            new_description = l.replace('Description:', '').strip()
    
    return new_title, new_description

# Function to give the ability to the user of copying text to their clipboard
def on_copy_click(text, label):
    st.session_state.copied.append((label, text))
    clipboard.copy(text)

if "copied" not in st.session_state: 
    st.session_state.copied = []

# Some streamlit visual configuration
st.set_page_config(
    page_title="Amazon Product Optimization Tool",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/solsylph/TheCompany'
        , 'Report a bug': "https://github.com/solsylph/TheCompany/issues"
        , 'About': "This is a Streamlit app using GPT-3.5-Turbo to optimize Amazon product titles and descriptions. Made by: [11acc](https://github.com/11acc), [sarwari-mallela](https://github.com/sarwari-mallela), [cheblimarc4](https://github.com/cheblimarc4), and [solsylph](https://github.com/solsylph) \ [GitHub Repo](https://github.com/solsylph/TheCompany)"
    }
)

# Streamlit interface and app logic
st.image("./assets/thecomp_trans.png", width=300)
st.title('Amazon Product Optimization Tool')
product_title = st.text_input('Product Title')
product_description = st.text_area('Product Description', height=200)

if st.button('Optimize'):
    if product_title and product_description:
        recommendations_raw = get_recommendations(product_title, product_description)
        print(recommendations_raw)
        new_title, new_description = parse_recommendations(recommendations_raw)
        print()
        print(new_title, new_description)

        # Better formatted output
        st.markdown("#### ✨ Generated Optimization ✨")
        st.markdown("__New Title:__")
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.markdown(f"{new_title}")
        with col2:
            st.button("📋", on_click=on_copy_click, args=(new_title, "Title"), key="copy_new_title")

        st.markdown("__New Description:__")
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.markdown(f"{new_description}")
        with col2:
            st.button("📋", on_click=on_copy_click, args=(new_description, "Description"), key="copy_new_description")

        for label, text in st.session_state.copied:
            st.toast(f"Copied {label}", icon='✅')
    else:
        st.error('Please enter both a title and a description.')