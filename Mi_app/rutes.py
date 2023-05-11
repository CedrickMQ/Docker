from flask import Flask, render_template, request, redirect, url_for,flash, session, send_file
from conection import database

app = Flask(__name__)

app.secret_key = "NUT_NUT"


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login-validando', methods=['POST'])
def validar():
    if request.method == 'POST':
        usuario = request.form['Usuario']
        contrasena = request.form['password']
        cursor = database.cursor()
        cursor.execute('SELECT * FROM docker WHERE Usuario = %s AND Contraseña = %s', (usuario, contrasena))
        cuenta = cursor.fetchone()
        if cuenta:
            session['Usuario'] = cuenta[1]
            return redirect(url_for('buenas', msg= "Datos invalidos"))
        else:
            return render_template('login.html', msg= "Datos invalidos")
    else:
        return render_template('login.html', msg = "")
    
@app.route('/welcome')
def buenas():
    return render_template('welcome.html')
