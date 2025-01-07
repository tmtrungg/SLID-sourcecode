import datetime
from enum import Enum

from pydantic import BaseModel

class TokenSlowLiquidityBase(BaseModel):
    block_number: float
    log_index: float
    transaction_hash: str
    timestamp: datetime.datetime
    exchange_name: str
    contract_version: str
    contract_address: str
    token_address: str
    pool_balance: float
    category: str
    sender_address: str
    amount_token: float
    token_price: float


class TokenSlowLiquidityCreate(TokenSlowLiquidityBase):
    pass


class TokenSlowLiquidity(TokenSlowLiquidityBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
        use_enum_values = True
