from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import os
import pyotp
from dotenv import load_dotenv

app = FastAPI()

# 環境変数の読み込み
load_dotenv()

security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials):
    correct_username = os.getenv("USERNAME")
    correct_password = os.getenv("PASSWORD")
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    username = verify_credentials(credentials)
    secret = os.getenv("TOTP_SECRET")
    totp = pyotp.TOTP(secret)
    return {"message": "Please provide the TOTP code", "username": username}

@app.post("/verify")
def verify_totp(username: str, token: str):
    secret = os.getenv("TOTP_SECRET")
    totp = pyotp.TOTP(secret)
    if not totp.verify(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid TOTP token",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {"message": "2FA successful", "username": username}

@app.get("/")
def read_root(username: str = Depends(verify_credentials)):
    return {"message": "Hello, World!", "user": username}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, username: str = Depends(verify_credentials)):
    return {"item_id": item_id, "q": q, "user": username}

@app.post("/items/")
def create_item(item: Item, username: str = Depends(verify_credentials)):
    return {"item": item, "user": username}