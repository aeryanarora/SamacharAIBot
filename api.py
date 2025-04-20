import requests
import json

def api_call(url,headers,data):
    try:
        response = requests.post(url = url, headers=headers,json=data)
        response.raise_for_status()
        result = response.json()         
        raw_output = result["choices"][0]["message"]["content"]
        return json.loads(raw_output)

    except Exception as e:
        return {
                "error": str(e),
                "raw_output": raw_output if 'raw_output' in locals() else None
        }