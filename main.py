from process_data import process_data

filename = "mini_newsgroups.tar.gz"
extension = "r:gz"
all_words = process_data(filename, extension)
# print(all_words[:10])
