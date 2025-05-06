📊 InsightGPT – Executive Dashboard Copilot
InsightGPT is a Streamlit-powered web app that allows users to upload CSV datasets and ask natural language questions about their data. It uses OpenAI's GPT model to intelligently generate Python code for visualizations, summaries, and tabular insights — all rendered dynamically.

🚀 Features
🔄 Upload your own CSV dataset
💬 Ask questions like “Show top 10 customers by sales” or “Which region had the highest profit?”
🧠 GPT-generated Python code using OpenAI API

📊 Automatically renders:
Plotly visualizations (when asked)
Tabular outputs (when requested)
Plain English summaries (when no visuals are needed)
🛠️ Code editor for manual tweaks and re-execution
✅ Smart logic to choose between text, table, or chart output

📂 Folder Structure

insightgpt/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── .env.example           # API key example (replace in your local .env)

🔧 How to Run Locally
Clone the repo:
git clone https://github.com/yourusername/insightgpt.git
cd insightgpt
Install dependencies:
pip install -r requirements.txt
Create your .env file:
OPENAI_API_KEY=your_openai_key_here

Run the app:
streamlit run app.py

🌐 Deploy on Streamlit Cloud
Push this folder to a public GitHub repository
Go to streamlit.io/cloud
Connect your GitHub account
Deploy the repo and enter your OpenAI API key in Streamlit's Secrets Manager

✅ Example Prompts
“Show average discount per region as a bar chart”
“Top 5 customers by total profit”
“Explain which segment performs best overall”
“Create a pie chart of sales by category”
