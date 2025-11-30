from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": "Bravo ! Le Backend fonctionne !"}
print ("Backend is running...")