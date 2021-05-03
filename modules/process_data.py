import tarfile
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def process_data(filename, extension):
    stop_words = set(stopwords.words('english'))
    porter = PorterStemmer()
    all_words = []
    tar = tarfile.open(filename, extension)

    for member in tar.getmembers():
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
            # stemming words (reducing each word to its root or base)
            # stemmed = [porter.stem(word) for word in words]

            all_words.append(words)

    return all_words
