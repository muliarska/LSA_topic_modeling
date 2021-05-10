from modules.tdm import form_tdm, tf_idf_modification
from modules.process_data import process_data
from modules.svd import classify_into_topics
from modules.topic_classification import define_key_words

# знайти функцію яка визначає екстеншин
filename = "../data/mini_newsgroups_to_test.tar.gz"
extension = "r:gz"
all_words, file_names = process_data(filename, extension)


# constructing document term matrix
unique_words, constructed_tdm = form_tdm(all_words)

# applying tf_idf algorithm
modified_tdm = tf_idf_modification(constructed_tdm)

topics = classify_into_topics(modified_tdm, file_names)


words = define_key_words(modified_tdm, unique_words)

counter = 0
# print results of classifying
for i in topics:
    print("Topic ", counter, topics[i])
    print("Words: ", words[i])
    print("\n")
    counter += 1
