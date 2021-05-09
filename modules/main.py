from modules.tdm import form_tdm, tf_idf_modification
from modules.process_data import process_data
from modules.svd_basic import apply_svd_basic, classify_into_topics
from modules.svd import apply_svd

# filename = "../data/mini_newsgroups.tar.gz"
filename = "../data/my_data.tar.gz"
extension = "r:gz"
all_words, file_names = process_data(filename, extension)
# print(all_words[:10])


# поки для швидшого виконання обрізала дані
all_words = all_words

# constructing document term matrix
unique_words, constructed_tdm = form_tdm(all_words)

# applying tf_idf algorithm
modified_tdm = tf_idf_modification(constructed_tdm)

topics = classify_into_topics(modified_tdm, file_names)

# print results of classifying
for i in topics:
    print("Topic ", i, topics[i])
