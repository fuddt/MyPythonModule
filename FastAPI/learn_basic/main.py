from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()



# 初歩的なGETリクエスト
@app.get("/")
async def read_root():
    """
    ブラウザでHOSTに続けて'/'を入力するとこの関数が呼ばれる
    Example: http://192.168.0.1:8000/
    """
    return {"Hello": "World"}

# パスパラメータを使ったGETリクエスト
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    """
    ブラウザでHOSTに続けて'/items/{item_id}'を入力するとこの関数が呼ばれる
    Example: http://192.168.0.1:8000/items/1
    """
    # 簡単な辞書を作ってみてパラメータによって返す値を変える
    items_dict = {"1": "apple", "2": "banana", "3": "orange"}
    return {"item_id": item_id, "item_name": items_dict.get(item_id, "item not found")}

# クエリパラメータを使ったGETリクエスト
@app.get("/items/")
async def read_item_query(item_id: int, q: str = None):
    """
    ブラウザでHOSTに続けて'/items/?item_id=1&q=apple'を入力するとこの関数が呼ばれる
    Example: http://192.168.0.1:8000/items/?item_id=1&q=apple
    """
    return {"item_id": item_id, "q": q}

# POSTメソッドでデータを追加するためのモデル
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# POSTリクエストで単一のアイテムを作成
@app.post("/items/")
async def create_item(item: Item):
    """
    ブラウザでHOSTに続けて'/items/'を入力して、
    ボディに以下のデータを入力するとこの関数が呼ばれる
    {
        "name": "apple",
        "description": "delicious",
        "price": 100,
        "tax": 10
    }
    """
    return item

# 入れ子構造のモデルを使ってPOSTリクエスト
class ShopInfo(BaseModel):
    name: str
    address: str

class Shop(BaseModel):
    shop_info: ShopInfo
    items: List[Item]

@app.post("/items/list/")
async def create_item_list(shop: Shop):
    """
    ブラウザでHOSTに続けて'/items/list/'を入力して、
    ボディに以下のデータを入力するとこの関数が呼ばれる
    {
        "shop_info": {
            "name": 'shop1',
            "address": 'tokyo'
        },
        "items": [
        {
            "name": "apple",
            "description": "delicious",
            "price": 100,
            "tax": 10
        },
        {
            "name": "banana",
            "description": "sweet",
            "price": 200,
            "tax": 20
        }
        ]
    }
    """
    return shop


# データ保持用のリスト
items = []

# POSTメソッドでアイテムをリストに追加する
# ちなみにこのスクリプトではリストに追加するだけで、データは保持されないので注意
@app.post("/items/add/")
async def add_item(item: Item):
    """
    ブラウザでHOSTに続けて'/items/add/'を入力して、
    ボディに以下のデータを入力するとこの関数が呼ばれる
    {
        "name": "apple",
        "description": "delicious",
        "price": 100,
        "tax": 10
    }
    """
    items.append(item)
    return {"message": "Item added successfully", "item": item}
