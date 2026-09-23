from ml.evaluation.metrics import (
    precision_at_k,
    recall_at_k,
    ndcg_at_k
)


relevant_items = [
    "python",
    "machine_learning"
]

retrieved_items = [
    "python",
    "programming",
    "machine_learning",
    "web_development",
    "data_science"
]

k = 5

precision = precision_at_k(
    relevant_items,
    retrieved_items,
    k
)

recall = recall_at_k(
    relevant_items,
    retrieved_items,
    k
)

ndcg = ndcg_at_k(
    relevant_items,
    retrieved_items,
    k
)


print("Evaluation Results")
print("-------------------")
print("Precision@5:", precision)
print("Recall@5:", recall)
print("NDCG@5:", ndcg)