from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List

app = FastAPI(
    title="InkaSec API",
    description="Backend Server para la plataforma InkaSec",
    version="1.0.0"
)
conn = UserConnection()

@app.get("/")
def root():
    return "Primero"

# 1. CREAR (POST)
@app.post("/api/insert")
def insert(user_data:UserCreate):
    conn.Write(user_data.model_dump()) 
    return {"message": "Usuario insertado correctamente"}

# 2. LISTAR (GET)
@app.get("/api/users", response_model=List[UserResponse])
def get_users():
    return conn.read_all()

# 3. MODIFICAR (PUT)
@app.put("/api/users/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    conn.update(user_id, user_data.model_dump())
    return {"message": f"Usuario con ID {user_id} actualizado correctamente"}

# 4. ELIMINAR (DELETE)
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    conn.delete(user_id)
    return {"message": f"Usuario con ID {user_id} eliminado correctamente"}


