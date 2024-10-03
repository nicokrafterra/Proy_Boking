from sqlalchemy import String, Integer,Column,Date,Boolean, ForeignKey
from conexion import base
from sqlalchemy.orm import relationship

class Usuario(base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False) 
    correoElectronico = Column(String(100), nullable=False)
    contraseñaUsuario = Column(String(225), nullable=False)
    numeroCelular = Column(String(20))
    edad = Column(Integer)
    esAdmin = Column(Boolean, default=False)  
    
class Reserva(base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))  
    fecha = Column(Date, nullable=False)
    tipo_Reserva = Column(String(225), nullable=False)  
    pagada = Column(Boolean, default=False)

    usuario = relationship("Usuario", back_populates="reservas")  

Usuario.reservas = relationship("Reserva", back_populates="usuario", cascade="all, delete-orphan")
