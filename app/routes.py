from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Clientes
from app.models import Vehiculos
from app.models import Ventas

# Definir el Blueprint
main_bp = Blueprint('main', __name__)

# Página principal - Lista de usuarios
@main_bp.route('/')
def index():
    clientes = Clientes.query.all()
    return render_template('index.html', usuarios=clientes)

@main_bp.route('/cliente')
def cliente():
    clientes = Clientes.query.all()
    return render_template('cliente/index.html', usuarios=clientes)

# Formulario para agregar usuario
@main_bp.route('/cliente/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        DPI = request.form['DPI']
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        nuevo_usuario = Clientes(DPI=DPI, nombre=nombre, email=email, telefono=telefono)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('cliente/add_user.html')

# Formulario para editar usuario
@main_bp.route('/cliente/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    usuario = Clientes.query.get_or_404(id)
    if request.method == 'POST':
        usuario.DPI = request.form['DPI']
        usuario.nombre = request.form['nombre']
        usuario.email = request.form['email']
        usuario.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_user.html', usuario=usuario)

# Eliminar usuario
@main_bp.route('/cliente/delete/<int:id>', methods=['GET'])
def delete_user(id):
    usuario = Clientes.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/vehiculo')
def vehiculo():
    car = Vehiculos.query.all()
    #print(car)
    return render_template('vehiculo/index.html', vehiculos=car)

# Formulario para agregar vehiculo
@main_bp.route('/vehiculo/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = request.form['anio']
        precio = request.form['precio']
        nuevo_vehiculo = Vehiculos( marca=marca, modelo=modelo, anio=anio, precio=precio, disponible=True)
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('cliente/add_car.html')

# Formulario para editar vehiculo
@main_bp.route('/vehiculo/edit/<int:id>', methods=['GET', 'POST'])
def edit_car(id):
    car = Vehiculos.query.get_or_404(id)
    if request.method == 'POST':
        car.marca = request.form['marca']
        car.modelo = request.form['modelo']
        car.anio = request.form['anio']
        car.precio = request.form['precio']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_user.html', vehiculo=car)

# Eliminar Vehiculo
@main_bp.route('/vehiculo/delete/<int:id>', methods=['GET'])
def delete_car(id):
    usuario = Vehiculos.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/venta')
def venta():
    ventas = Ventas.query.all()
    return render_template('venta/index.html', ventas=ventas)

# Formulario para agregar venta
@main_bp.route('/venta/add', methods=['GET', 'POST'])
def add_venta():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        id_vehiculo = request.form['id_vehiculo']
        fecha = request.form['fecha']
        nueva_venta = Ventas(id_cliente=id_cliente, id_vehiculo=id_vehiculo, fecha=fecha)
        db.session.add(nueva_venta)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('venta/add_venta.html')

# Formulario para editar venta
@main_bp.route('/venta/edit/<int:id>', methods=['GET', 'POST'])
def edit_venta(id):
    venta = Ventas.query.get_or_404(id)
    if request.method == 'POST':
        venta.id_cliente = request.form['id_cliente']
        venta.id_vehiculo = request.form['id_vehiculo']
        venta.fecha = request.form['fecha']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_user.html', venta=venta)

# Eliminar venta
@main_bp.route('/venta/delete/<int:id>', methods=['GET'])
def delete_venta(id):
    venta = Ventas.query.get_or_404(id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for('main.index'))