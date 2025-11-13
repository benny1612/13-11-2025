from fastapi import FastAPI
import uvicorn
from logic import faence,caesar_cipher
app =FastAPI()
from pydantic import BaseModel
class Caesar(BaseModel):
    text:str
    offset:int
    mode:str

class Fence(BaseModel):
    text:str
    
    
@app.get("/test")
def test ():
    return{ "msg": "hi from test" }

@app.get("/test/:name")
def test2(q:str):
    with open("names.txt","a") as f:
        
        f.write(q)
    return {"msg":"saved user"}

@app.get("/fence/encrypt")
def fence_cipher(text:str):
    fence_cipher_word=faence(text)
    return { "encrypted_text": fence_cipher_word }

    
@app.post("/fence/decrypt")


async def fenca_encrypt(fence:Fence):
    fenca_encrypt_word=faence(fence.text)
    return {"decrypted":fenca_encrypt_word}
    
@app.post("/caesar")
async def caesar_cipher(caesar:Caesar):
     encrypt=caesar_cipher(caesar.text,caesar.offset)
     return{caesar.mode:encrypt}
    
   
   


    
    



















if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)