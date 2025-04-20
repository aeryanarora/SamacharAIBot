import re
import json
from classifier.api import api_call
from classifier.config import get_data, url, headers


def get_qa_prompt(text: str, topics: list[str], gs_paper: str) -> str:
    topics_str = ', '.join(topics)
    return f"""
    You are a UPSC Mains answer generation assistant.

    Given an article and its associated GS paper and topics, generate:
    1. One UPSC-style General Studies Mains question.
    2. A model answer with clear structure:
    - Introduction
    - Main Body (in bullet or paragraph form)
    - Conclusion

    Use only the content below. Keep answer around 300 words.

    Return only a valid JSON object in the following format — do not include explanation or markdown outside of the JSON. Use \\n to escape newlines inside the values.

    GS Paper: {gs_paper}
    Topics: {topics_str}

    Article:
    \"\"\"
    {text}
    \"\"\"

    Format:
    {{
    "Question": "...",
    "Answer": "..."
    }}
    """


def generate_qa(text: str, topics: list[str], gs_paper: str, model="llama-3.3-70b-versatile") -> dict:
    prompt = get_qa_prompt(text, topics, gs_paper)
    data = get_data(model, prompt, temperature=0.3)
    result = api_call(url, headers, data)

    if isinstance(result, dict) and "Question" in result:
        return result

    if isinstance(result, dict) and "error" in result:
        if "429" in result["error"]:
            return generate_qa(text, topics, gs_paper, model="gemma2-9b-it")

    if isinstance(result, dict) and "raw_output" in result:
        try:
            cleaned = result["raw_output"].replace("\n", "\\n")
            parsed = json.loads(cleaned)
            if "Question" in parsed:
                return parsed
        except:
            pass

    return {"error": "QnA generation failed", "raw": result}


def generate_qa_for_all_papers(text: str, gs_map: dict) -> dict:
    qa_results = {}
    for gs_paper, topics in gs_map.items():
        if topics:
            qa = generate_qa(text, topics, gs_paper)
            qa_results[gs_paper] = qa
    return qa_results


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return text
    text = re.sub(r'[*_`]', '', text)
    text = text.replace('\\n', '\n')
    return text.strip()


def format_qa_markdown(qa_dict: dict, gs_paper: str) -> str:
    if "Question" not in qa_dict or "Answer" not in qa_dict:
        return "Could not generate question and answer."

    question = clean_text(qa_dict["Question"])
    answer = qa_dict["Answer"]

    if isinstance(answer, dict):
        parts = []
        for section, content in answer.items():
            if isinstance(content, list):
                section_text = f"{section}:\n" + "\n".join(f"- {clean_text(item)}" for item in content)
            else:
                section_text = f"{section}:\n{clean_text(content)}"
            parts.append(section_text)
        answer = "\n\n".join(parts)
    else:
        answer = clean_text(answer)

    return f"""{gs_paper}

Question:
{question}

Answer:
{answer}
"""

