import json
import os
from typing import Any

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from tqdm import tqdm


class ElasticsearchBM25:
    def __init__(self, index_name: str = "contextual_bm25_index"):
        self.es_client = Elasticsearch("http://localhost:9200")
        self.index_name = index_name
        self.create_index()

    def create_index(self):
        index_settings = {
            "settings": {
                "analysis": {"analyzer": {"default": {"type": "english"}}},
                "similarity": {"default": {"type": "BM25"}},
                "index.queries.cache.enabled": False,
            },
            "mappings": {
                "properties": {
                    "content": {"type": "text", "analyzer": "english"},
                    "contextualized_content": {"type": "text", "analyzer": "english"},
                    "doc_id": {"type": "keyword", "index": False},
                    "chunk_id": {"type": "keyword", "index": False},
                    "original_index": {"type": "integer", "index": False},
                }
            },
        }

        # Change this line - remove 'body=' parameter
        if not self.es_client.indices.exists(index=self.index_name):
            self.es_client.indices.create(
                index=self.index_name,
                settings=index_settings["settings"],
                mappings=index_settings["mappings"],
            )
            print(f"Created index: {self.index_name}")

    def index_documents(self, documents: list[dict[str, Any]]):
        actions = [
            {
                "_index": self.index_name,
                "_source": {
                    "content": doc["original_content"],
                    "contextualized_content": doc["contextualized_content"],
                    "doc_id": doc["doc_id"],
                    "chunk_id": doc["chunk_id"],
                    "original_index": doc["original_index"],
                },
            }
            for doc in documents
        ]
        success, _ = bulk(self.es_client, actions)
        self.es_client.indices.refresh(index=self.index_name)
        return success

    def search(self, query: str, k: int = 20) -> list[dict[str, Any]]:
        self.es_client.indices.refresh(index=self.index_name)

        # Change this - remove 'body=' and pass query directly
        response = self.es_client.search(
            index=self.index_name,
            query={
                "multi_match": {
                    "query": query,
                    "fields": ["content", "contextualized_content"],
                }
            },
            size=k,
        )

        return [
            {
                "doc_id": hit["_source"]["doc_id"],
                "original_index": hit["_source"]["original_index"],
                "content": hit["_source"]["content"],
                "contextualized_content": hit["_source"]["contextualized_content"],
                "score": hit["_score"],
            }
            for hit in response["hits"]["hits"]
        ]


def create_elasticsearch_bm25_index(db: ContextualVectorDB):
    es_bm25 = ElasticsearchBM25()
    es_bm25.index_documents(db.metadata)
    return es_bm25


def retrieve_advanced(
    query: str,
    db: ContextualVectorDB,
    es_bm25: ElasticsearchBM25,
    k: int,
    semantic_weight: float = 0.8,
    bm25_weight: float = 0.2,
):
    num_chunks_to_recall = 150

    # Semantic search
    semantic_results = db.search(query, k=num_chunks_to_recall)
    ranked_chunk_ids = [
        (result["metadata"]["doc_id"], result["metadata"]["original_index"])
        for result in semantic_results
    ]

    # BM25 search using Elasticsearch
    bm25_results = es_bm25.search(query, k=num_chunks_to_recall)
    ranked_bm25_chunk_ids = [
        (result["doc_id"], result["original_index"]) for result in bm25_results
    ]

    # Combine results
    chunk_ids = list(set(ranked_chunk_ids + ranked_bm25_chunk_ids))
    chunk_id_to_score = {}

    # Initial scoring with weights
    for chunk_id in chunk_ids:
        score = 0
        if chunk_id in ranked_chunk_ids:
            index = ranked_chunk_ids.index(chunk_id)
            score += semantic_weight * (1 / (index + 1))  # Weighted 1/n scoring for semantic
        if chunk_id in ranked_bm25_chunk_ids:
            index = ranked_bm25_chunk_ids.index(chunk_id)
            score += bm25_weight * (1 / (index + 1))  # Weighted 1/n scoring for BM25
        chunk_id_to_score[chunk_id] = score

    # Sort chunk IDs by their scores in descending order
    sorted_chunk_ids = sorted(
        chunk_id_to_score.keys(), key=lambda x: (chunk_id_to_score[x], x[0], x[1]), reverse=True
    )

    # Assign new scores based on the sorted order
    for index, chunk_id in enumerate(sorted_chunk_ids):
        chunk_id_to_score[chunk_id] = 1 / (index + 1)

    # Prepare the final results
    final_results = []
    semantic_count = 0
    bm25_count = 0
    for chunk_id in sorted_chunk_ids[:k]:
        chunk_metadata = next(
            chunk
            for chunk in db.metadata
            if chunk["doc_id"] == chunk_id[0] and chunk["original_index"] == chunk_id[1]
        )
        is_from_semantic = chunk_id in ranked_chunk_ids
        is_from_bm25 = chunk_id in ranked_bm25_chunk_ids
        final_results.append(
            {
                "chunk": chunk_metadata,
                "score": chunk_id_to_score[chunk_id],
                "from_semantic": is_from_semantic,
                "from_bm25": is_from_bm25,
            }
        )

        if is_from_semantic and not is_from_bm25:
            semantic_count += 1
        elif is_from_bm25 and not is_from_semantic:
            bm25_count += 1
        else:  # it's in both
            semantic_count += 0.5
            bm25_count += 0.5

    return final_results, semantic_count, bm25_count


