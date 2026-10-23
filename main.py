from fastapi import FastAPI

app = FastAPI(
    title="InkaSec API",
    description="Backend Server para la plataforma InkaSec",
    version="1.0.0"
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok", "message": "Backend de InkaSec operando correctamente"}