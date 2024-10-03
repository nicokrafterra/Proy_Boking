import bcrypt
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from conexion import crear, get_db
from modelo import base,Usuario,Reserva
from schemas import UsuarioBase as cli
from schemas import ReservaU as usu
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

base.metadata.create_all(bind=crear)
# Crud usuario 
@app.get("/usuarios/")
async def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@app.post("/usuarios/", response_model=cli)
async def crear_usuario(usuario: cli, db: Session = Depends(get_db)):
    contraseña_encriptada = bcrypt.hashpw(usuario.contraseñaUsuario.encode('utf-8'), bcrypt.gensalt())
    
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correoElectronico=usuario.correoElectronico,
        contraseñaUsuario=contraseña_encriptada.decode('utf-8'),
        numeroCelular=usuario.numeroCelular,
        edad=usuario.edad,
        esAdmin=usuario.esAdmin
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.put("/usuarios/{usuario_id}", response_model=cli)
async def actualizar_usuario(usuario_id: int, usuario_actualizado: cli, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    for key, value in usuario_actualizado.dict().items():
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}", response_model=cli)
async def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    return usuario


# Reserva
@app.get("/reservas/")
async def obtener_reservas(db: Session = Depends(get_db)):
    reservas = db.query(Reserva).all()
    return reservas

@app.post("/reservas/", response_model=usu)
async def crear_reserva(reserva: usu, db: Session = Depends(get_db)):
    nueva_reserva = Reserva(**reserva.dict())
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)
    return nueva_reserva

@app.get("/reservas/{reserva_id}", response_model=usu)
async def obtener_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

@app.put("/reservas/{reserva_id}", response_model=usu)
async def actualizar_reserva(reserva_id: int, reserva_actualizada: usu, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    for key, value in reserva_actualizada.dict().items():
        setattr(reserva, key, value)

    db.commit()
    db.refresh(reserva)
    return reserva

@app.delete("/reservas/{reserva_id}", response_model=usu)
async def eliminar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    db.delete(reserva)
    db.commit()
    return reserva

