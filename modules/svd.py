from sklearn.decomposition import TruncatedSVD


def apply_svd(data):
    svd_model = TruncatedSVD(n_components=20, algorithm='randomized', n_iter=100, random_state=122)
    terms = data[0]
    svd_model.fit(data[1:])

    # print(len(svd_model.components_))

    for i, comp in enumerate(svd_model.components_):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:7]
        temp_str = "Topic " + str(i) + ": "
        for t in sorted_terms:
            temp_str += t[0] + " "
        temp_str += "\n"
        print(temp_str)
