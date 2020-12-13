from fastapi import FastAPI
import hashlib

app = FastAPI()

@app.get('/')
async def root(password):
    ##specify constraints
    if len(password) < 6:
        return {'small':'password must be at least 6 characters'}
    ##hash data integrity using the powerful and fast blake hash algorithm
    return {"protected password":hashlib.blake2b(password.encode()).hexdigest()}
