import tarfile
from zipfile import ZipFile
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def clean_data(content, all_words):
    """

    Cleaning the data.

    :param content: file to clean
    :param all_words: data in the file to clean
    :return: cleaned data
    """
    stop_words = set(stopwords.words('english'))

    # split data into tokens
    tokens = word_tokenize(content)
    # filter out tokens that are not alphabetic
    words = [x for x in tokens if x.isalpha()]
    # remove stop words
    words = [x for x in words if x not in stop_words]
    # convert to lowercase
    words = [x.lower() for x in words]

    w = 0
    while w < len(words):
        if len(words[w]) <= 2:
            words.pop(w)
            w -= 1
        w += 1

    all_words.append(words)


def process_data(filename, extension):
    """

    Reading the data and getting all the words from documents.

    :param filename: name of the file to read
    :param extension: extension of the file
    :return: words from the files, names of the files
    """
    all_words = []
    count_pop = 0
    file_names = ""

    if extension == "r:gz":
        tar = tarfile.open(filename, extension)
        file_names = tar.getnames()

        for member_index, member in enumerate(tar.getmembers()):
            file = tar.extractfile(member)
            if file is not None:
                # read content of file as string
                content = str(file.read())
                clean_data(content, all_words)
            else:
                file_names.pop(member_index-count_pop)
                count_pop += 1

    elif extension == "zip":
        z = ZipFile(filename, "r")
        file_names = z.namelist()

        for file_index, filename in enumerate(z.namelist()):
            if filename.endswith(".txt"):
                print(filename)
                content = str(z.read(filename))
                clean_data(content, all_words)
            else:
                file_names.pop(file_index-count_pop)
                count_pop += 1

    return all_words, file_names
