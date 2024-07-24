def get_similarity_score(tomato_1, tomato_2):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, tomato_1, tomato_2).ratio()