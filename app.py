import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.workorderdb


@app.route('/')
def workorder():

    _items = db.workorderb.find()
    items = [item for item in _items]

    return render_template('workorder.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'asset': request.form['asset'],
        'description': request.form['description']
    }
    db.workorderdb.insert_one(item_doc)

    return redirect(url_for('workorder'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)