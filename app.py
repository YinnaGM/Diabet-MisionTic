from os import name
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/diabetdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

# Creacion de Database a traves de las librerías
db = SQLAlchemy(app)

# Importar los modelos
from models import Admin

# Crear el esquema de la DB
db.create_all()
db.session.commit()

#Rutas de páginas
@app.route('/')
def get_home():
    return 'Este es el inicio de la página, donde encontraras noticias y articulos relacionados a la diabetes tipo 1'

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