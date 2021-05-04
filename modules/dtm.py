import math


# function for creating term-document matrix
def form_tdm(all_words):
    '''
    (list) -> list
    
    Form term-document matrix.
    :param all_words: matrix with words of each document.
    :return: term document matrix, with appearing of certain word in each document.
    '''
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
    
    return term_document_matrix


def tf_idf_modification(document_term_matrix):
    """
    (list) -> list

    Function that applies TFIDF on the document term matrix.

    :param document_term_matrix: matrix with the terms amounts in each document
    :return: document term matrix modified with TFIDF
    """
    # defining the amount of documents and terms
    amount_of_documents = len(document_term_matrix) - 1
    amount_of_terms = len(document_term_matrix[0])

    # initialising matrix for saving results of tfidf applying
    document_term_matrix_with_tf_idf = [[0] * amount_of_terms for _ in range(len(document_term_matrix))]
    document_term_matrix_with_tf_idf[0] = document_term_matrix[0]

    # applying tfidf for every term
    for i in range(1, amount_of_documents + 1):
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
            for k in range(1, amount_of_documents + 1):
                if document_term_matrix[k][j] != 0:
                    documents_with_term += 1

            idf = math.log(amount_of_documents / documents_with_term)

            # getting tfidf by tf * idf
            document_term_matrix_with_tf_idf[i][j] = round(tf * idf, 3)

    return document_term_matrix_with_tf_idf
