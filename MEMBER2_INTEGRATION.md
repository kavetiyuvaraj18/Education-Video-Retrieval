# Member 2 Recommendation Module Integration

## Purpose

Member 2's recommendation module will replace the temporary
recommendation logic currently used by the Flask application.

The module will receive:

1. Student query
2. Candidate YouTube videos

It will return:

1. Ranked Top-K videos
2. Relevance score for each video
3. Relevant timestamp for each video

---

## Current Member 1 Interface

File:

```text
recommendation_interface.py