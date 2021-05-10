from modules.tdm import form_tdm, tf_idf_modification
from modules.process_data import process_data
from modules.svd import classify_into_topics
from modules.topic_classification import define_key_words

filename = "../data/mini_newsgroups_to_test.tar.gz"
# filename = "../data/my_data.tar.gz"
extension = "r:gz"
all_words, file_names = process_data(filename, extension)
print("read")
# поки для швидшого виконання обрізала дані
all_words = all_words

# constructing document term matrix
unique_words, constructed_tdm = form_tdm(all_words)
print("form tdm")
# applying tf_idf algorithm
modified_tdm = tf_idf_modification(constructed_tdm)

topics = classify_into_topics(modified_tdm, file_names)
print("form tfidf")

print(topics)

# print results of classifying
for i in topics:
    print("Topic ", i, topics[i])

words = define_key_words(modified_tdm, unique_words)
print(words)
