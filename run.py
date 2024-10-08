from flask import Flask, request, redirect, url_for, render_template, session, flash
from app.modelos import Usuario  # Importa tu clase Usuario
from app.DAL import UsuarioDAL  # Importa tu capa DAL para manejar la base de datos
import config
from db import crear_conexion_bd  # Importa la función para conectar a la base de datos

app = Flask(__name__)
app.secret_key = config.Config.SECRET_KEY  # Llave secreta desde config.py

# Crear la conexión a la base de datos
db_connection = crear_conexion_bd()  # Aquí inicializas la conexión a la base de datos

# Crea una instancia del DAL
usuario_dal = UsuarioDAL(db_connection)  # Pasar la conexión a UsuarioDAL

# Ruta para la página de inicio de sesión (login)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']
        
        # Crear una instancia temporal de Usuario
        usuario = Usuario()
        
        # Intentar iniciar sesión usando los datos del formulario
        if usuario.login(username_input, password_input, usuario_dal):
            # Si el login es exitoso, redirigir al dashboard
            flash(f'Bienvenido {session["username"]}', 'success')
            return redirect(url_for('dashboard'))
        else:
            # Si el login falla, mostrar un mensaje de error
            flash('Error en el inicio de sesión. Inténtalo de nuevo.', 'danger')
    
    # Mostrar el formulario de login si el método es GET o si el login falla
    return render_template('login.html')

# Ruta para cerrar sesión (logout)
@app.route('/logout')
def logout():
    # Si el usuario está loggeado, cerrar sesión
    if 'username' in session:
        usuario = Usuario()
        usuario.logout()  # Llamar a la función logout para limpiar la sesión
        flash('Has cerrado sesión exitosamente.', 'success')
        return redirect(url_for('login'))
    else:
        flash('No estás autenticado.', 'warning')
        return redirect(url_for('login'))

# Ruta protegida (ejemplo de una página que requiere estar loggeado)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        # Si el usuario está loggeado, mostrar el dashboard
        return render_template('dashboard.html', username=session['username'])
    else:
        # Si no está loggeado, redirigir a la página de login
        flash('Debes iniciar sesión primero.', 'warning')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
