from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/category', methods=['POST'])
def setCategory():
    category_receive = request.form['category_give']
    index = len(list(db.category_info.find({}))) + 1
    collection = {'name': category_receive, 'index': index}
    db.category_info.insert_one(collection)

    return jsonify({'result': 'success'})

@app.route('/category/data', methods=['POST'])
def setData():
    category_receive = request.form['category_give']
    data_receive = request.form['data_give']

    index = db.category_info.find_one({'name': category_receive})['index']
    info ={'criteria1': data_receive}
    db["collection"+str(index)].insert_one(info)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)