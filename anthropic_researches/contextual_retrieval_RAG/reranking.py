import json
from collections.abc import Callable
from typing import Any

import cohere
from tqdm import tqdm


def evaluate_db_rerank(
    db, original_jsonl_path: str, k_values: list[int] = None, db_name: str = "Reranking"
):
    """
    Evaluate reranking performance at multiple k values with formatted results.

    Args:
        db: ContextualVectorDB instance
        original_jsonl_path: Path to evaluation dataset
        k_values: List of k values to evaluate (default: [5, 10, 20])
        db_name: Name for the evaluation display

    Returns:
        Dict mapping k values to their results
    """
    if k_values is None:
        k_values = [5, 10, 20]
    original_data = load_jsonl(original_jsonl_path)
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    results = {}

    print(f"{'=' * 60}")
    print(f"Evaluation Results: {db_name}")
    print(f"{'=' * 60}\n")

    for k in k_values:
        print(f"Evaluating Pass@{k} with reranking...")

        total_score = 0
        total_queries = len(original_data)

        for query_item in tqdm(original_data, desc=f"Pass@{k}"):
            query = query_item["query"]
            golden_chunk_uuids = query_item["golden_chunk_uuids"]

            # Find golden contents
            golden_contents = []
            for doc_uuid, chunk_index in golden_chunk_uuids:
                golden_doc = next(
                    (doc for doc in query_item["golden_documents"] if doc["uuid"] == doc_uuid), None
                )
                if golden_doc:
                    golden_chunk = next(
                        (chunk for chunk in golden_doc["chunks"] if chunk["index"] == chunk_index),
                        None,
                    )
                    if golden_chunk:
                        golden_contents.append(golden_chunk["content"].strip())

            if not golden_contents:
                continue

            # Retrieve and rerank
            semantic_results = db.search(query, k=k * 10)

            # Prepare documents for reranking
            documents = [
                f"{res['metadata']['original_content']}\n\nContext: {res['metadata']['contextualized_content']}"
                for res in semantic_results
            ]

            # Rerank
            rerank_response = co.rerank(
                model="rerank-english-v3.0", query=query, documents=documents, top_n=k
            )
            time.sleep(0.1)  # Rate limiting

            # Get final results
            retrieved_docs = []
            for r in rerank_response.results:
                original_result = semantic_results[r.index]
                retrieved_docs.append(
                    {"chunk": original_result["metadata"], "score": r.relevance_score}
                )

            # Check if golden chunks are in results
            chunks_found = 0
            for golden_content in golden_contents:
                for doc in retrieved_docs[:k]:
                    retrieved_content = doc["chunk"]["original_content"].strip()
                    if retrieved_content == golden_content:
                        chunks_found += 1
                        break

            query_score = chunks_found / len(golden_contents)
            total_score += query_score

        average_score = total_score / total_queries
        pass_at_n = average_score * 100

        results[k] = {
            "pass_at_n": pass_at_n,
            "average_score": average_score,
            "total_queries": total_queries,
        }

        print(f"Pass@{k}: {pass_at_n:.2f}%")
        print(f"Average Score: {average_score:.4f}\n")

    # Print summary table
    print(f"{'=' * 60}")
    print(f"{'Metric':<15} {'Pass Rate':<15} {'Score':<15}")
    print(f"{'-' * 60}")
    for k in k_values:
        pass_rate = f"{results[k]['pass_at_n']:.2f}%"
        score = f"{results[k]['average_score']:.4f}"
        print(f"{'Pass@' + str(k):<15} {pass_rate:<15} {score:<15}")
    print(f"{'=' * 60}\n")

    return results