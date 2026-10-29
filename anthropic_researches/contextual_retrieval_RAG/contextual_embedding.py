DOCUMENT_CONTEXT_PROMPT = """
<document>
{doc_content}
</document>
"""

CHUNK_CONTEXT_PROMPT = """
Here is the chunk we want to situate within the whole document
<chunk>
{chunk_content}
</chunk>

Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
Answer only with the succinct context and nothing else.
"""


def situate_context(doc: str, chunk: str) -> str:
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        temperature=0.0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),\
                        # LESSON 2: cache te full document at the first prompt instead of sending it everytime you send a chunk
                        "cache_control": {
                            "type": "ephemeral"
                        },  # we will make use of prompt caching for the full documents
                    },
                    {
                        "type": "text",
                        "text": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
                    },
                ],
            }
        ],
    )
    return response


jsonl_data = load_jsonl("data/evaluation_set.jsonl")
# Example usage
doc_content = jsonl_data[0]["golden_documents"][0]["content"]
chunk_content = jsonl_data[0]["golden_chunks"][0]["content"]

response = situate_context(doc_content, chunk_content)
print(f"Situated context: {response.content[0].text}")
print("-" * 10)
# Print cache performance metrics
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Cache creation input tokens: {response.usage.cache_creation_input_tokens}")
print(f"Cache read input tokens: {response.usage.cache_read_input_tokens}")