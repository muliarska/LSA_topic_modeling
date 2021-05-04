from sklearn.decomposition import TruncatedSVD


def apply_svd(data, docs, topics_numb):
    svd_model = TruncatedSVD(n_components=topics_numb, algorithm='randomized', n_iter=100, random_state=122)
    svd_model.fit(data)

    # print(len(svd_model.components_))

    for i, comp in enumerate(svd_model.components_):
        docs_comp = zip(docs, comp)
        sorted_docs = sorted(docs_comp, key=lambda x: x[1], reverse=True)[:7]
        temp_str = "Topic " + str(i) + ": "
        for t in sorted_docs:
            temp_str += t[0] + " "
        temp_str += "\n"
        print(temp_str)
