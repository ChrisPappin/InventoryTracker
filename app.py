from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
from flask_cors import CORS
from models import createItem, getItems, deleteItem, editItem, getOneItem, createCSV
import os

app = Flask(__name__) #create server object

CORS(app)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        amount = request.form.get('amount')
        createItem(name, amount)

    items = getItems()

    return render_template('index.html', items=items)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    deleteItem(id)
    return redirect(url_for('index')) #return to home page

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    if request.method == 'POST':
        updatedItem=getOneItem(id)
        name = updatedItem[0][1]
        amount = request.form.get('new amount')
        editItem(name,amount)
        return redirect(url_for('index'))

    item=getOneItem(id)
    print(item)

    return render_template('edit.html',item=item)

@app.route('/getCSV', methods=['GET'])
def getCSV():
    createCSV()
    
    return send_file('Inventory.csv',
                     mimetype='text\csv',
                     attachment_filename='Inventory.csv',
                     as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)