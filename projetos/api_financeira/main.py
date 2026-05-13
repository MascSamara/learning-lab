from fastapi import FastAPI

app = FastAPI(title="Personal Finance API")

@app.get("/")
def home():
    return {"message": "Minha API financeira está funcionando."}