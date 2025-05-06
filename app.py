import streamlit as st
import pandas as pd
import plotly.express as px
import openai
import os
from dotenv import load_dotenv
from openai import OpenAI
import io
import contextlib
import ast

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI config
st.set_page_config(page_title="InsightGPT", layout="wide")
st.title("📊 InsightGPT – Executive Dashboard Copilot")

# File upload
uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])
df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Data Summary")
    st.write(df.describe())

    st.subheader("📋 Column Names")
    st.write(df.columns.tolist())

    # User query
    st.subheader("🧠 Ask a question about your data")
    user_query = st.text_input("Enter your question here:", placeholder="e.g. Show total sales by region")

    if user_query:
        context = f"The dataset has the following columns: {', '.join(df.columns)}."
        prompt = f"""
You are a smart data assistant. The dataset is already loaded in a DataFrame named df.

{context}

Instructions:
- If the user explicitly asks for a chart, graph, or visualization, return Python code using pandas and plotly, ending with st.plotly_chart(fig).
- If the user asks for a table, top-N results, sorted values, or anything requiring a dataframe, return Python code that ends with st.dataframe(...).
- For all other general, interpretive, or insight-based questions, respond with plain English wrapped in st.markdown(...).

Only return the relevant code or text (no triple backticks, no imports).

User query: {user_query}
"""

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        answer = response.choices[0].message.content.strip()

        # Remove markdown code fences if present
        if answer.startswith("```"):
            answer = '\n'.join(line for line in answer.splitlines() if not line.strip().startswith('```'))

        # Determine if response is Python code
        def is_python_code(text):
            try:
                ast.parse(text)
                return True
            except:
                return False

        if is_python_code(answer):
            st.subheader("🤖 GPT-Generated Code")
            st.code(answer, language='python')

            st.subheader("📊 Output")
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(answer, globals())
            except Exception as e:
                st.error(f"⚠️ Error executing generated code: {e}")

            st.subheader("🛠️ Edit or Fix the Code Below")
            editable_code = st.text_area("Edit the generated code if needed:", value=answer, height=300)
            if st.button("▶️ Run Edited Code"):
                st.subheader("📊 Output of Your Edited Code")
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        exec(editable_code, globals())
                except Exception as e:
                    st.error(f"⚠️ Error executing your edited code: {e}")
        else:
            st.subheader("📝 GPT Insights")
            st.markdown(answer)

else:
    st.info("👈 Upload a CSV file to get started.")
