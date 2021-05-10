from modules.svd import apply_svd_basic


def define_key_words(data, all_unique_words):
    u, s, vh = apply_svd_basic(data)

    # creating empty list topics, in which each list will correspond
    # to certain topic. And values in these lists will be coefficients of connection
    # of each word with this topic
    # (So we will have now 10 lists (10 topics) with 511 values in each (terms))

    topics = [[] for _ in range(len(u[0]))]
    for word_index, word_coef_list in enumerate(u):
        for i in range(len(word_coef_list)):
            topics[i].append(word_coef_list[i])

    for lst in range(len(topics)):
        for val in range(len(topics[lst])):
            topics[lst][val] = abs(topics[lst][val])

    words = [[] for x in range(len(topics))]

    for topic in range(len(topics)):
        max_coef = max(topics[topic])
        max_coef_index = topics[topic].index(max_coef)
        key_words = [all_unique_words[max_coef_index]]

        second_max_coef = 0
        second_max_coef_index = 0
        for j in range(len(topics[topic])):
            if topics[topic][j] > second_max_coef\
                    and all_unique_words[j] not in key_words:
                second_max_coef = topics[topic][j]
                second_max_coef_index = j
        key_words.append(all_unique_words[second_max_coef_index])

        third_max_coef = 0
        third_max_coef_index = 0
        for k in range(len(topics[topic])):
            if topics[topic][k] > third_max_coef \
                    and all_unique_words[k] not in key_words:
                third_max_coef = topics[topic][k]
                third_max_coef_index = k
        key_words.append(all_unique_words[third_max_coef_index])

        fourth_max_coef = 0
        fourth_max_coef_index = 0
        for k in range(len(topics[topic])):
            if topics[topic][k] > fourth_max_coef \
                    and all_unique_words[k] not in key_words:
                fourth_max_coef = topics[topic][k]
                fourth_max_coef_index = k
        key_words.append(all_unique_words[fourth_max_coef_index])

        fifth_max_coef = 0
        fifth_max_coef_index = 0
        for k in range(len(topics[topic])):
            if topics[topic][k] > fifth_max_coef \
                    and all_unique_words[k] not in key_words:
                fifth_max_coef = topics[topic][k]
                fifth_max_coef_index = k
        key_words.append(all_unique_words[fifth_max_coef_index])

        words[topic] = [key_words[0],
                        key_words[1],
                        key_words[2],
                        key_words[3],
                        key_words[4]]
    return words