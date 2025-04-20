import json
from classifier.config import get_data, get_prompt, url, headers
from classifier.api import api_call


def classify_into_syllabus_l(content: str) -> list[str]:
    prompt = get_prompt(content)
    data = get_data("llama-3.3-70b-versatile", prompt)
    result = api_call(url, headers, data)

    if isinstance(result, dict):
        if "Topics" in result:
            return list(result["Topics"])

        if "error" in result and "429" in result["error"]:
            return []

        if "raw_output" in result:
            try:
                cleaned = result["raw_output"].replace("\n", "\\n")
                parsed = json.loads(cleaned)
                return list(parsed.get("Topics", []))
            except:
                return []

    return []
