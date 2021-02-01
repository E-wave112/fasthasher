from fastapi import FastAPI
import random
import hashlib

app = FastAPI()

@app.get('/')
async def root(password):
    ##specify constraints
    if len(password) < 6:
        return {'small':'password must be at least 6 characters'}
    ##hash data integrity using the powerful and fast blake hash algorithm
    return {"protected password":hashlib.blake2b(password.encode()).hexdigest()}

##route for generating strong passwords
@app.get('/generate')
async def generate():
    pass_list = [random.randint(65,90), random.randint(65,90), random.randint(65,90),random.randint(97,122),
        random.randint(65,90), random.randint(65,90), random.randint(65,90),random.randint(97,122),
        random.randint(65,90),random.randint(65,90),random.randint(97,122),random.randint(65,122)]
    return {"generated_password":''.join([chr(i) for i in pass_list])}
    
    

