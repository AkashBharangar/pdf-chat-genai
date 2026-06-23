from groq import Groq

client = Groq()


def retrieve_relevant_chunks(query, chunks, tok_k=3):
    query_words = set(query.lower().split())

    scored_chunks = []

    for chunk in chunks:
        chunked_words = set(chunk.lower().split())
        score = len(query_words.intersection(chunked_words))
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key= lambda x:x[0])

    return [chunk for score, chunk in scored_chunks[:tok_k]]


def get_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""You are a ai assistant
    Read the context to give answer to the query
    Only give answer in brief and NOT large answers
    
    Context:
    {context}
    
    query:
    {query}
    """

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content