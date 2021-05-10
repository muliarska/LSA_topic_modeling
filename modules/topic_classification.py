from modules.svd import apply_svd_basic


def define_key_words(data, all_unique_words):
    u, s, vh = apply_svd_basic(data)

    words = dict()

    # creating empty list topics, in which each list will correspond
    # to certain topic. And values in these lists will be coefficients of connection
    # of each word with this topic
    # (So we will have now 10 lists (10 topics) with 511 values in each (terms))

    topics = [[] for _ in range(len(u[0]))]
    for word_index, word_coef_list in enumerate(u):
        for i in range(len(word_coef_list)):
            topics[i].append(word_coef_list[i])

    for topic in range(len(topics)):
        max_coef = max(topics[topic])
        max_coef_index = topics[topic].index(max_coef)

        second_max_coef = 0
        second_max_coef_index = 0
        for j in range(len(topics[topic])):
            if topics[topic][j] > second_max_coef\
                    and topics[topic][j] != max_coef:
                second_max_coef = topics[topic][j]
                second_max_coef_index = j

        third_max_coef = 0
        third_max_coef_index = 0
        for k in range(len(topics[topic])):
            if topics[topic][k] > third_max_coef \
                    and topics[topic][k] != max_coef\
                    and topics[topic][k] != second_max_coef:
                third_max_coef = topics[topic][k]
                third_max_coef_index = k

        words[topic] = [all_unique_words[max_coef_index],
                        all_unique_words[second_max_coef_index],
                        all_unique_words[third_max_coef_index]]

    # print(words)
    return words