from app import db

class Clientes(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    DPI = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"<Cliente {self.nombre}>"

class Vehiculos(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer , nullable=True)
    disponibilidad = db.Column(db.Boolean, nullable=False)
    def __repr__(self):
        return f"<Vehiculo {self.marca} {self.modelo}>"
    

class Ventas(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f"<Venta {self.id}>"