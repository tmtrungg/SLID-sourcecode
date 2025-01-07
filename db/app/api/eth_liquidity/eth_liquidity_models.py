from datetime import datetime as dt

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.db import Base


class TokenLiquidities(Base):
    __tablename__ = "eth_alltoken_liquidity"

    id = Column(Integer, primary_key=True, index=True)
    block_number = Column(Float)
    log_index = Column(Float)
    transaction_hash = Column(String)
    timestamp = Column(DateTime, default=dt.utcnow)
    exchange_name = Column(String)
    contract_version = Column(String)
    contract_address = Column(String)
    token_address = Column(String)
    pool_balance = Column(Float)
    category = Column(String)
    sender_address = Column(String)
    amount_token = Column(Float)
    token_price = Column(Float)
    created_at = Column(DateTime, default=dt.utcnow)
