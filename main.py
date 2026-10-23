from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema
app = FastAPI(
    title="InkaSec API",
    description="Backend Server para la plataforma InkaSec",
    version="1.0.0"
)
conn = UserConnection()

@app.get("/")
def root():
    return "Primero"

@app.post("/api/insert")
def insert(user_data:UserSchema):
    conn.Write(user_data.model_dump()) 
    return {"message": "Usuario insertado correctamente"}

