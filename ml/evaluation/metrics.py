import math


def precision_at_k(relevant_items, retrieved_items, k):
    retrieved = retrieved_items[:k]

    if not retrieved:
        return 0.0

    relevant_count = sum(
        1 for item in retrieved
        if item in relevant_items
    )

    return relevant_count / len(retrieved)


def recall_at_k(relevant_items, retrieved_items, k):
    if not relevant_items:
        return 0.0

    retrieved = retrieved_items[:k]

    relevant_count = sum(
        1 for item in retrieved
        if item in relevant_items
    )

    return relevant_count / len(relevant_items)


def ndcg_at_k(relevant_items, retrieved_items, k):
    retrieved = retrieved_items[:k]

    if not retrieved:
        return 0.0

    dcg = 0.0

    for position, item in enumerate(retrieved, start=1):
        if item in relevant_items:
            dcg += 1 / math.log2(position + 1)

    ideal_count = min(len(relevant_items), k)

    if ideal_count == 0:
        return 0.0

    idcg = sum(
        1 / math.log2(position + 1)
        for position in range(1, ideal_count + 1)
    )

    return dcg / idcg