from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from modules.process_data import process_data
from modules.tdm import form_dtm, tf_idf_modification


app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template("index.html")


@app.route("/analytics", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))

        # # WORK WITH LSA
        # extension = "r:gz"
        # all_words = process_data(f.filename, extension)
        #
        # all_words = all_words[:2]
        # constructed_dtm = form_dtm(all_words)
        # modified_dtm = tf_idf_modification(constructed_dtm)
        #
        # print(constructed_dtm)
        # print(modified_dtm)

        topic_documents = {6: ['mini_newsgroups_to_test/alt.atheism/51121'], 11: ['mini_newsgroups_to_test/comp.graphics/37916'], 13: ['mini_newsgroups_to_test/comp.os.ms-windows.misc/9141'], 0: ['mini_newsgroups_to_test/comp.sys.ibm.pc.hardware/58829'], 1: ['mini_newsgroups_to_test/comp.sys.mac.hardware/50419'], 9: ['mini_newsgroups_to_test/comp.windows.x/64830'], 3: ['mini_newsgroups_to_test/misc.forsale/70337'], 4: ['mini_newsgroups_to_test/rec.autos/101564'], 7: ['mini_newsgroups_to_test/rec.motorcycles/103129', 'mini_newsgroups_to_test/sci.electronics/52464'], 2: ['mini_newsgroups_to_test/rec.sport.baseball/102590'], 17: ['mini_newsgroups_to_test/rec.sport.hockey/52550'], 15: ['mini_newsgroups_to_test/sci.crypt/14989'], 8: ['mini_newsgroups_to_test/sci.med/58061', 'mini_newsgroups_to_test/sci.space/59848'], 18: ['mini_newsgroups_to_test/soc.religion.christian/20491'], 12: ['mini_newsgroups_to_test/talk.politics.guns/53302'], 10: ['mini_newsgroups_to_test/talk.politics.mideast/75369'], 5: ['mini_newsgroups_to_test/talk.politics.misc/176869'], 14: ['mini_newsgroups_to_test/talk.religion.misc/82758']}

        classification = {0: ['concert', 'wupost', 'wupost'], 1: ['arizona', 'hilarie', 'find'], 2: ['arizona', 'kedz', 'hilarie'], 3: ['strom', 'scouts', 'et'], 4: ['sipp', 'joth', 'asuvax'], 5: ['ringing', 'strom', 'jfare'], 6: ['designated', 'sipp', 'joth'], 7: ['engines', 'select', 'hmarvel'], 8: ['engines', 'select', 'glang'], 9: ['lord', 'land', 'god'], 10: ['lord', 'land', 'god'], 11: ['norton', 'land', 'edwards'], 12: ['lord', 'god', 'turn'], 13: ['gilham', 'norton', 'armenians'], 14: ['position', 'olivea', 'paul'], 15: ['michael', 'tree', 'full'], 16: ['tesla', 'flyback', 'osc'], 17: ['attendance', 'mario', 'team']}

        topics = classification.values()
        return render_template("analytics.html", documents=topic_documents, classification=topics)


if __name__ == '__main__':
    app.run(debug=True)