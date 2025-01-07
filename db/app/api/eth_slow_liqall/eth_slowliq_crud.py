from sqlalchemy.orm import Session
from typing import List
from app.api.eth_slow_liqall.eth_slowliq_models import TokenSlowLiquidities
from app.api.eth_slow_liqall.eth_slowliq_schemas import TokenSlowLiquidityCreate

"""`eth_token_liquidity` table API"""


def get_slowtokens(db: Session):
    return db.query(TokenSlowLiquidities).order_by(TokenSlowLiquidities.id.asc()).all()

def create_eth_slowtokenliq(db: Session, eth_tokenliqs: TokenSlowLiquidityCreate):
    db_eth_tokenliq = TokenSlowLiquidities(**eth_tokenliqs.dict())
    db.add(db_eth_tokenliq)
    db.commit()
    db.refresh(db_eth_tokenliq)
    return db_eth_tokenliq


def create_eth_slowtokenliq_bulk(db: Session, eth_tokenliqs: list[TokenSlowLiquidityCreate]):
    try:
        db_eth_tokenliqs_bulk = [TokenSlowLiquidities(**eth_tokenliq.dict()) for eth_tokenliq in eth_tokenliqs]
        db.add_all(db_eth_tokenliqs_bulk)
        db.commit()
        db.refresh(db_eth_tokenliqs_bulk)
        return db_eth_tokenliqs_bulk
    except Exception as e:
        print(e)
