from collections import Counter
from math import ceil
from classifier.classify import topics
from classifier.consensus import map_to_gs


def chunk_text(text: str, chunk_size: int = 1500, overlap: int = 250) -> list[str]:
    if len(text) < 2 * chunk_size:
        return [text]  #Chunk bypass for short articles

    chunks = []
    i = 0
    while i < len(text):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks


def classify_chunks(text: str, chunk_size: int = 1500) -> dict:
    chunks = chunk_text(text, chunk_size)
    tot = len(chunks)
    if tot == 0:
        return {}

    topic_counter = Counter()

    for chunk in chunks:
        result = topics(chunk)
        if not result:
            continue
        for topic in result:
            topic_counter[topic] += 1

    final_topics = [
        topic for topic, count in topic_counter.items()
        if count >= ceil(0.25 * tot)
    ]

    return map_to_gs(final_topics)



    
        



