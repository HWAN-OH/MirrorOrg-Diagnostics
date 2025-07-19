# conflict_calculator.py

import numpy as np

def cosine_distance(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    if norm_product == 0:
        return 1.0
    return 1 - np.dot(vec1, vec2) / norm_product
