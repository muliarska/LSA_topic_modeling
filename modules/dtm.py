import math


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


def tf_idf_modification(document_term_matrix):
    # defining the amount of documents and terms
    amount_of_documents = len(document_term_matrix)
    amount_of_terms = len(document_term_matrix[0])

    # initialising matrix for saving results of tfidf applying
    document_term_matrix_with_tf_idf = [[0] * amount_of_terms for _ in range(len(document_term_matrix))]
    document_term_matrix_with_tf_idf[0] = document_term_matrix[0]

    # applying tfidf for every term
    for i in range(1, amount_of_documents):
        for j in range(0, amount_of_terms):

            # computing tf
            # tf = (number of times term appears in a document) divide by
            # (total number of terms in the document)

            term_amount = document_term_matrix[i][j]
            document_terms_amount = sum(document_term_matrix[i])

            tf = term_amount / document_terms_amount

            # computing idf
            # idf = log((total number of documents) divide by
            # (number of documents with a certain term in it))

            # finding the number of documents with the certain term in it
            documents_with_term = 0
            for k in range(1, amount_of_documents):
                if document_term_matrix[k][j] != 0:
                    documents_with_term += 1

            idf = math.log(amount_of_documents / documents_with_term)

            # getting tfidf by tf * idf
            document_term_matrix_with_tf_idf[i][j] = tf * idf

    return document_term_matrix_with_tf_idf
