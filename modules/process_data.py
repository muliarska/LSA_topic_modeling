import tarfile
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def process_data(filename, extension):
    stop_words = set(stopwords.words('english'))
    tar = tarfile.open(filename, extension)

    file_names = tar.getnames()

    all_words = []
    count_pop = 0

    for member_index, member in enumerate(tar.getmembers()):
        file = tar.extractfile(member)
        if file is not None:
            # read content of file as string
            content = str(file.read())
            # split data into tokens
            tokens = word_tokenize(content)
            # filter out tokens that are not alphabetic
            words = [x for x in tokens if x.isalpha()]
            # remove stop words
            words = [x for x in words if x not in stop_words]
            # convert to lowercase
            words = [x.lower() for x in words]

            for w in words:
                if len(w) <= 2:
                    words.remove(w)

            all_words.append(words)

        else:
            file_names.pop(member_index-count_pop)
            count_pop += 1

    return all_words, file_names
