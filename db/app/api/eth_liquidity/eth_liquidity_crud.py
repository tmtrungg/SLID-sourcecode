from sqlalchemy.orm import Session
from typing import List
from app.api.eth_liquidity.eth_liquidity_models import TokenLiquidities
from app.api.eth_liquidity.eth_liquidity_schemas import TokenLiquidityCreate

"""`eth_token_liquidity` table API"""


def get_tokens(db: Session):
    return db.query(TokenLiquidities).order_by(TokenLiquidities.id.asc()).all()

def create_eth_tokenliq(db: Session, eth_tokenliqs: TokenLiquidityCreate):
    db_eth_tokenliq = TokenLiquidities(**eth_tokenliqs.dict())
    db.add(db_eth_tokenliq)
    db.commit()
    db.refresh(db_eth_tokenliq)
    return db_eth_tokenliq


def create_eth_tokenliq_bulk(db: Session, eth_tokenliqs: list[TokenLiquidityCreate]):
    try:
        db_eth_tokenliqs_bulk = [TokenLiquidities(**eth_tokenliq.dict()) for eth_tokenliq in eth_tokenliqs]
        db.add_all(db_eth_tokenliqs_bulk)
        db.commit()
        db.refresh(db_eth_tokenliqs_bulk)
        return db_eth_tokenliqs_bulk
    except Exception as e:
        print(e)
