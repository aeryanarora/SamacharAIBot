from classifier.map import TOPIC_TO_GS_MAP


def strict_agreement(output1: list[str], output2: list[str]) -> dict:
    set1 = set(output1)
    set2 = set(output2)
    result = list(set1 & set2)
    return result
def map_to_gs(topics: list[str]) -> dict:
    ans = {"GS1": [], "GS2": [], "GS3": []}
    for topic in topics:
        paper = TOPIC_TO_GS_MAP.get(topic)
        if paper:
            ans[f"{paper}"].append(topic)
    return ans

def topics_list(llama_output: list[str], gemma_output: list[str]) -> list[str]:
    agreed = strict_agreement(llama_output, gemma_output)
    final_topics = agreed if len(agreed)!=0 else llama_output   
    return list(final_topics)
