from classifier.gemma import classify_into_syllabus_g
from classifier.llama import classify_into_syllabus_l
from classifier.consensus import topics_list


def topics(content: str) -> list[str]:
    gemma_op = classify_into_syllabus_g(content)
    llama_op = classify_into_syllabus_l(content)
    if not llama_op and gemma_op:
        return gemma_op
    if llama_op and not gemma_op:
        return llama_op

    return topics_list(llama_op, gemma_op)

   