def evaluate_db_advanced(
    db: ContextualVectorDB,
    original_jsonl_path: str,
    k_values: list[int] = None,
    db_name: str = "Hybrid Search",
):
    """
    Evaluate hybrid search (semantic + BM25) at multiple k values with formatted results.

    Args:
        db: ContextualVectorDB instance
        original_jsonl_path: Path to evaluation dataset
        k_values: List of k values to evaluate (default: [5, 10, 20])
        db_name: Name for the evaluation display

    Returns:
        Dict mapping k values to their results and source breakdowns
    """
    if k_values is None:
        k_values = [5, 10, 20]
    original_data = load_jsonl(original_jsonl_path)
    es_bm25 = create_elasticsearch_bm25_index(db)
    results = {}

    print(f"{'=' * 70}")
    print(f"Evaluation Results: {db_name}")
    print(f"{'=' * 70}\n")

    try:
        # Warm-up queries
        warm_up_queries = original_data[:10]
        for query_item in warm_up_queries:
            _ = retrieve_advanced(query_item["query"], db, es_bm25, k_values[0])

        for k in k_values:
            print(f"Evaluating Pass@{k}...")

            total_score = 0
            total_semantic_count = 0
            total_bm25_count = 0
            total_results = 0

            for query_item in tqdm(original_data, desc=f"Pass@{k}"):
                query = query_item["query"]
                golden_chunk_uuids = query_item["golden_chunk_uuids"]

                golden_contents = []
                for doc_uuid, chunk_index in golden_chunk_uuids:
                    golden_doc = next(
                        (doc for doc in query_item["golden_documents"] if doc["uuid"] == doc_uuid),
                        None,
                    )
                    if golden_doc:
                        golden_chunk = next(
                            (
                                chunk
                                for chunk in golden_doc["chunks"]
                                if chunk["index"] == chunk_index
                            ),
                            None,
                        )
                        if golden_chunk:
                            golden_contents.append(golden_chunk["content"].strip())

                if not golden_contents:
                    continue

                retrieved_docs, semantic_count, bm25_count = retrieve_advanced(
                    query, db, es_bm25, k
                )

                chunks_found = 0
                for golden_content in golden_contents:
                    for doc in retrieved_docs[:k]:
                        retrieved_content = doc["chunk"]["original_content"].strip()
                        if retrieved_content == golden_content:
                            chunks_found += 1
                            break

                query_score = chunks_found / len(golden_contents)
                total_score += query_score

                total_semantic_count += semantic_count
                total_bm25_count += bm25_count
                total_results += len(retrieved_docs)

            total_queries = len(original_data)
            average_score = total_score / total_queries
            pass_at_n = average_score * 100

            semantic_percentage = (
                (total_semantic_count / total_results) * 100 if total_results > 0 else 0
            )
            bm25_percentage = (total_bm25_count / total_results) * 100 if total_results > 0 else 0

            results[k] = {
                "pass_at_n": pass_at_n,
                "average_score": average_score,
                "total_queries": total_queries,
                "semantic_percentage": semantic_percentage,
                "bm25_percentage": bm25_percentage,
            }

            print(f"Pass@{k}: {pass_at_n:.2f}%")
            print(f"Semantic: {semantic_percentage:.1f}% | BM25: {bm25_percentage:.1f}%\n")

        # Print summary table
        print(f"{'=' * 70}")
        print(f"{'Metric':<12} {'Pass Rate':<12} {'Score':<12} {'Semantic':<12} {'BM25':<12}")
        print(f"{'-' * 70}")
        for k in k_values:
            r = results[k]
            print(
                f"{'Pass@' + str(k):<12} {r['pass_at_n']:>10.2f}% {r['average_score']:>10.4f} "
                f"{r['semantic_percentage']:>10.1f}% {r['bm25_percentage']:>10.1f}%"
            )
        print(f"{'=' * 70}\n")

        return results

    finally:
        # Delete the Elasticsearch index
        if es_bm25.es_client.indices.exists(index=es_bm25.index_name):
            es_bm25.es_client.indices.delete(index=es_bm25.index_name)
            print(f"Deleted Elasticsearch index: {es_bm25.index_name}")