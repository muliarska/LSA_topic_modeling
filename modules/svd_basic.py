import numpy as np


def apply_svd_basic(data):

    # Shapes of matrices:

    # u - matrix 511 x 10
    # s - diagonal 10 x 10
    # vh - matrix 10 x 10

    return np.linalg.svd(data, full_matrices=False)


def classify_into_topics(data, filenames):
    u, s, vh = apply_svd_basic(data)

    topics = dict()

    for list_index, doc_coeff_list in enumerate(vh):
        if abs(max(doc_coeff_list)) > abs(min(doc_coeff_list)):
            max_coef = max(doc_coeff_list)
        else:
            max_coef = min(doc_coeff_list)

        topic_index = np.where(doc_coeff_list == max_coef)[0][0]

        if topic_index not in topics:
            topics[topic_index] = []

        topics[topic_index].append(filenames[list_index])

    return topics
