from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    """
    アイテムを表すクラスです。

    Attributes:
        id (int): アイテムのID
        name (str): アイテムの名前
        description (str): アイテムの説明
        price (float): アイテムの価格
        tax (float): アイテムの税金
    """
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    tax = Column(Float, index=True)

Base.metadata.create_all(bind=engine)