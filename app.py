from flask import Flask, render_template, request
import sqlite3 as sql
import random

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'

#returns to the main page
@app.route('/')
def index():
    return render_template('main.html')

#adds new patient names
@app.route('/add', methods=['POST', 'GET'])
def name():
    error = None
    #when triggered by POST, enters the name and generates random id
    if request.method == 'POST':
        result = valid_name(random.randint(1, 100), request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('add.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('add.html', error=error)

#accesses database and inserts new values into the table
def valid_name(pid_name, first_name, last_name):
    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(pid INTEGER, firstname TEXT, lastname TEXT);')
    connection.execute('INSERT INTO users (pid, firstname, lastname) VALUES (?,?,?);', (pid_name, first_name, last_name))
    connection.commit()
    #displays the table
    cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
    return cursor.fetchall()

#deletes patient names
@app.route('/delete', methods=['POST', 'GET'])
def erase():
    error = None
    # displays the table
    connection = sql.connect('database.db')
    cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
    username=cursor.fetchall()
    # when triggered by POST, checks if patient name matches the existing one and deletes it
    if request.method == 'POST':
        result = delete_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('delete.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('delete.html', error=error, result=username)

#accesses database and deletes values from the table
def delete_name(first_name, last_name):
    connection = sql.connect('database.db')
    connection.execute('DELETE FROM users WHERE firstname=? AND  lastname=?;', (first_name, last_name))
    connection.commit()
    cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
    return cursor.fetchall()

if __name__ == "__main__":
    app.run()


