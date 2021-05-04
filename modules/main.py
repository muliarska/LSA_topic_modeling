from modules.tdm import form_tdm, tf_idf_modification
from modules.process_data import process_data
from modules.svd import apply_svd

filename = "../data/mini_newsgroups.tar.gz"
extension = "r:gz"
all_words, file_names = process_data(filename, extension)
# print(all_words[:10])

print(file_names)
print(len(file_names))

# поки для швидшого виконання обрізала дані
all_words = all_words[:2]

# constructing document term matrix
constructed_tdm = form_tdm(all_words)

print(constructed_tdm)
# applying tf_idf algorithm
modified_tdm = tf_idf_modification(constructed_tdm)

print(modified_tdm)
#apply_svd(modified_tdm)
