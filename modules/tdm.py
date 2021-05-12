import math


# function for creating term-document matrix
def form_tdm(all_words):
    """
    (list) -> list

    Form term-document matrix.
    :param all_words: matrix with words of each document.
    :return: term document matrix, with appearing of certain word in each document.
    """
    # create list for unique words from all the documents
    words = []
    # print(len(all_words))

    # define those unique words and fill list with them
    for lst in range(0, len(all_words)):
        for element in all_words[lst]:
            if element not in words:
                words.append(element)

    # crate an empty list for term document matrix
    term_document_matrix = [[] for x in range(len(words))]
    for word in range(len(words)):
        for lst in range(len(all_words)):
            term_document_matrix[word].append(all_words[lst].count(words[word]))

    return words, term_document_matrix


def tf_idf_modification(term_document_matrix):
    """
    (list) -> list
    Function that applies TF-IDF on the document term matrix.
    :param term_document_matrix: matrix with the terms amounts in each document
    :return: document term matrix modified with TF-IDF
    """
    # defining the amount of documents and terms
    amount_of_documents = len(term_document_matrix[0])
    amount_of_terms = len(term_document_matrix)

    # initialising matrix for saving images of tf-idf applying
    term_document_matrix_with_tf_idf = [[0] * amount_of_documents for _ in range(amount_of_terms)]

    # applying tf-idf for every term
    for i in range(0, amount_of_terms):
        for j in range(0, amount_of_documents):

            # computing tf
            # tf = (number of times term appears in a document) divide by
            # (total number of terms in the document)

            term_amount_in_document = term_document_matrix[i][j]
            terms_amount_in_document = 0
            for k in range(0, amount_of_terms):
                terms_amount_in_document += term_document_matrix[k][j]

            tf = term_amount_in_document / terms_amount_in_document

            # computing idf
            # idf = log((total number of documents) divide by
            # (number of documents with a certain term in it))

            # finding the number of documents with the certain term in it
            documents_with_term = 0
            for m in range(0, amount_of_documents):
                if term_document_matrix[i][m] != 0:
                    documents_with_term += 1

            idf = math.log(amount_of_documents / documents_with_term)

            # getting tf-idf by tf * idf
            term_document_matrix_with_tf_idf[i][j] = round(tf * idf, 3)

    return term_document_matrix_with_tf_idf