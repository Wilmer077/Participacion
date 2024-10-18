from flask import Flask,render_template,redirect,url_for,request,session,flash

app = Flask(__name__)
app.secret_key = 'secret_key' 

usuario = {
    'wilmer': 'contraseña123'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

   
        if username in usuario and usuario[username] == password:
            session['username'] = username 
            flash('Inicio de sesión exitoso')
            return redirect(url_for('iniciar'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/iniciar')
def iniciar():
    if 'username' in session:
        return render_template('iniciar.html', username=session['username'])
    else:
        flash('Por favor, inicie sesión primero.')
        return redirect(url_for('login'))

@app.route('/cerrar')
def cerrar():
    session.pop('username', None)
    flash('Has cerrado sesión.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)