from modules.dtm import form_dtm, tf_idf_modification
from modules.process_data import process_data

filename = "../data/mini_newsgroups.tar.gz"
extension = "r:gz"
all_words = process_data(filename, extension)
# print(all_words[:10])

# поки для швидшого виконання обрізала дані
all_words = all_words[:10]

# constructing document term matrix
constructed_dtm = form_dtm(all_words)

# applying tf_idf algorithm
modified_dtm = tf_idf_modification(constructed_dtm)

print(constructed_dtm)
print(modified_dtm)
