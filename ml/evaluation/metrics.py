def precision_at_k(relevant_items, retrieved_items, k):
    """
    Calculate Precision@K.
    """

    retrieved = retrieved_items[:k]

    if not retrieved:
        return 0.0

    relevant_count = sum(
        1 for item in retrieved
        if item in relevant_items
    )

    return relevant_count / len(retrieved)


def recall_at_k(relevant_items, retrieved_items, k):
    """
    Calculate Recall@K.
    """

    if not relevant_items:
        return 0.0

    retrieved = retrieved_items[:k]

    relevant_count = sum(
        1 for item in retrieved
        if item in relevant_items
    )

    return relevant_count / len(relevant_items)