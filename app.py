from flask import Flask, render_template, jsonify
from database import DataBase
from flask_cors import CORS, cross_origin
from chart import *

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
@cross_origin()
def index():
    return render_template("index.html")


@app.route('/data_table', methods=["GET"])
@cross_origin()
def data_table():
    db = DataBase()
    return jsonify(db.data_table())


@app.route('/data_table/desc/<kanji>', methods=["PUT"])
@cross_origin()
def data_desc(kanji):
    db = DataBase()
    return jsonify(db.desc(kanji=kanji))


@app.route('/data_table/kanjis', methods=["GET"])
@cross_origin()
def data_kanji():
    db = DataBase()
    db.cursor.execute('''SELECT kanji FROM kanji''')
    data = db.cursor.fetchall()
    res_list = [i[0] for i in data]
    return jsonify(res_list)


@app.route('/data_table/box_1', methods=["GET"])
@cross_origin()
def data_box_1():
    data = box_1()
    return jsonify(data)


@app.route('/data_table/box_2', methods=["GET"])
@cross_origin()
def data_box_2():
    return jsonify(box_2())


@app.route('/data_table/box_3', methods=["GET"])
@cross_origin()
def data_box_3():
    return jsonify(box_3())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3305)
