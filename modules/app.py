from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from modules.process_data import process_data
from modules.dtm import form_dtm, tf_idf_modification


app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template("index.html")


@app.route("/analytics", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))

        # WORK WITH LSA
        extension = "r:gz"
        all_words = process_data(f.filename, extension)

        all_words = all_words[:2]
        constructed_dtm = form_dtm(all_words)
        modified_dtm = tf_idf_modification(constructed_dtm)

        print(constructed_dtm)
        print(modified_dtm)

        return render_template("analytics.html", matrix=modified_dtm)


if __name__ == '__main__':
    app.run(debug=True)