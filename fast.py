from fastapi import FastAPI
import random
import hashlib


tags_metadata = [
    {
        "name": "hash",
        "description": "Accepts a password parameter in string format to be hashed",
    },
    {
        "name": "generate",
        "description": "On request generates a 12 random character password"
        
    },
]
app = FastAPI(

 title="My Py Hashgen",
    description="A starter code on building python hashers and generators with fastApi",
    version="1.0.0",
    openapi_tags=tags_metadata
)

@app.get('/',tags=['hash'])
##function to hash a password
async def root(password):
    ##specify constraints
    if len(password) < 6:
        return {'short':'password must be at least 6 characters'}
    ##hash data integrity using the powerful and fast blake hash algorithm
    return {"protected password":hashlib.blake2b(password.encode()).hexdigest()}

##route for generating strong passwords
@app.get('/generate',tags=['generate'])
##function to gewnerate a strong passowrd
async def generate():
    pass_list = [random.randint(65,122), random.randint(65,90), random.randint(65,122),random.randint(97,122),
        random.randint(65,90), random.randint(65,122), random.randint(65,90),random.randint(97,122),
        random.randint(65,122),random.randint(65,122),random.randint(97,122),random.randint(65,122)]
    return {"generated_password":''.join([chr(i) for i in pass_list])}
    
    

