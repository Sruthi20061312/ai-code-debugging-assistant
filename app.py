import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Code Debugger", layout="wide")
st.title("🚀 AI Code Debugging Assistant")

language = st.selectbox("Select Language", ["Python", "SQL"])
code_input = st.text_area("Paste your code here:", height=300)

if st.button("Analyze Code"):

    prompt = f"""
    You are an expert {language} developer.
    Analyze the following code:
    1. Detect errors
    2. Fix the code
    3. Explain the mistake
    4. Suggest optimization
    
    Code:
    {code_input}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("AI Response:")
    st.markdown(response.choices[0].message.content)
st.success("Analysis complete.")
show_explanation = st.checkbox("Show Explanation")
show_optimization = st.checkbox("Show Optimization Suggestions")
