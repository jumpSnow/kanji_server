from flask import Flask, render_template, jsonify
from database import DataBase
from flask_cors import CORS
from chart import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data_table', methods=["GET"])
def data_table():
    db = DataBase()
    return jsonify(db.data_table())


@app.route('/data_table/desc/<kanji>', methods=["PUT"])
def data_desc(kanji):
    db = DataBase()
    return jsonify(db.desc(kanji=kanji))


@app.route('/data_table/kanjis', methods=["GET"])
def data_kanji():
    db = DataBase()
    db.cursor.execute('''SELECT kanji FROM kanji''')
    data = db.cursor.fetchall()
    res_list = [i[0] for i in data]
    return jsonify(res_list)


@app.route('/data_table/box_1', methods=["GET"])
def data_box_1():
    return jsonify(box_1())


@app.route('/data_table/box_2', methods=["GET"])
def data_box_2():
    return jsonify(box_2())


@app.route('/data_table/box_3', methods=["GET"])
def data_box_3():
    return jsonify(box_3())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3305)
