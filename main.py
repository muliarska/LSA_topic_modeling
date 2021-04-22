from process_data import process_data

filename = "mini_newsgroups.tar.gz"
extension = "r:gz"
all_words = process_data(filename, extension)
# print(all_words[:10])

# поки для швидшого виконання обрізала дані
all_words = all_words[:10]

constructed_dtm = form_dtm(all_words)
print(constructed_dtm)
