#! /usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, request
from flask import render_template
import mysql.connector
app = Flask(__name__)

conn = mysql.connector.connect(host="127.0.0.1", user="root", password="ruffin", database="bdlivre")
cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/detail', methods=['GET', 'POST'])
def detail():
	idlivre = request.form['idlivre']
	query = "SELECT * FROM livre where id=%s"
	cursor.execute(query, (idlivre,))
	data = cursor.fetchall()
	return render_template('detail.html',data=data)

@app.route('/aide')
def listeLivre():
	cursor.execute("SELECT id, nom_livre, annee_edition FROM livre")
	table = cursor.fetchall()
	return render_template('aide.html', name=table)


if __name__ == '__main__':
    app.run(debug=True)
