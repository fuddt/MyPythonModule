from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from database import SessionLocal, engine, Base, Item as DBItem

app = FastAPI()

# Dependency
def get_db():
    """
    データベースセッションを取得します。

    Returns:
        db: データベースセッションオブジェクト
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ItemCreate(BaseModel):
    """
    アイテムの作成に使用するデータモデルです。

    :param name: アイテムの名前
    :type name: str
    :param description: アイテムの説明 (オプション)
    :type description: str, optional
    :param price: アイテムの価格
    :type price: float
    :param tax: アイテムの税金 (オプション)
    :type tax: float, optional
    """
    name: str
    description: str = None
    price: float
    tax: float = None

class Item(BaseModel):
    """
    商品の情報を表すクラスです。

    Attributes:
        id (int): 商品のID
        name (str): 商品の名前
        description (str, optional): 商品の説明
        price (float): 商品の価格
        tax (float, optional): 商品の税金
    """

    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        orm_mode = True

@app.post("/items/", response_model=Item)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item in the database.

    Parameters:
    - item: The item data to be created.
    - db: The database session.

    Returns:
    - The created item.

    この関数はデータベースに新しいアイテムを作成します。

    パラメーター:
    - item: 作成するアイテムのデータ。
    - db: データベースセッション。

    戻り値:
    - 作成されたアイテム。
    """
    db_item = DBItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    アイテムを読み込むためのエンドポイントです。

    Parameters:
        skip (int): スキップするアイテムの数（デフォルトは0）
        limit (int): 取得するアイテムの最大数（デフォルトは10）
        db (Session): データベースセッション（get_db関数によって提供されます）

    Returns:
        List[Item]: アイテムのリスト
    """
    items = db.query(DBItem).offset(skip).limit(limit).all()
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    指定されたアイテムIDに対応するアイテムを取得します。

    Parameters:
        - item_id (int): 取得するアイテムのID
        - db (Session, optional): データベースセッション (デフォルト値: Depends(get_db))

    Returns:
        - Item: 取得したアイテム

    Raises:
        - HTTPException: 指定されたアイテムが見つからない場合に発生します (ステータスコード: 404)
    """
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item