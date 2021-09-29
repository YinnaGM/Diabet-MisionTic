from os import name
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/diabetdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

#if __name__ == "__main__": 
    #app.run()


# Creacion de Database a traves de las librerías
db = SQLAlchemy(app)

# Importar los modelos
from models import Admin, User, Profile

# Crear el esquema de la DB
db.create_all()
db.session.commit()

#Rutas de páginas

@app.route('/')
def get_home():
    return 'Este es el inicio de la página, donde encontraras noticias y articulos relacionados a la diabetes tipo 1'



# Ruta del registro de usuario
@app.route('/register')
def register():
    return render_template("register2.html")


@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]
    print(email)
    print(password)

    user = User(email,password)
    db.session.add(user)
    db.session.commit()
    return render_template("profile.html")


# Ruta para el perfil de usuario
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/create_profile', methods=['POST'])
def create_profile():
    sex = request.form["sex"]
    age = request.form["age"]
    height = request.form["heigth"]
    weight = request.form["weight"]
    insulin_type = request.form["insulin_type"]
    user_id = request.form["user_id"]
    print(sex)
    print(age)
    print(height)
    print(weight)
    print(insulin_type)
    print(user_id)

    profile = Profile(sex, age, height, weight, insulin_type, user_id)
    db.session.add(profile)
    db.session.commit()
    return "Su perfil se creo con exito"



#Rutas de otras acciones
@app.route('/admin', methods=['GET','POST'])
def crud_admin():
    if request.method == 'GET':
        # Hago algo
        print("Llego un GET")
        # Insertar un admin
        email = "admin2@cod.com"
        password = "54321"
        entry = Admin(email, password)
        db.session.add(entry)
        db.session.commit()
        return 'Esto fue un GET'
    elif request.method == 'POST':
        # Registrar un admin
        request_data = request.form
        email = request_data['email']
        password = request_data['password']

        print("Correo:" + email)
        print("Contraseña:" + password)

        # Insertar en la base de datos la canción

        return 'Se registro el admin exitosamente'

@app.route('/updateadmin',methods=['GET','POST'])
def update_admin():
    old_email = "admin@vis.com"
    new_email = "ad@vis.com"
    old_admin = Admin.query.filter_by(email = old_email).first()
    old_admin.email = new_email
    db.session.commit()
    return "Actualización exitosa"

@app.route('/getadmins')
def get_admins():
    admins = Admin.query.all()
    print(admins[0].email)
    return "Se trajo la lista de administradores registrados"

@app.route('/deleteadmin')
def delete_admin():
    admin_email = "ad@vis.com"
    admin = Admin.query.filter_by(email = admin_email).first()
    db.session.delete(admin)
    db.session.commit()
    return "Se eliminó el administrador"