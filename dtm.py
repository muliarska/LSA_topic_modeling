def form_dtm(all_words):
    # create list for unique words from all the documents
    words = []

    # define those unique words and fill list with them
    for lst in range(0, len(all_words)):
        for element in all_words[lst]:
            if element not in words:
                words.append(element)

    # create empty matrix, where the first row
    # corresponds to all given words
    document_term_matrix = [[] for x in range(len(all_words)+1)]
    document_term_matrix[0] = words

    # calculate how many times each word appears
    # in each document and fill other lists with the results
    for lst in range(len(all_words)):
        for word in words:
            document_term_matrix[lst + 1].append(all_words[lst].count(word))

    # на виході ми маємо щось таке:
    # [['apple', 'banana', 'peach', 'grape'],
    # [0, 2, 1, 2],
    # [1, 1, 0, 0],
    # [3, 0, 0, 2]]
    # .....

    return document_term_matrix
