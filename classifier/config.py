from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Content-Type" : "application/json" ,
    "Authorization": f"Bearer {key}"
}

def get_data(model_name,prompt, temperature = 0.25):
    return {
        "model": model_name, 
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }
def get_prompt(content):
    prompt =  f"""
    You are a classification assistant trained to map any news article, report, or content to relevant Topics from the official UPSC Civil Services Mains General Studies syllabus.

    Your goal is to:
    1. Understand the **full context** and **core themes** of the content.
    2. Assign only those Topics that are directly or reasonably **implied** by the content.
    3. Choose only from the official topic list provided below. You may infer the appropriate topic even if the exact keyword is not present — but ensure the inferred topic logically fits the meaning of the content. Do not create your own topic names outside this list.

    You may infer a topic even if the exact keyword is not mentioned — for example:
    - A rural electrification scheme may involve **Infrastructure** and **Governance**
    - A report on declining groundwater levels may relate to **Environment** and **Agriculture**
    - A speech on universal basic income may involve **Economy**, **Welfare Schemes**, and **Social Justice**

    If the article clearly connects to a mentioned topic, **you should tag it**, even if subtly or indirectly.

    Return only a valid JSON object using this format:
    Example :-
    {{ 
        "Topics": ["Polity", "Disaster Management", "Environment"]
    }}

    Use only the topics below:

    - Indian Society
    - Modern Indian History
    - World History
    - Geography
    - Globalization
    - Urbanization
    - Role of Women
    - Social Empowerment

    - Indian Constitution
    - Governance
    - Polity
    - Social Justice
    - Welfare Schemes
    - Parliament
    - Judiciary
    - International Relations
    - e-Governance

    - Economy
    - Agriculture
    - Science & Technology
    - Environment
    - Disaster Management
    - National Security
    - Cybersecurity
    - Infrastructure
    
    If a topic clearly applies based on the content’s goals, challenges, or beneficiaries — even without being named — include it.
    Here is the article:
    \"\"\"
    {content}
    \"\"\"

    Only return the JSON object. Do not include explanations or extra text.
    """


    return prompt


