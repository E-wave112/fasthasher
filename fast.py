from fastapi import FastAPI
import hashlib

app = FastAPI()

@app.get('/')
async def root(password: str):
    ##hash data integrity using the powerful and fast blake hash algorithm
    return {"protected password":hashlib.blake2b(password.encode()).hexdigest()}

