from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from modules.process_data import process_data
from modules.svd import classify_into_topics
from modules.tdm import form_tdm, tf_idf_modification
from modules.topic_classification import define_key_words


app = Flask(__name__)


@app.route('/')
def upload_file():
    """
    Main page with uploading file possibility.

    :return: initial html template
    """
    return render_template("index.html")


@app.route("/analytics", methods=["GET", "POST"])
def upload():
    """
    Uploading images on the web page.

    :return: html template with the obtained images
    """
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        filename = f.filename
        ext_index = filename.find(".")
        extension = filename[ext_index + 1:]

        if extension == "zip" or extension == "tar.gz":
            if extension == "tar.gz":
                extension = "r:gz"
            all_words, file_names = process_data(filename, extension)
            unique_words, constructed_tdm = form_tdm(all_words)
            modified_tdm = tf_idf_modification(constructed_tdm)
            topic_documents = classify_into_topics(modified_tdm, file_names)
            classification = define_key_words(modified_tdm, unique_words)

            amount_of_documents = len(topic_documents)
            topics = list(range(amount_of_documents))
            docs_amount = []
            sorted_documents = dict(sorted(topic_documents.items()))
            amount_of_documents = 0
            classification_updated = dict()
            for key in sorted_documents:
                amount = len(sorted_documents[key])
                classification_updated[key] = classification[key]
                docs_amount.append(amount)
                amount_of_documents += amount

            keys = sorted_documents.keys()

            return render_template("analytics.html", documents=topic_documents, classification=classification_updated,
                                   keys=keys, length=len(keys), topics=topics, docs_amount=docs_amount,
                                   amount_of_documents=amount_of_documents)
        else:
            return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)